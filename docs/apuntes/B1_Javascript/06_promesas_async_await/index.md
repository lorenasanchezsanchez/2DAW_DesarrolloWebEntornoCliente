## Promesas y Async/Await



### 1. Introducción a la programación asíncrona

JavaScript es un lenguaje de programación monohilo, lo que significa que ejecuta una sola tarea a la vez. Sin embargo, muchas operaciones —como la carga de un archivo, una consulta a una API o la espera de una respuesta del servidor— tardan tiempo, y no podemos permitir que el navegador se quede bloqueado mientras tanto.

Para resolver esto, JavaScript utiliza operaciones asíncronas, que permiten que una tarea se inicie ahora y se complete más adelante, sin detener el flujo principal del programa.

#### Ejemplos comunes de acciones asíncronas

* Cargar una imagen o script externo.
* Esperar una respuesta de una API (petición HTTP).
* Temporizadores (`setTimeout`, `setInterval`).
* Eventos del usuario (clics, teclas, movimientos del ratón).

Todas ellas se gestionan de forma asíncrona mediante un sistema interno conocido como el *event loop*.

#### Ejemplo básico con `setTimeout`

```javascript
console.log("Inicio");
setTimeout(() => console.log("Mensaje retrasado"), 2000);
console.log("Fin");
```

#### Salida:
```text
Inicio
Fin
Mensaje retrasado
```

Aunque el `setTimeout` está en el medio del código, se ejecuta al final, porque se programa para más adelante. Este comportamiento es lo que llamamos asincronía.

---

### 2. Callbacks: la primera solución

Antes de las promesas y async/await, JavaScript usaba *callbacks* para manejar tareas asíncronas. Un callback es simplemente una función que se pasa como argumento a otra función, para que se ejecute cuando la tarea haya terminado.

#### Ejemplo con callback

```javascript
function loadScript(src, callback) {
  let script = document.createElement('script');
  script.src = src;
  script.onload = () => callback(null, script);
  script.onerror = () => callback(new Error("Error al cargar"));
  document.head.append(script);
}

loadScript("script1.js", function(err, script) {
  if (err) console.error(err);
  else console.log("Script cargado:", script.src);
});
```

* **Ventaja:** Podemos ejecutar algo cuando el script termina de cargarse.
* **Desventaja:** Si queremos cargar varios scripts o hacer varias tareas en orden, el código se vuelve un desastre.

#### El "infierno de callbacks" (Callback Hell)

Cuando las tareas se encadenan una dentro de otra, el código empieza a crecer hacia la derecha, dificultando su lectura y mantenimiento.

```javascript
loadScript("1.js", function() {
  loadScript("2.js", function() {
    loadScript("3.js", function() {
      console.log("Todos los scripts cargados");
    });
  });
});
```

Este estilo es lo que se conoce como *callback hell* o pirámide infernal. Cada nueva operación depende de la anterior, lo que hace el código largo, confuso y difícil de depurar.

#### Ejemplo con manejo de errores

En las funciones basadas en callback, se utiliza una convención llamada *error-first*, donde el primer parámetro es el error (si lo hay), y el segundo es el resultado:

```javascript
function operacionAsincrona(callback) {
  let exito = Math.random() > 0.5;
  if (exito) callback(null, "Operación correcta");
  else callback(new Error("Algo falló"));
}

operacionAsincrona((err, resultado) => {
  if (err) console.error("Error:", err.message);
  else console.log(resultado);
});
```

Este sistema funciona, pero no escala bien cuando hay muchas operaciones encadenadas o múltiples niveles de dependencia.

#### Resumen del problema

| Problema | Consecuencia |
| :--- | :--- |
| Múltiples callbacks anidados | Código ilegible |
| Manejo manual de errores | Difícil de mantener |
| Pérdida de contexto | Variables y flujo complicados |
| Poca reutilización | Callbacks específicos por tarea |

**Conclusión:** Los callbacks fueron el primer intento de manejar la asincronía, pero a medida que las aplicaciones crecieron, se hicieron insuficientes. De ahí nacen las Promesas, un nuevo modelo más limpio y potente para gestionar el código asíncrono.

---

## Bloque 2 – Promesas: el nuevo modelo de asincronía

### 1. Qué es una Promesa

Una Promesa es un objeto especial de JavaScript que representa el resultado futuro de una operación asíncrona. Podemos imaginarla como un contrato: el programa promete que en algún momento habrá un resultado (éxito o error).

Cada promesa tiene tres estados posibles:

