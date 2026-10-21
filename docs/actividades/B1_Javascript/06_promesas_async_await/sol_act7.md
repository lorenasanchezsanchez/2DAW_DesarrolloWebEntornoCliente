# Solución de Ejercicios Evaluables – Bloque 7
## Síntesis y aplicación práctica de Promesas y Async/Await

### Ejercicio 1 – Teórico de repaso (1 punto)

**Pregunta:** Explica las diferencias principales entre **callbacks**, **promesas** y **async/await**, indicando una ventaja de cada uno.

**Solución:**

| Característica | **Callbacks** | **Promesas** | **Async/Await** |
| :--- | :--- | :--- | :--- |
| **Definición** | Funciones que se pasan como argumentos a otras funciones para ejecutarse al finalizar una tarea. | Objetos nativos que representan el resultado futuro (éxito/fracaso) de una acción asíncrona. | Azúcar sintáctico construido sobre las promesas para escribir código asíncrono con aspecto síncrono. |
| **Gestión de Errores** | Manual mediante la convención *error-first* en cada nivel de anidación. | Centralizada a través del método estructurado `.catch()`. | Estructurada y nativa del lenguaje mediante bloques tradicionales `try...catch`. |
| **Flujo del Código** | Horizontal y piramidal cuando se encadenan varios (*Callback Hell*). | Lineal y vertical mediante el encadenamiento de métodos `.then()`. | Secuencial y síncrono a la vista, eliminando los bloques anidados. |
| **Ventaja principal** | **Simplicidad inicial:** No requieren estructuras complejas ni soporte de versiones modernas de JS. | **Modularidad:** Permiten encadenar y pasar estados de forma limpia sin acoplar funciones. | **Legibilidad máxima:** El código es idéntico al síncrono, facilitando la depuración y mantenimiento. |

---

### Ejercicio 2 – Promesa secuencial (2 puntos)

#### Código en JavaScript:
```javascript
function procesoSecuencial() {
  console.log("Iniciando...");

  // Primer paso con retardo de 1 segundo
  new Promise((resolve) => {
    setTimeout(() => {
      console.log("Procesando...");
      resolve();
    }, 1000);
  })
  // Segundo paso encadenado con otro segundo de retardo
  .then(() => {
    return new Promise((resolve) => {
      setTimeout(() => {
        console.log("Finalizado ✅");
        resolve();
      }, 1000);
    });
  });
}

// Ejecución de la prueba
procesoSecuencial();
```

---

### Ejercicio 3 – Conversión a Async/Await (2 puntos)

#### Código en JavaScript:
```javascript
// Función helper basada en una promesa para pausar la ejecución de forma limpia
const esperar = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function procesoSecuencialAsync() {
  console.log("Iniciando...");
  
  await esperar(1000); // Pausa el flujo 1 segundo
  console.log("Procesando...");
  
  await esperar(1000); // Pausa el flujo otro segundo
  console.log("Finalizado ✅");
}

// Ejecución de la prueba
procesoSecuencialAsync();
```

---

### Ejercicio 4 – Ejecución paralela (2 puntos)

#### Código en JavaScript:
```javascript
async function cargarTodo() {
  // Definición de las tres promesas con tiempos variables
  const p1 = new Promise(res => setTimeout(() => res("Tarea 1 completada"), 1000));
  const p2 = new Promise(res => setTimeout(() => res("Tarea 2 completada"), 2000));
  const p3 = new Promise(res => setTimeout(() => res("Tarea 3 completada"), 3000));

  try {
    // Se ejecutan las tres en paralelo de manera concurrente
    const resultados = await Promise.all([p1, p2, p3]);
    
    // Mostramos los resultados individuales resueltos en el array
    resultados.forEach(mensaje => console.log(mensaje));
    
    console.log("Todas las tareas completadas ✅");
  } catch (error) {
    console.error("Una de las tareas en paralelo falló:", error);
  }
}

// Ejecución de la prueba
cargarTodo();
```

---

### Ejercicio 5 – Proyecto integrador (3 puntos)

#### Código en JavaScript:
```javascript
// Variable global para simular el estado del servidor en las pruebas
let simulacionServidorVacio = false; 

// 1. Implementación de obtenerPedidos()
function obtenerPedidos() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (simulacionServidorVacio) {
        resolve([]); // Devolución vacía para forzar el flujo de error
      } else {
        resolve(["Pedido #001", "Pedido #002", "Pedido #003"]);
      }
    }, 2000);
  });
}

// 2. Implementación de procesarPedidos()
function procesarPedidos(listaPedidos) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (!listaPedidos || listaPedidos.length === 0) {
        reject(new Error("No hay pedidos"));
      } else {
        // Añadimos metadatos de procesamiento a cada pedido
        const pedidosProcesados = listaPedidos.map(p => `${p} [PROCESADO]`);
        resolve(pedidosProcesados);
      }
    }, 2000);
  });
}

// 3. Función síncrona auxiliar mostrarResumen()
function mostrarResumen(listaProcesados) {
  console.log("Resumen del lote:");
  listaProcesados.forEach(p => console.log(` - ${p}`));
}

// --- Función integradora principal proporcionada ---
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

// Ejecución de Pruebas:
// Para probar el caso de éxito, ejecuta directamente:
gestionarPedidos();

// Para probar el caso de error (descomenta las líneas de abajo):
// setTimeout(() => {
//   console.log("\n--- INICIANDO PRUEBA DE ERROR ---");
//   simulacionServidorVacio = true;
//   gestionarPedidos();
// }, 5000);
```
