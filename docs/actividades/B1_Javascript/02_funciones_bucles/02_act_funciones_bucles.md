---
marp: true
math: katex
paginate: true
html: true
size: 16:9
header: "2º DAW · 2026-2027"
theme: default
footer: "Lorena Sánchez Sánchez"
---

# FUNCIONES Y BUCLES EN JAVASCRIPT

## Actividades + test de razonamiento

**2º DAW · Desarrollo en Entorno Cliente**

**Duración máxima: 2 h 30 min · Nivel alto**

---

# 1. Objetivos

Al finalizar la sesión deberás ser capaz de:

- Elegir entre `for`, `while` y `do...while`.
- Utilizar correctamente `break` y `continue`.
- Controlar situaciones complejas con `switch`.
- Diseñar funciones con una única responsabilidad.
- Trabajar con parámetros, argumentos y `return`.
- Utilizar funciones como valores y callbacks.
- Transformar funciones tradicionales en funciones flecha.
- Analizar código y detectar errores de lógica.

**Importante:** no se busca únicamente que el programa funcione. Debes justificar por qué has elegido cada estructura.

---

# 2. Organización de la sesión

| Parte | Tiempo |
| --- | --- |
| Actividad 1 · Refactorización | 30 min |
| Actividad 2 · Analizador de notas | 50 min |
| Actividad 3 · Callbacks y arrow functions | 35 min |
| Actividad 4 · Reto final | 25 min |
| Test · 30 preguntas | 10 min |
| **TOTAL** | **150 min** |

El tiempo es máximo. Si terminas una actividad antes, utiliza el tiempo restante para revisar casos límite y justificar tus decisiones.

---

# ACTIVIDAD 1 · Refactorización

## 30 minutos

Analiza el siguiente código:


```js
function procesarPedidos(pedidos) {
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
```


---


```js
        switch (pedido.tipo) {
            case "A":
                total += pedido.importe * 1.21;
                pedidosValidos++;
                break;

            case "B":
                total += pedido.importe * 1.10;
                pedidosValidos++;
                break;

            case "C":
                total += pedido.importe;
                pedidosValidos++;
                break;

            default:
                console.log("Tipo desconocido");
        }
    }

    return { total, pedidosValidos };
}
```


---

# ACTIVIDAD 1 · Analiza antes de modificar

Responde:

1. ¿Qué ocurre con un pedido cancelado?
2. ¿Qué ocurre cuando aparece un importe negativo?
3. ¿Qué ocurre con un tipo de pedido desconocido?
4. ¿Por qué `continue` tiene sentido en un caso y `break` en otro?
5. ¿Qué ocurriría si eliminásemos el `break` de uno de los `case`?
6. ¿Qué responsabilidades diferentes tiene actualmente `procesarPedidos()`?
7. ¿Qué partes convertirías en funciones independientes?

**Objetivo:** no programes todavía. Primero identifica la lógica que debe separarse.

---

# ACTIVIDAD 1 · Refactoriza

Divide el programa en funciones pequeñas:


```text
esPedidoValido(pedido)
calcularImportePedido(pedido)
calcularTotal(pedidos)
procesarPedidos(pedidos)
```


Condiciones:

- Debe mantenerse el comportamiento general.
- Utiliza `switch` para decidir el tipo.
- Mantén `continue` para pedidos cancelados.
- Mantén `break` para detener el procesamiento ante un importe negativo.
- Las funciones deben tener una responsabilidad clara.
- `procesarPedidos()` debe ser sencilla de leer.

---

# ACTIVIDAD 2 · Analizador de notas

## 50 minutos

Trabaja con:


```js
const notas = [
    4.5, 7, 8.5, 3, null,
    9.5, 6, 10, 2.5, 7.5, 5
];
```


En este ejercicio:

- `null` significa **alumno sin nota** y debe ignorarse.
- Las notas válidas están entre `0` y `10`.
- Si aparece una nota de otro tipo o fuera del rango, el procesamiento debe detenerse.

---

# ACTIVIDAD 2 · Funciones

Implementa:


```js
esAprobado(nota)
calcularMedia(notas)
obtenerEstadisticas(notas)
mostrarInforme(estadisticas)
```


`obtenerEstadisticas()` debe devolver:


```js
{
    media,
    aprobados,
    suspensos,
    maxima,
    minima
}
```


No utilices `reduce()`.

---

# ACTIVIDAD 2 · Requisitos

Tu solución debe:

- Utilizar funciones con una única responsabilidad.
- Utilizar `return`.
- Utilizar al menos un `continue`.
- Utilizar un `break` para detener datos inválidos.
- Ignorar los `null`.
- No contar los `null` en la media.
- No contar los `null` como aprobados ni suspensos.
- Detectar listas vacías.
- Detectar que el argumento no sea un array.

