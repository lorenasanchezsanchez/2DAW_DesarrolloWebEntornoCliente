**Ejercicios evaluables – Bloque 3**

***Manejo de errores y depuración en Promesas***

**🧠 Ejercicio 1 – Teórico (1 punto)**

**Pregunta:**
Explica brevemente qué hace el método .catch() y en qué se diferencia del uso del segundo parámetro en .then().

**💻 Ejercicio 2 – Errores dentro de .then() (2 puntos)**

Analiza el siguiente código y responde:

new Promise(resolve => resolve("OK"))

.then(valor => {

console.log(valor);

throw new Error("Fallo interno");

})

.catch(err => console.error("Error capturado:", err.message));

1️⃣ ¿Qué mostrará la consola?
2️⃣ ¿Por qué no se ejecuta un segundo .then() tras el error?

**🧩 Ejercicio 3 – Re-lanzamiento de errores (2 puntos)**

Crea una promesa que:

1. Se rechace con el mensaje "Error inicial".
2. En el primer .catch(), muestre "Manejo parcial" y vuelva a lanzar el error.
3. En un segundo .catch(), muestre "Error final".

📘 **Salida esperada:**

Manejo parcial

Error final: Error inicial

**⚙️ Ejercicio 4 – Errores no manejados (2 puntos)**

Crea una promesa que se rechace sin .catch() y luego agrega un manejador global:

new Promise((\_, reject) => reject("Error global"));

window.addEventListener("unhandledrejection", event => {

console.error("Promesa no manejada:", event.reason);

});

Explica para qué sirve este evento y en qué contextos es útil.

**⚡ Ejercicio 5 – Cadena con varios errores (3 puntos)**

Crea una promesa que:

* Muestre "Inicio del proceso".
* En el primer .then() genere un error con throw.
* En el .catch() lo maneje y devuelva "Recuperado".
* En un segundo .then() muestre "Proceso terminado correctamente".

📘 **Salida esperada:**

Inicio del proceso

Proceso terminado correctamente