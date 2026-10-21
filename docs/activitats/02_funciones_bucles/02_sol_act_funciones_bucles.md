# Soluciones · Funciones y bucles

## Actividad 1

```js
function esPedidoValido(pedido) {
    if (pedido.estado === "cancelado") return false;
    if (pedido.importe < 0) return false;
    return true;
}

```

```js

function calcularImportePedido(pedido) {
    switch (pedido.tipo) {
        case "A":
            return pedido.importe * 1.21;

        case "B":
            return pedido.importe * 1.10;

        case "C":
            return pedido.importe;

        default:
            return null;
    }
}

```

```js
function calcularTotal(pedidos) {
    let total = 0;
    let pedidosValidos = 0;

    for (let i = 0; i < pedidos.length; i++) {
        const pedido = pedidos[i];

        if (pedido.estado === "cancelado") {
            continue;
        }

        if (pedido.importe < 0) {
            break;
        }

        const importe = calcularImportePedido(pedido);

        if (importe === null) {
            continue;
        }

        total += importe;
        pedidosValidos++;
    }

    return {
        total,
        pedidosValidos
    };
}

```

```js

function procesarPedidos(pedidos) {
    return calcularTotal(pedidos);
}
```

## Actividad 2

Una solución posible:

```js
function esAprobado(nota) {
    return nota >= 5;
}

function calcularMedia(notas) {
    let suma = 0;
    let cantidad = 0;

    for (let i = 0; i < notas.length; i++) {
        const nota = notas[i];

        if (nota === null) {
            continue;
        }

        if (typeof nota !== "number" ||
            nota < 0 ||
            nota > 10) {
            break;
        }

        suma += nota;
        cantidad++;
    }

    if (cantidad === 0) {
        return null;
    }

    return suma / cantidad;
}
```

```js
function obtenerEstadisticas(notas) {
    if (!Array.isArray(notas)) {
        return null;
    }

    if (notas.length === 0) {
        return null;
    }

    let suma = 0;
    let cantidad = 0;
    let aprobados = 0;
    let suspensos = 0;
    let maxima = null;
    let minima = null;

    for (let i = 0; i < notas.length; i++) {
        const nota = notas[i];

        if (nota === null) {
            continue;
        }

        if (typeof nota !== "number" ||
            nota < 0 ||
            nota > 10) {
            break;
        }

        suma += nota;
        cantidad++;

        if (esAprobado(nota)) {
            aprobados++;
        } else {
            suspensos++;
        }

        if (maxima === null || nota > maxima) {
            maxima = nota;
        }

        if (minima === null || nota < minima) {
            minima = nota;
        }
    }

    if (cantidad === 0) {
        return null;
    }

    return {
        media: suma / cantidad,
        aprobados,
        suspensos,
        maxima,
        minima
    };
}

function mostrarInforme(estadisticas) {
    if (!estadisticas) {
        console.log("Datos no válidos");
        return;
    }

    console.log(`Media: ${estadisticas.media}`);
    console.log(`Aprobados: ${estadisticas.aprobados}`);
    console.log(`Suspensos: ${estadisticas.suspensos}`);
    console.log(`Nota máxima: ${estadisticas.maxima}`);
    console.log(`Nota mínima: ${estadisticas.minima}`);
}
```

## Actividad 3

```js
function procesarUsuarios(usuarios, callback) {
    for (let i = 0; i < usuarios.length; i++) {
        callback(usuarios[i]);
    }
}
```

### Mostrar nombres

```js
procesarUsuarios(
    usuarios,
    usuario => console.log(usuario.nombre)
);
```

### Mayores de edad

```js
procesarUsuarios(
    usuarios,
    usuario => {
        if (usuario.edad >= 18) {
            console.log(usuario.nombre);
        }
    }
);
```

### Usuarios activos

```js
procesarUsuarios(
    usuarios,
    usuario => {
        if (usuario.activo) {
            console.log(usuario.nombre);
        }
    }
);
```

## Actividad 4

```js
function calcularMedia(notas) {
    let suma = 0;

    for (let i = 0; i < notas.length; i++) {
        suma += notas[i];
    }

    return suma / notas.length;
}

function analizarAlumnos(alumnos, callback) {
    for (let i = 0; i < alumnos.length; i++) {
        const alumno = alumnos[i];
        const media = calcularMedia(alumno.notas);

        callback({
            nombre: alumno.nombre,
            media,
            aprobado: media >= 5
        });
    }
}
```

### Todos

```js
analizarAlumnos(alumnos, resultado => {
    console.log(resultado);
});
```

### Solo aprobados

```js
analizarAlumnos(alumnos, resultado => {
    if (resultado.aprobado) {
        console.log(resultado);
    }
});
```

### Media superior a 8

```js
analizarAlumnos(alumnos, resultado => {
    if (resultado.media > 8) {
        console.log(resultado);
    }
});
```

La función `analizarAlumnos()` **no necesita modificarse** para añadir nuevos criterios.

## Test (1–10)

| Pregunta | Respuesta | Idea clave |
|---:|:---:|---|
| 1 | C | El contador nunca cambia. |
| 2 | B | `continue` salta la iteración. |
| 3 | A | `break` termina el bucle. |
| 4 | C | `break` termina; `continue` continúa. |
| 5 | B | `do...while` ejecuta al menos una vez. |
| 6 | B | Ignorar elemento y continuar. |
| 7 | C | Falta `break` y hay *fall-through*. |
| 8 | B | `switch` compara con igualdad estricta. |
| 9 | B | Falta devolver el resultado. |
| 10 | C | `return a + b`. |

## Test (11–20)

| Pregunta | Respuesta | Idea clave |
|---:|:---:|---|
| 11 | D | Se utiliza el valor por defecto. |
| 12 | B | `return` termina la función. |
| 13 | C | Una responsabilidad clara. |
| 14 | B | Devuelve el menor. |
| 15 | A | La función se almacena y se invoca. |
| 16 | B | Las funciones pueden tratarse como valores. |
| 17 | C | `doble(5)` devuelve `10`. |
| 18 | B | `doble` se pasa como argumento. |
| 19 | A | Arrow function equivalente. |
| 20 | C | Con `{}` hace falta `return`. |

## Test (21–30)

| Pregunta | Respuesta | Idea clave |
|---:|:---:|---|
| 21 | B | Arrow con retorno implícito. |
| 22 | B | Se reutiliza el recorrido. |
| 23 | A | Primero se ejecuta `saludar()`. |
| 24 | B | Se pasa la función sin ejecutarla. |
| 25 | B | `null` debe ignorarse en este caso. |
| 26 | A | `continue` ignora el dato. |
| 27 | B | `length` no equivale a procesados. |
| 28 | A | Primero se ignora `null`; luego se valida. |
| 29 | B | Se separa procesamiento y presentación. |
| 30 | B | El callback recibe el resultado calculado. |

## Qué debes dominar

Al terminar la sesión deberías poder explicar, sin consultar apuntes:

- Cuándo utilizar `for`, `while` y `do...while`.
- Cuándo utilizar `break` y `continue`.
- Qué sucede si olvidamos un `break` en `switch`.
- Cómo diseñar funciones pequeñas y reutilizables.
- Diferencia entre parámetros y argumentos.
- Cómo funciona `return`.
- Qué significa que una función sea un valor.
- Qué es un callback.
- Diferencia entre ejecutar una función y pasarla como argumento.
- Cómo convertir funciones sencillas a arrow functions.

!!! tip "Reto final"

    si puedes modificar los criterios de filtrado sin tocar la función que procesa los datos, has conseguido una buena separación de responsabilidades.
