#!/usr/bin/env python3
"""Limpia Markdown importado de un conversor (PDF/Word -> MD) para MkDocs.

Uso:
    python scripts/limpiar_md.py fichero.md [otro.md ...]
    python scripts/limpiar_md.py carpeta/            (todos los .md, recursivo)
    python scripts/limpiar_md.py fichero.md --nivel 3 --dry-run

Qué hace (sin tocar el contenido de los bloques ``` ):
  1. Convierte el fichero a UTF-8 si está en UTF-16.
  2. Elimina las etiquetas <span ...> y </span>.
  3. Quita las barras de escape: \\, \\. \\( \\" ...
  4. Cambia imagenes%5C por imagenes/ (rutas de imágenes).
  5. Convierte líneas _Título_ o __Título__ en encabezados (## por defecto).
  6. Quita espacios sobrantes (sangrías, finales de línea, líneas en blanco repetidas).
  7. Une líneas "__Nota: ...__" consecutivas en un aviso `!!! note`.
  8. Añade al fichero un bloque ```lang a un bloque de código sin lenguaje (--lang).
"""
import argparse
import re
import sys
from pathlib import Path

ESCAPADOS = r'\\([\\`*_{}\[\]()<>#+\-.!,"\'|~=:;])'


def leer(ruta: Path) -> str:
    datos = ruta.read_bytes()
    if datos[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return datos.decode("utf-16")
    return datos.decode("utf-8-sig")


def partir_codigo(texto: str):
    """Devuelve [(es_codigo, texto)] separando los bloques ``` del resto."""
    trozos, actual, en_codigo = [], [], False
    for linea in texto.split("\n"):
        if linea.lstrip().startswith("```"):
            if en_codigo:
                actual.append(linea)
                trozos.append((True, "\n".join(actual)))
                actual, en_codigo = [], False
            else:
                if actual:
                    trozos.append((False, "\n".join(actual)))
                actual, en_codigo = [linea], True
        else:
            actual.append(linea)
    if actual:
        trozos.append((en_codigo, "\n".join(actual)))
    return trozos


def limpiar_prosa(t: str) -> str:
    t = re.sub(r"</?span[^>]*>", "", t)
    t = re.sub(ESCAPADOS, r"\1", t)
    t = t.replace("%5C", "/")
    t = re.sub(r"[ \t]+$", "", t, flags=re.M)
    t = re.sub(r"^[ \t]+(?=\S)", "", t, flags=re.M)
    return t


def titulos_y_notas(t: str, nivel: int) -> str:
    lineas = t.split("\n")
    salida, i = [], 0
    while i < len(lineas):
        linea = lineas[i]
        s = linea.strip()
        if re.match(r"^__Nota", s):
            partes = []
            while i < len(lineas) and (
                lineas[i].strip().startswith("__")
                or (
                    lineas[i].strip() == ""
                    and i + 1 < len(lineas)
                    and lineas[i + 1].strip().startswith("__")
                )
            ):
                if lineas[i].strip():
                    partes.append(lineas[i].strip().strip("_").strip())
                i += 1
            salida += ["!!! note", "    " + " ".join(partes), ""]
            continue
        if re.match(r"^_{1,2}[^_\s].*[^_\s]_{1,2}\s*$", s) or re.match(r"^_{1,2}[^_\s]_{1,2}$", s):
            salida.append("#" * nivel + " " + s.strip("_").strip())
        else:
            salida.append(linea)
        i += 1
    return "\n".join(salida)


def procesar(texto: str, nivel: int, lang: str) -> str:
    trozos = []
    for es_codigo, contenido in partir_codigo(texto):
        if es_codigo:
            primera, _, resto = contenido.partition("\n")
            if lang and primera.strip() == "```":
                contenido = "```" + lang + "\n" + resto
            trozos.append(contenido)
        else:
            trozos.append(titulos_y_notas(limpiar_prosa(contenido), nivel))
    t = "\n".join(trozos)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("rutas", nargs="+", help="ficheros .md o carpetas")
    ap.add_argument("--nivel", type=int, default=2, help="nivel de los títulos _así_ (por defecto 2 = ##)")
    ap.add_argument("--lang", default="", help="lenguaje para bloques ``` sin lenguaje (p.ej. javascript)")
    ap.add_argument("--dry-run", action="store_true", help="no escribe, solo informa")
    ap.add_argument("--backup", action="store_true", help="guarda copia .bak antes de modificar")
    a = ap.parse_args()

    ficheros = []
    for r in map(Path, a.rutas):
        ficheros += sorted(r.rglob("*.md")) if r.is_dir() else [r]

    for f in ficheros:
        original = leer(f)
        nuevo = procesar(original, a.nivel, a.lang)
        spans = len(re.findall(r"<span", original))
        titulos = len(re.findall(r"(?m)^_{1,2}[^_\s].*_{1,2}\s*$", original))
        print(f"{f}: {spans} spans, {titulos} títulos _ _ -> {'sin cambios' if nuevo == original else 'modificado'}")
        if not a.dry_run and nuevo != original:
            if a.backup:
                f.with_suffix(f.suffix + ".bak").write_text(original, encoding="utf-8")
            f.write_text(nuevo, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