**Pregunta importante:** si utilizas `notas.length` directamente para calcular la media, ¿qué problema aparece cuando existen valores `null`?

---

# ACTIVIDAD 2 · Casos que debes probar

Comprueba como mínimo:


```js
obtenerEstadisticas([
    5, 6, 7, 8
]);
```


```js
obtenerEstadisticas([
    5, null, 7, null, 9
]);
```


```js
obtenerEstadisticas([]);
```


```js
obtenerEstadisticas("5,6,7");
```


```js
obtenerEstadisticas([
    5, 7, 11, 8
]);
```


Explica qué debería devolver cada caso antes de ejecutarlo.

---

# ACTIVIDAD 3 · Callbacks

## 35 minutos

Tenemos:


```js
const usuarios = [
    { nombre: "Ana", edad: 21, activo: true },
    { nombre: "Luis", edad: 17, activo: true },
    { nombre: "Marta", edad: 32, activo: false },
    { nombre: "Pablo", edad: 28, activo: true }
];
```


Implementa:


```js
function procesarUsuarios(usuarios, callback) {
    // ...
}
```


La función debe recorrer el array y ejecutar `callback()` para cada usuario.

---

# ACTIVIDAD 3 · Diferentes callbacks

Crea tres callbacks:

### A. Mostrar nombres


```js
usuario => console.log(usuario.nombre)
```


### B. Mostrar mayores de edad

Solo debe mostrar usuarios con:


```js
usuario.edad >= 18
```


### C. Mostrar usuarios activos

Solo debe mostrar:


```js
usuario.activo === true
```


Prueba los tres callbacks con `procesarUsuarios()`.

---

# ACTIVIDAD 3 · Reflexión

Responde:

1. ¿Quién decide cómo recorrer el array?
2. ¿Quién decide qué hacer con cada usuario?
3. ¿Qué ventaja aporta pasar una función como argumento?
4. ¿Podrías sustituir los callbacks por tres funciones completamente independientes?
5. ¿Qué parte del código es reutilizable?
6. Convierte todos los callbacks posibles a funciones flecha.

**Idea clave:** la función que recorre los usuarios no necesita conocer qué operación concreta se realizará con cada usuario.

---

# ACTIVIDAD 4 · RETO FINAL

## 25 minutos

Crea:


```js
const alumnos = [
    { nombre: "Ana", notas: [8, 9, 7] },
    { nombre: "Luis", notas: [4, 5, 3] },
    { nombre: "Marta", notas: [9, 10, 8] },
    { nombre: "Pablo", notas: [6, 7, 5] }
];
```


Implementa:


```js
analizarAlumnos(alumnos, callback)
```


---

La función debe calcular para cada alumno:


```js
{
    nombre,
    media,
    aprobado
}
```


y pasar el resultado al callback.

---

# ACTIVIDAD 4 · Callbacks del reto

Crea tres formas de utilizar `analizarAlumnos()`:

### Opción A

Mostrar todos los resultados.

### Opción B

Mostrar únicamente los alumnos aprobados.

### Opción C

Mostrar únicamente los alumnos cuya media sea superior a `8`.

Condiciones:

- Utiliza funciones.
- Utiliza un bucle.
- Utiliza un callback.
- Utiliza al menos una función flecha.
- No repitas la lógica de cálculo de la media en cada callback.

---

# ACTIVIDAD 4 · Pregunta de diseño

Supón que mañana te piden añadir:


```text
D. Mostrar alumnos con media inferior a 5.
E. Mostrar alumnos con media entre 5 y 7.
F. Mostrar solo los nombres.
```


¿Tendrías que modificar `analizarAlumnos()`?

Justifica tu respuesta.

**Objetivo:** comprobar si has separado correctamente la lógica de procesamiento de la lógica de presentación.

---

# TEST · 30 preguntas

## 10 minutos

Marca **una única respuesta correcta**.

Las preguntas están diseñadas para comprobar comprensión y razonamiento, no memorización.

---

# Pregunta 1

¿Qué ocurre?


```js
let i = 0;

while (i < 3) {
    console.log(i);
}
```


A. Imprime `0 1 2`.

B. No imprime nada.

C. Entra en un bucle infinito.

D. Produce un error de sintaxis.

---

# Pregunta 2

¿Qué imprime?


```js
for (let i = 0; i < 5; i++) {
    if (i === 2) continue;
    console.log(i);
}
```


A. `0 1 2 3 4`

B. `0 1 3 4`

C. `0 1`

D. `2 3 4`

---

# Pregunta 3

¿Qué ocurre?


```js
for (let i = 0; i < 5; i++) {
    if (i === 2) break;
    console.log(i);
}
```


