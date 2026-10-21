---
marp: true
math: katex
paginate: true
html: true
size: 16:9
header: "2º DAM · 2026-2027"
theme: default
footer: "Lorena Sánchez Sánchez"
style: |
  :root { --fondo:#FFFFFF; --azul:#C8EDED; --rosa:#FDD4E3; --verde:#18D6C0; --amarillo:#F9EAC1; --rosa-fuerte:#FDB3CA; --texto:#4E4A42; --lila:#EE4091; }
  section { font-family: "Aptos", "Segoe UI", sans-serif; background:#FFF; color:#4E4A42; padding:50px 60px 40px; font-size:1.15em; line-height:1.30; }
  h1 { color:#EE4091; font-size:2.65em; font-weight:800; border-bottom:6px solid #C8EDED; padding-bottom:10px; }
  h2 { color:#18D6C0; font-size:2.15em; }
  h3 { color:#EE4091; }
  strong { color:#18D6C0; }
  section::after { background:white; border:3px solid #18D6C0; color:#18D6C0; width:36px; height:36px; border-radius:50%; right:15px; bottom:2px; display:flex; justify-content:center; align-items:center; font-size:1.3em; font-weight:700; }
  img { max-height:430px; display:block; margin:auto; }
  .small { font-size:.78em; }
  .tiny { font-size:.65em; }
  .center { text-align:center; }
  .two { display:grid; grid-template-columns:1fr 1fr; gap:30px; align-items:center; }
  .box { padding:18px 24px; background:#F4FCFC; border-left:8px solid #18D6C0; }
  .warn { padding:18px 24px; background:#FFF3F7; border-left:8px solid #EE4091; }
  .activity { padding:20px 26px; background:#F4FCFC; border:3px solid #18D6C0; border-radius:16px; }
  code { font-size:.86em; }
    footer { position:absolute; bottom:0; left:0; width:100%; height:30px; line-height:42px; background:var(--rosa-fuerte); color:var(--texto); text-align:center; font-size:0.80em; font-weight:600; }
      header { position:absolute; top:0; left:0; width:100%; height:40px; line-height:40px; background:#C8EDED; color:#4E4A42; font-weight:600; text-align:center; font-size:1.05em; }
---

# SOLUCIONES · UD2
## Introducción a JavaScript

### 2º DAM · Sesión práctica

**Soluciones completas de las actividades**

---

# Actividad 1 · Tipo test

| Nº | Respuesta | Explicación breve |
|---:|:---:|---|
| 1 | **C** | `typeof null` devuelve `"object"` |
| 2 | **B** | `Number("25")` devuelve `25` |
| 3 | **C** | `0` es un valor *falsy* |
| 4 | **B** | `"0"` es una cadena no vacía → `true` |
| 5 | **B** | `==` permite conversión; `===` exige igualdad estricta |
| 6 | **A** | `null == undefined` → `true` |
| 7 | **B** | `null === undefined` → `false` |
| 8 | **A** | `"Hola"` ya es *truthy* |
| 9 | **C** | `0` es *falsy*, por eso `||` continúa |
| 10 | **C** | `??` solo considera `null` y `undefined` |

---

# Actividad 2 · ¿Qué devuelve JavaScript?

## Ejercicio 1

```javascript
console.log(Number("15"));
console.log(Number("15px"));
console.log(Number(""));
console.log(Number(null));
console.log(Number(undefined));
```

### Solución

```text
15
NaN
0
0
NaN
```

---

# Actividad 2 · Ejercicio 1

### ¿Por qué?

| Expresión | Resultado | Motivo |
|---|---:|---|
| `Number("15")` | `15` | Número válido |
| `Number("15px")` | `NaN` | No representa un número completo |
| `Number("")` | `0` | Cadena vacía → `0` |
| `Number(null)` | `0` | `null` → `0` |
| `Number(undefined)` | `NaN` | No puede convertirse en número |

<div class="box">

**`NaN` significa "Not a Number".**

</div>

---

# Actividad 2 · Ejercicio 2

| Expresión | Resultado |
|---|---|
| `Boolean(0)` | `false` |
| `Boolean(1)` | `true` |
| `Boolean("")` | `false` |
| `Boolean("0")` | `true` |
| `Boolean(null)` | `false` |
| `Boolean(undefined)` | `false` |
| `Boolean("false")` | `true` |

### Idea clave

Una cadena que contiene texto, aunque sea `"0"` o `"false"`, es **truthy** porque no está vacía.

---

# Actividad 2 · Ejercicio 3

```javascript
5 == "5"             // true
5 === "5"            // false

0 == false           // true
0 === false          // false

null == undefined    // true
null === undefined   // false
```

### Regla

**`==`**

Compara permitiendo conversión de tipos.

**`===`**

Compara valor **y tipo** sin conversión implícita.

---

# Actividad 2 · Ejercicio 4

```javascript
console.log(0 || "A");
console.log(0 ?? "A");

console.log("" || "B");
console.log("" ?? "B");

console.log(null || "C");
console.log(null ?? "C");

console.log(undefined || "D");
console.log(undefined ?? "D");
```

### Solución

```text
A
0
B
""
C
C
D
D
```

---

# Actividad 2 · Ejercicio 4

| Expresión | Resultado |
|---|---|
| `0 || "A"` | `"A"` |
| `0 ?? "A"` | `0` |
| `"" || "B"` | `"B"` |
| `"" ?? "B"` | `""` |
| `null || "C"` | `"C"` |
| `null ?? "C"` | `"C"` |
| `undefined || "D"` | `"D"` |
| `undefined ?? "D"` | `"D"` |

---

# Actividad 2 · Ejercicio 4

## ¿Por qué se comportan diferente?

### `||`

Busca el primer valor **truthy**.

```javascript
0 || "A"     // "A"
"" || "B"    // "B"
```

### `??`

Solo considera ausencia de valor cuando es:

```javascript
null
undefined
```

Por eso:

```javascript
0 ?? "A"     // 0
"" ?? "B"    // ""
```

<div class="warn">

**Regla:** `||` trata `0` y `""` como falsos; `??` conserva esos valores.

</div>

---

# Actividad 3 · Condiciones y operadores lógicos

Partimos de:

```javascript
let edad = 20;
let tieneEntrada = true;
let estaInvitado = false;
```

---

# Actividad 3 · Ejercicio 1

### Condición

Debe entrar si:

- tiene entrada **Y**
- tiene 18 años o más.

### Solución

```javascript
tieneEntrada && edad >= 18
```

Por ejemplo:

```javascript
if (tieneEntrada && edad >= 18) {
    console.log("Puede entrar");
}
```

---

# Actividad 3 · Ejercicio 2

### Condición

Puede entrar si:

- tiene entrada **Y** tiene 18 años o más
- **O** está invitado.

### Solución

```javascript
if ((tieneEntrada && edad >= 18) || estaInvitado) {
    console.log("Puede entrar");
} else {
    console.log("No puede entrar");
}
```

---

# Actividad 3 · Ejercicio 3

Añadimos:

```javascript
let usuarioBloqueado = false;
```

La persona no puede entrar si está bloqueada.

### Solución

```javascript
if ((tieneEntrada && edad >= 18) && !usuarioBloqueado) {
    console.log("Puede entrar");
} else {
    console.log("No puede entrar");
}
```

---

### El operador `!`

```javascript
!true   // false
!false  // true
```

Por tanto:

```javascript
!usuarioBloqueado
```

significa:

> El usuario **NO** está bloqueado.

---

# Actividad 3 · Ejercicio 4

Tenemos:

```javascript
let edad = 17;
let tieneEntrada = true;
let estaInvitado = false;

let puedeEntrar =
    edad >= 18 && tieneEntrada || estaInvitado;
```

### 1. ¿Qué valor tiene?

```text
false
```

Porque:

```javascript
edad >= 18
```

es:

```text
false
```
---

Y:

```javascript
false && true
```

es:

```text
false
```

Finalmente:

```javascript
false || false
```

es:

```text
false
```

---

# Actividad 3 · Ejercicio 4

### 2. ¿Qué condición se evalúa?

JavaScript interpreta:

```javascript
edad >= 18 && tieneEntrada || estaInvitado
```

como:

```javascript
(edad >= 18 && tieneEntrada) || estaInvitado
```

porque `&&` tiene **mayor precedencia** que `||`.

---

# Actividad 3 · Ejercicio 4

### 3. ¿Cambiaría con estos paréntesis?

```javascript
edad >= 18 && (tieneEntrada || estaInvitado)
```

Con los valores:

```javascript
edad = 17
tieneEntrada = true
estaInvitado = false
```

el resultado sigue siendo:

```text
false
```

Porque:

```javascript
edad >= 18
```

es `false`.


---

Por tanto:

```javascript
false && (true || false)
```

es:

```text
false
```

### Importante

Aunque en este caso el resultado coincide, **las condiciones no son equivalentes en todos los casos**.

---

# Actividad 3 · Ejercicio 5 · `??`

Tenemos:

```javascript
let nombre = null;
```

### Solución

```javascript
let nombreMostrado = nombre ?? "Usuario desconocido";

console.log(nombreMostrado);
```

Resultado:

```text
Usuario desconocido
```

---

# Actividad 3 · Ejercicio 5

Después probamos:

```javascript
nombre = "";
```

Resultado:

```text
""
```

Porque `??` **no considera la cadena vacía como ausencia**.

---

### Si tenemos:

```javascript
nombre = "Ana";
```

Resultado:

```text
"Ana"
```

### Resumen

| `nombre` | `nombre ?? "Usuario desconocido"` |
|---|---|
| `null` | `"Usuario desconocido"` |
| `""` | `""` |
| `"Ana"` | `"Ana"` |

---

# Actividad 4 · Mini programa

## Sistema de acceso a una plataforma DAM

### Requisitos

El acceso se permite cuando:

```text
edad >= 18
Y
NO está bloqueado
Y
(es profesor O es admin)
```

---

# Actividad 4 · Solución completa

```javascript
let usuario = prompt("Usuario:");
let edad = Number(prompt("Edad:"));

let esProfesor = false;
let bloqueado = false;

usuario = usuario ?? "Usuario desconocido";

if (Number.isNaN(edad)) {
    console.log("La edad introducida no es válida.");
} else {

    let puedeAcceder =
        edad >= 18 &&
        !bloqueado &&
        (esProfesor || usuario === "admin");

    if (puedeAcceder) {
        console.log("Acceso permitido");
    } else {
        console.log("Acceso denegado");
    }
}
```

---

# Actividad 4 · Usuario vacío

La actividad pide utilizar `??` para mostrar un usuario alternativo.

La solución es:

```javascript
usuario = usuario ?? "Usuario desconocido";
```

### Atención

`??` sustituye:

```javascript
null
undefined
```

pero **no** sustituye:

```javascript
""
```

Por tanto, si el usuario pulsa simplemente **Aceptar** dejando el campo vacío, `prompt()` devuelve `""`.

Si queremos considerar también la cadena vacía como usuario no válido, podemos utilizar:

```javascript
usuario = usuario || "Usuario desconocido";
```

Pero para practicar específicamente `??`, la solución pedida es:

```javascript
usuario = usuario ?? "Usuario desconocido";
```

---

# Actividad 4 · Condición final

La condición debe representar:

> Tiene 18 años o más, no está bloqueado y además es profesor o es admin.

### Solución

```javascript
let puedeAcceder =
    edad >= 18 &&
    !bloqueado &&
    (esProfesor || usuario === "admin");
```

También puede escribirse en una sola línea:

```javascript
let puedeAcceder = edad >= 18 && !bloqueado && (esProfesor || usuario === "admin");
```

---

# Actividad 4 · Comprobación de casos

| Edad | Usuario | Profesor | Bloqueado | Resultado |
|---:|---|:---:|:---:|---|
| 20 | `ana` | sí | no | **Acceso permitido** |
| 17 | `ana` | sí | no | **Acceso denegado** |
| 25 | `admin` | no | no | **Acceso permitido** |
| 25 | `ana` | no | no | **Acceso denegado** |
| 25 | `ana` | sí | sí | **Acceso denegado** |

---

# Actividad 4 · Explicación de los casos

### Caso 1

```text
20 · ana · profesor · no bloqueado
```

```javascript
20 >= 18                 // true
!false                   // true
true || false            // true
```

Resultado:

```text
Acceso permitido
```

---

### Caso 2

```text
17 · ana · profesor · no bloqueado
```

```javascript
17 >= 18                 // false
```

Aunque sea profesor, no cumple la edad mínima.

Resultado:

```text
Acceso denegado
```

---

# Actividad 4 · Explicación de los casos

### Caso 3

```text
25 · admin · no profesor · no bloqueado
```

```javascript
25 >= 18                 // true
!false                   // true
false || true            // true
```

Resultado:

```text
Acceso permitido
```

---

### Caso 4

```text
25 · ana · no profesora · no bloqueada
```

```javascript
25 >= 18                 // true
!false                   // true
false || false           // false
```

Resultado:

```text
Acceso denegado
```

---

# Actividad 4 · Explicación de los casos

### Caso 5

```text
25 · ana · profesora · bloqueada
```

```javascript
25 >= 18                 // true
!true                    // false
```

Como está bloqueada:

```text
Acceso denegado
```

---

# 🚀 Reto final

## Condición

Un alumno puede presentarse si:

- tiene una nota de evaluación de **5 o más**
- y **no** tiene una incidencia
- **o** tiene una autorización especial.

### Solución

```javascript
let nota = 7;
let tieneIncidencia = false;
let tieneAutorizacion = false;

let puedePresentarse =
    (nota >= 5 && !tieneIncidencia) ||
    tieneAutorizacion;
```

---

# 🚀 Reto final · Operador ternario

Transformamos el resultado en un mensaje:

```javascript
let mensaje =
    puedePresentarse
        ? "Puede presentarse"
        : "No puede presentarse";

console.log(mensaje);
```

También puede escribirse:

```javascript
console.log(
    puedePresentarse
        ? "Puede presentarse"
        : "No puede presentarse"
);
```

---

# Reto final · Ejemplos

| Nota | Incidencia | Autorización | Resultado |
|---:|:---:|:---:|---|
| 7 | no | no | **Puede presentarse** |
| 4 | no | no | **No puede presentarse** |
| 4 | sí | sí | **Puede presentarse** |
| 7 | sí | no | **No puede presentarse** |
| 5 | no | no | **Puede presentarse** |

---

# 🧠 Resumen de operadores

| Operador | Significado |
|---|---|
| `==` | Igualdad con conversión |
| `===` | Igualdad estricta |
| `&&` | Y |
| `||` | O / primer *truthy* |
| `!` | Negación |
| `??` | Valor alternativo para `null`/`undefined` |
| `?:` | Operador ternario |

---

# 📌 Reglas fundamentales

### `==` vs `===`

```javascript
5 == "5"     // true
5 === "5"    // false
```

**Recomendación habitual:** utilizar `===` cuando se quiere comparar de forma estricta.

---

### `||` vs `??`

```javascript
0 || "A"     // "A"
0 ?? "A"     // 0
```

```javascript
"" || "A"    // "A"
"" ?? "A"    // ""
```

```javascript
null || "A"  // "A"
null ?? "A"  // "A"
```

---

# ✅ Solución final completa

```javascript
// ACTIVIDAD 4 · MINI PROGRAMA

let usuario = prompt("Usuario:");
let edad = Number(prompt("Edad:"));

let esProfesor = false;
let bloqueado = false;

// Valor alternativo si prompt devuelve null
usuario = usuario ?? "Usuario desconocido";

// Comprobamos la edad
if (Number.isNaN(edad)) {

    console.log("La edad introducida no es válida.");

} else {

    let puedeAcceder =
        edad >= 18 &&
        !bloqueado &&
        (esProfesor || usuario === "admin");

    if (puedeAcceder) {
        console.log("Acceso permitido");
    } else {
        console.log("Acceso denegado");
    }
}
```

---

# 🎯 Reto final · Solución completa

```javascript
let nota = 7;
let tieneIncidencia = false;
let tieneAutorizacion = false;

let puedePresentarse =
    (nota >= 5 && !tieneIncidencia) ||
    tieneAutorizacion;

let mensaje =
    puedePresentarse
        ? "Puede presentarse"
        : "No puede presentarse";

console.log(mensaje);
```

---

# FIN

## UD2 · Introducción a JavaScript

### Conceptos trabajados

- Conversión de tipos
- `Number()` y `Boolean()`
- `==` y `===`
- `null` y `undefined`
- Valores *truthy/falsy*
- `&&`, `||`, `!` y `??`
- Precedencia de operadores
- `if / else`
- Operador ternario
- Construcción de condiciones complejas