| Estado | Significado |
| :--- | :--- |
| `pending` | La operación sigue en curso (pendiente). |
| `fulfilled` | La operación terminó correctamente. |
| `rejected` | La operación falló y devolvió un error. |

Cuando una promesa cambia de `pending` a cualquiera de los otros dos, queda "resuelta" y ya no puede volver atrás.

### 2. Creación de una Promesa

La sintaxis básica usa el constructor `Promise`, que recibe una función ejecutora con dos parámetros:

```javascript
let promesa = new Promise((resolve, reject) => {
  // 1. Ejecutamos alguna tarea que tarda tiempo
  setTimeout(() => {
    let exito = true;
    if (exito) resolve("¡Operación completada!");
    else reject("Ha ocurrido un error");
  }, 1000);
});
```

La función ejecutora se ejecuta inmediatamente al crear la promesa.
* Si la tarea sale bien, se llama a `resolve(valor)`.
* Si algo falla, se llama a `reject(error)`.

### 3. Consumidores: `.then()` y `.catch()`

Para reaccionar al resultado de una promesa, usamos sus métodos principales:

| Método | Cuándo se ejecuta |
| :--- | :--- |
| `.then(función)` | Cuando la promesa se cumple correctamente. |
| `.catch(función)` | Cuando la promesa falla o se rechaza. |

```javascript
promesa
  .then(resultado => console.log("Resultado:", resultado))
  .catch(error => console.error("Error:", error));
```

El método `.then()` recibe el valor pasado a `resolve()`. Si la promesa falla, el control pasa al `.catch()`.

### 4. Ejemplo práctico

```javascript
function comprobarUsuario(nombre) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (nombre === "Sergio") resolve("Acceso concedido");
      else reject("Usuario no autorizado");
    }, 1500);
  });
}

comprobarUsuario("Sergio")
  .then(msg => console.log(msg))
  .catch(err => console.error(err));
```

#### Salida:
```text
Acceso concedido
```
Si cambiamos el nombre por otro valor, el flujo saltará al `.catch()`:
```text
Usuario no autorizado
```

### 5. El método `.finally()`

Al igual que en un bloque `try...catch...finally`, este método se ejecuta siempre, haya éxito o error. Sirve para liberar recursos, ocultar indicadores de carga, etc.

```javascript
comprobarUsuario("Alex")
  .then(msg => console.log(msg))
  .catch(err => console.error(err))
  .finally(() => console.log("Operación completada"));
```

#### Salida:
```text
Usuario no autorizado
Operación completada
```

`.finally()` no recibe el resultado ni el error; su función es limpiar o cerrar procesos.

### 6. Encadenamiento de promesas

Podemos encadenar varios `.then()`, pasando el resultado de uno al siguiente.

```javascript
new Promise(resolve => setTimeout(() => resolve(2), 1000))
  .then(num => num * 2)   // devuelve 4
  .then(num => num + 3)   // devuelve 7
  .then(num => console.log("Resultado final:", num));
```

#### Salida:
```text
Resultado final: 7
```

Cada `.then()` devuelve una nueva promesa, lo que permite construir flujos ordenados y fáciles de seguir.

**Resumen del bloque:** Las promesas sustituyen a los callbacks ofreciendo un sistema claro, encadenable y con manejo de errores integrado. `.then()` procesa los éxitos, `.catch()` los fallos y `.finally()` siempre limpia al final.

---

## Bloque 3 – Manejo de errores en Promesas

Las promesas permiten gestionar los errores de forma limpia y controlada, sin tener que anidar múltiples callbacks. Todo error o rechazo dentro de una promesa puede capturarse y tratarse fácilmente con `.catch()`.

### 1. El método `.catch()`

El método `.catch()` se ejecuta cuando una promesa es rechazada o cuando ocurre un error dentro de un `.then()`.

```javascript
fetch("https://inventada123.com")
  .then(response => response.json())  // Esto lanzará un error si la URL no existe
  .catch(error => console.error("Error al obtener datos:", error));
```

El `.catch()` no necesita estar inmediatamente después del `.then()`; JavaScript recorrerá toda la cadena hasta encontrarlo.

### 2. Errores dentro de `.then()`

Si un error ocurre dentro de un `.then()`, se interpreta como un rechazo y se envía automáticamente al `.catch()` más cercano.

```javascript
new Promise((resolve) => resolve("OK"))
  .then(() => {
    throw new Error("Algo falló dentro del then");
  })
  .catch(err => console.error("Error capturado:", err.message));
```