A. `0 1`

B. `0 1 3 4`

C. `2`

D. `0 1 2`

---

# Pregunta 4

¿Cuál es la diferencia fundamental entre `break` y `continue` dentro de un bucle?

A. `break` salta una iteración y `continue` termina el bucle.

B. Ambos terminan el bucle.

C. `break` termina el bucle y `continue` pasa a la siguiente iteración.

D. `continue` solo puede utilizarse con `while`.

---

# Pregunta 5

¿Qué imprime?


```js
let i = 0;

do {
    console.log(i);
    i++;
} while (i < 0);
```


A. Nada.

B. `0`.

C. Bucle infinito.

D. Error.

---

# Pregunta 6

¿Cuál de estas situaciones justifica mejor `continue`?

A. Se ha producido una condición que hace imposible seguir procesando el resto de datos.

B. Queremos ignorar el elemento actual pero continuar con los siguientes.

C. Queremos salir de una función.

D. Queremos reiniciar el programa.

---

# Pregunta 7

¿Qué problema aparece?


```js
switch (tipo) {
    case "A":
        console.log("A");

    case "B":
        console.log("B");
        break;
}
```


Si `tipo === "A"`:

A. Solo imprime `A`.

B. Solo imprime `B`.

C. Imprime `A` y `B`.

D. Produce un error.

---

# Pregunta 8

¿Qué ocurre?


```js
switch (1) {
    case "1":
        console.log("uno");
        break;
    case 1:
        console.log("número");
        break;
}
```


A. Imprime `uno`.

B. Imprime `número`.

C. Imprime ambos.

D. No imprime nada porque `switch` no compara tipos.

---

# Pregunta 9

¿Qué problema tiene esta función?


```js
function sumar(a, b) {
    a + b;
}
```


A. `a` y `b` no pueden ser parámetros.

B. Falta `return`.

C. Falta `break`.

D. Una función no puede sumar valores.

---

# Pregunta 10

¿Qué devuelve?


```js
function sumar(a, b) {
    return a + b;
}

const resultado = sumar(2, 3);
```


A. `undefined`

B. `"23"`

C. `5`

D. `true`

---

# Pregunta 11

¿Qué valor recibe `b`?


```js
function calcular(a, b = 10) {
    return a + b;
}

calcular(5);
```


A. `undefined`

B. `0`

C. `5`

D. `10`

---

# Pregunta 12

¿Qué ocurre?


```js
function comprobar(nota) {
    if (nota >= 5) {
        return "aprobado";
    }

    return "suspenso";
}
```


Cuando `nota` vale `8`:

A. Se ejecutan los dos `return`.

B. Solo se ejecuta el primer `return`.

C. Se ejecuta primero el segundo `return`.

D. La función devuelve ambos valores.

---

# Pregunta 13

¿Cuál representa mejor el principio de una función con una única responsabilidad?

A. Una función que valida, calcula, muestra y guarda datos.

B. Una función que hace todo para evitar tener muchas funciones.

C. Una función que realiza una tarea concreta y bien definida.

D. Una función que siempre tiene exactamente una línea.

---

# Pregunta 14

¿Qué devuelve?


```js
function min(a, b) {
    if (a < b) return a;
    return b;
}
```


```js
min(8, 3);
```


A. `8`

B. `3`

C. `false`

D. `undefined`

---

# Pregunta 15

¿Qué sucede?


```js
const doble = function (n) {
    return n * 2;
};

console.log(doble(4));
```


A. `8`

B. `4`

C. `undefined`

D. Error porque una función anónima no puede almacenarse en una variable.

---

# Pregunta 16

¿Qué significa que una función pueda tratarse como un valor?

A. Que solo puede devolver números.

B. Que puede almacenarse en una variable, pasarse como argumento o devolverse desde otra función.

C. Que siempre debe ser una función flecha.

D. Que no necesita parámetros.

---

# Pregunta 17

¿Qué imprime?


```js
function ejecutar(fn) {
    return fn(5);
}

function doble(n) {
    return n * 2;
}

console.log(ejecutar(doble));
```


A. `5`

B. `7`

C. `10`

D. `undefined`

---

# Pregunta 18

En el código anterior, ¿qué papel desempeña `doble` al hacer `ejecutar(doble)`?

A. Es el resultado de ejecutar la función.

B. Es una función que se pasa como argumento.

C. Es una variable global obligatoria.

D. Es un objeto.

---

# Pregunta 19

¿Cuál es equivalente?


```js
function sumar(a, b) {
    return a + b;
}
```


A. 
```js
const sumar = (a, b) => a + b;
```
 B. 
```js
const sumar = (a, b) => { a + b };
```
 | C. 
