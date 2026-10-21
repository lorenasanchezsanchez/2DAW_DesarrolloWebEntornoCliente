# Solución de Ejercicios Evaluables – Bloque 6
## Sintaxis moderna: Async/Await y flujos asíncronos

### Ejercicio 1 – Teórico (1 punto)

**Pregunta:** Explica la relación que existe entre las Promesas y la sintaxis `async/await`. ¿Por qué se dice que `async/await` es "azúcar sintáctico"?

**Solución:**
La sintaxis `async/await` no es un sistema nuevo ni independiente de gestión de asincronía, sino que **está construida directamente encima de las Promesas**. Su relación es absoluta:
* Cualquier función declarada con la palabra clave `async` devuelve automáticamente una Promesa (si devuelves un valor plano, este se empaqueta en una promesa resuelta).
* La palabra clave `await` solo puede utilizarse dentro de funciones `async` y sirve para pausar de manera lógica la ejecución del código hasta que una Promesa se resuelva (`fulfilled`) o se rechace (`rejected`).

Se le denomina **azúcar sintáctico** porque no añade ninguna funcionalidad nueva al motor de JavaScript. Simplemente ofrece una forma de escribir y leer el código mucho más limpia, humana y secuencial, simulando un comportamiento síncrono que evita el encadenamiento infinito de métodos `.then()` y `.catch()`.

---

### Ejercicio 2 – Transformación básica a Async (2 puntos)

**Pregunta:** Transforma una función de consumo de datos con encadenamiento tradicional (`.then`) a una función moderna utilizando `async/await`.

#### Código original (.then):
```javascript
function mostrarDatos() {
  sumarPromise(5, 5)
    .then(resultado => console.log("Resultado:", resultado))
    .catch(error => console.error(error));
}
```

#### Solución con Async/Await:
```javascript
// Añadimos la palabra clave async a la función
async function mostrarDatosAsync() {
  try {
    // Usamos await para capturar el valor de la resolución directamente en una variable
    const resultado = await sumarPromise(5, 5);
    console.log("Resultado Async:", resultado);
  } catch (error) {
    // Los rechazos de la promesa saltan directamente al bloque catch
    console.error("Error capturado en Async:", error);
  }
}

// Ejecución
mostrarDatosAsync();
```

---

### Ejercicio 3 – Gestión de errores estructurada con Try/Catch (2 puntos)

**Pregunta:** Crea una función que intente autenticar a un usuario mediante una promesa y gestione tanto el éxito como el fallo utilizando bloques `try...catch...finally`.

#### Código en JavaScript:
```javascript
// Promesa base simulada
function solicitarToken(usuario) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (usuario === "admin") resolve("Token_Seguro_123");
      else reject(new Error("Usuario no registrado"));
    }, 1000);
  });
}

// Función asíncrona de gestión
async function autenticarSistema(nombreUsuario) {
  console.log("Iniciando conexión con el servidor...");
  try {
    const token = await solicitarToken(nombreUsuario);
    console.log(`✅ Autenticación exitosa. Su token es: ${token}`);
  } catch (error) {
    console.error(`❌ Error en el proceso: ${error.message}`);
  } finally {
    console.log("🧹 Conexión cerrada. Operación finalizada.");
  }
}

// Prueba con error
autenticarSistema("invitado");
```

---

### Ejercicio 4 – Ejecución en paralelo con Async/Await (2 puntos)

**Pregunta:** Si necesitas llamar a tres endpoints independientes que tardan 2 segundos cada uno, ¿cómo evitarías que la función tarde 6 segundos en total utilizando `Promise.all` junto con `async/await`?

#### Código en JavaScript (Optimizado para ejecución paralela):
```javascript
// Funciones que simulan peticiones asíncronas lentas
const consultarBaseDatos = () => new Promise(res => setTimeout(() => res("Datos de DB"), 2000));
const consultarAPI = () => new Promise(res => setTimeout(() => res("Datos de API"), 2000));
const consultarCache = () => new Promise(res => setTimeout(() => res("Datos de Caché"), 2000));

async function realizarConsultasParalelas() {
  const tiempoInicio = performance.now();

  try {
    // INCORRECTO (Secuencial - tardaría 6s):
    // const db = await consultarBaseDatos();
    // const api = await consultarAPI();
    // const cache = await consultarCache();

    // CORRECTO (Paralelo - tarda solo 2s en total):
    const [db, api, cache] = await Promise.all([
      consultarBaseDatos(),
      consultarAPI(),
      consultarCache()
    ]);

    console.log("Resultados obtenidos:", { db, api, cache });
  } catch (error) {
    console.error("Una de las consultas falló:", error);
  }

  const tiempoFin = performance.now();
  console.log(`Tiempo total de ejecución: ${((tiempoFin - tiempoInicio) / 1000).toFixed(2)} segundos`);
}

realizarConsultasParalelas();
```

---

### Ejercicio 5 – Bucles e iteraciones asíncronas (3 puntos)

**Pregunta:** Crea un flujo que recorra un array de identificadores de productos y mande una petición asíncrona para cada uno, asegurando que se procesen **en estricto orden secuencial** (uno detrás de otro).

#### Código en JavaScript:
```javascript
// Simulación de una petición de red por ID de producto
function procesarProducto(id) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(`Producto #${id} procesado con éxito en inventario.`);
    }, 1000);
  });
}

// Array de prueba
const loteProductos =;

// Función de procesamiento secuencial ordenado
async function procesarLoteSecuencial(productos) {
  console.log("--- Iniciando procesamiento de lote por orden ---");
  
  // El bucle for...of respeta de forma nativa el operador await en cada iteración
  for (const id of productos) {
    const resultado = await procesarProducto(id);
    console.log(resultado);
  }
  
  console.log("--- ¡Lote completo completado! ---");
}

procesarLoteSecuencial(loteProductos);
```

