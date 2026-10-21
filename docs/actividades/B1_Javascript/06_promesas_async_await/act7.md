**Ejercicios evaluables – Bloque 7**

***Síntesis y aplicación práctica de Promesas y Async/Await***

**🧠 Ejercicio 1 – Teórico de repaso (1 punto)**

**Pregunta:**
Explica las diferencias principales entre **callbacks**, **promesas** y **async/await**, indicando una ventaja de cada uno.

**💻 Ejercicio 2 – Promesa secuencial (2 puntos)**

Crea una función procesoSecuencial() que ejecute tres pasos consecutivos usando promesas encadenadas:

1️⃣ Mostrar "Iniciando..."
2️⃣ Mostrar "Procesando..." (tras 1 segundo)
3️⃣ Mostrar "Finalizado ✅" (tras otro segundo)

Usa setTimeout() dentro de cada paso y encadena los .then() para asegurar el orden.

📘 **Salida esperada:**

Iniciando...

Procesando...

Finalizado ✅

**🧩 Ejercicio 3 – Conversión a Async/Await (2 puntos)**

Reescribe el **Ejercicio 2** usando async/await para lograr el mismo resultado, pero con sintaxis más limpia.
Utiliza una función esperar(ms) basada en una promesa que retarde la ejecución.

**⚙️ Ejercicio 4 – Ejecución paralela (2 puntos)**

Crea una función cargarTodo() que ejecute **tres promesas en paralelo** usando Promise.all() y await.
Cada promesa debe resolverse en un tiempo diferente (1, 2 y 3 segundos) y devolver un mensaje:
"Tarea 1 completada", "Tarea 2 completada", "Tarea 3 completada".

Cuando todas terminen, muestra "Todas las tareas completadas ✅".

**⚡ Ejercicio 5 – Proyecto integrador (3 puntos)**

Crea una función gestionarPedidos() que simule un flujo completo de peticiones asíncronas, combinando todo lo aprendido:

async function gestionarPedidos() {

try {

console.log("Solicitando pedidos...");

const pedidos = await obtenerPedidos(); // Promesa 1

console.log("Procesando pedidos...");

const procesados = await procesarPedidos(pedidos); // Promesa 2

console.log("Mostrando resultados...");

mostrarResumen(procesados); // Función síncrona

} catch (error) {

console.error("Error en la gestión:", error.message);

} finally {

console.log("Gestión finalizada ✅");

}

}

Implementa las funciones obtenerPedidos() y procesarPedidos() como promesas que se resuelvan tras 2 segundos.
Si pedidos está vacío, lanza un error.

📘 **Salida esperada (si todo va bien):**

Solicitando pedidos...

Procesando pedidos...

Mostrando resultados...

Gestión finalizada ✅

📘 **Salida esperada (si hay error):**

Solicitando pedidos...

Error en la gestión: No hay pedidos

Gestión finalizada ✅