```js
const sumar = a, b => a + b;
```
 D. 
```js
const sumar = => a + b;
```
 |

---

# Pregunta 20

¿Qué devuelve?


```js
const doble = n => {
    n * 2;
};

doble(5);
```


A. `10`

B. `5`

C. `undefined`

D. Error.

---

# Pregunta 21

¿Qué función flecha es equivalente?


```js
function esAdulto(edad) {
    return edad >= 18;
}
```


A. 
```js
edad => { edad >= 18; }
```
 B. 
```js
edad => edad >= 18
```
 | C. 
```js
(edad) => return edad >= 18
```
 D. 
```js
=> edad >= 18
```
 |

---

# Pregunta 22

¿Qué ventaja aporta este diseño?


```js
function procesar(datos, callback) {
    for (const dato of datos) {
        callback(dato);
    }
}
```


A. Evita completamente los bucles.

B. Permite reutilizar el recorrido cambiando la operación aplicada a cada elemento.

C. Hace que `callback` sea siempre una función flecha.

D. Impide que la función reciba arrays.

---

# Pregunta 23

¿Qué ocurre?


```js
function procesar(callback) {
    callback();
}

function saludar() {
    console.log("Hola");
}

procesar(saludar());
```


A. Se ejecuta `saludar` y después se pasa su resultado a `procesar`.

B. Se pasa la función `saludar` como callback.

C. `saludar()` produce un error de sintaxis.

D. Se ejecuta `procesar` dos veces.

---

# Pregunta 24

¿Cuál sería la llamada correcta de la pregunta anterior si queremos pasar la función sin ejecutarla?

A. 
```js
procesar(saludar());
```
 B. 
```js
procesar(saludar);
```
 | C. 
```js
procesar(() => saludar);
```
 D. 
```js
procesar(return saludar);
```
 |

---

# Pregunta 25

¿Qué problema tiene?


```js
function media(notas) {
    let suma = 0;

    for (let i = 0; i < notas.length; i++) {
        suma += notas[i];
    }

    return suma / notas.length;
}
```


si:


```js
notas = [5, null, 10];
```


A. No hay ningún problema.  B. `null` debe ignorarse si representa una nota ausente. | C. `null` se convierte automáticamente en una nota válida.  D. El bucle no puede recorrer arrays con `null`. |

---

# Pregunta 26

Si `null` representa una ausencia de dato, ¿qué estructura es más adecuada?

A. 
```js
if (nota === null) continue;
```
 B. 
```js
if (nota === null) break;
```
 | C. 
```js
if (nota === null) return nota;
```
 D. 
```js
if (nota === null) nota++;
```
 |

---

# Pregunta 27

¿Qué problema conceptual existe aquí?


```js
function analizar(notas) {
    for (const nota of notas) {
        if (nota < 0 || nota > 10) {
            break;
        }
    }

    return notas.length;
}
```


A. `break` no puede utilizarse en `for...of`.

B. El resultado no informa de cuántos elementos se procesaron realmente antes del `break`.

C. `return` no puede aparecer después de un bucle.

D. `notas.length` siempre provoca un error.

---

# 44. Pregunta 28

Queremos detener el procesamiento cuando aparece una nota inválida, pero ignorar los alumnos sin nota (`null`). ¿Cuál es el orden lógico?

A.


```js
if (nota === null) continue;
if (nota < 0 || nota > 10) break;
```


B.


```js
if (nota < 0 || nota > 10) continue;
if (nota === null) break;
```


C.


```js
if (nota === null) break;
if (nota < 0 || nota > 10) continue;
```


D.


```js
if (nota === null) return;
```


---

# Pregunta 29

¿Cuál diseño es más reutilizable?

A. 
```js
function mostrarAprobados(alumnos) {
    // recorre y calcula todo
    // y además muestra
}
```
 B. 
```js
function analizarAlumnos(alumnos, callback) {
    // calcula resultados
    // callback decide qué mostrar
}
```
 | C. 
```js
function hacerTodo(alumnos) {
    // calcula, filtra, muestra y guarda
}
```
 D. 
```js
function alumnos() {
    // devuelve siempre los mismos datos
}
```
 |

---

# Pregunta 30

Observa:


```js
function procesar(alumnos, callback) {
    for (const alumno of alumnos) {
        const media =
            alumno.notas.reduce((a, b) => a + b, 0)
            / alumno.notas.length;

        callback({
            nombre: alumno.nombre,
            media: media
        });
    }
}
```


¿Qué afirmación describe mejor el diseño?

A. El callback calcula la media.

B. `procesar()` calcula los datos y el callback decide qué hacer con cada resultado.

C. El callback sustituye al bucle.

D. `procesar()` no utiliza funciones como valores.

---


