**Ejercicios evaluables – Bloque 5**

***Promisificación: transformar callbacks en Promesas***

**🧠 Ejercicio 1 – Teórico (1 punto)**

**Pregunta:**
Define qué significa *promisificar una función* y explica por qué este proceso es útil al trabajar con código JavaScript moderno.

**💻 Ejercicio 2 – Transformación básica (2 puntos)**

Convierte la siguiente función basada en callback a una versión que devuelva una Promesa:

function sumar(a, b, callback) {

setTimeout(() => callback(null, a + b), 1000);

}

✅ Requisitos:

* La nueva función debe llamarse sumarPromise.
* Si a o b no son números, debe rechazarse con "Error: parámetros inválidos".
* Si todo va bien, debe resolverse con el resultado.

Ejemplo de uso:

sumarPromise(4, 6)

.then(resultado => console.log("Suma:", resultado))

.catch(error => console.error(error));

**⚙️ Ejercicio 3 – Promisificación genérica (2 puntos)**

Crea una función promisify(func) que reciba cualquier función de estilo callback
(callback(error, resultado)) y devuelva una nueva función que use Promesas.

Ejemplo:

function obtenerMensaje(callback) {

setTimeout(() => callback(null, "Todo bien 👍"), 1000);

}

const obtenerMensajePromise = promisify(obtenerMensaje);

obtenerMensajePromise()

.then(m => console.log(m))

.catch(e => console.error(e));

**🧩 Ejercicio 4 – Callback múltiple (2 puntos)**

Algunas funciones devuelven **más de un resultado**.
Crea una versión promisifyMany(func) que soporte varios valores de salida.

Ejemplo:

function dividir(a, b, callback) {

if (b === 0) callback(new Error("División por cero"));

else callback(null, a / b, "Operación completada");

}

const dividirPromise = promisifyMany(dividir);

dividirPromise(10, 2)

.then(([resultado, mensaje]) => console.log(resultado, mensaje))

.catch(err => console.error(err.message));

📘 **Salida esperada:**

5 Operación completada

**⚡ Ejercicio 5 – Promisificación aplicada (3 puntos)**

Tienes la siguiente función que carga un script usando callbacks:

function loadScript(src, callback) {

let script = document.createElement('script');

script.src = src;

script.onload = () => callback(null, script);

script.onerror = () => callback(new Error("No se pudo cargar el script"));

document.head.append(script);

}

1️⃣ Crea una versión loadScriptPromise(src) basada en Promesas.
2️⃣ Usa la función con .then() y .catch().
3️⃣ Muestra en consola:

* "Script cargado: <nombre>" si todo va bien.
* "Error al cargar script" si falla.
