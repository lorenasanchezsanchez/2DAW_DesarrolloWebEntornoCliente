# Solución de Ejercicios Evaluables – Bloque 3
## Manejo de errores y depuración en Promesas

### Ejercicio 1 – Teórico (1 punto)

**Pregunta:** Explica brevemente qué hace el método `.catch()` y en qué se diferencia del uso del segundo parámetro en `.then()`.

**Solución:**
El método `.catch()` sirve para capturar y manejar de forma centralizada cualquier rechazo (`reject`) o error lanzado (`throw`) que ocurra en cualquier punto previo de la cadena de promesas. 

La diferencia principal con respecto al segundo parámetro de `.then(onFulfilled, onRejected)` radica en el **alcance del control de errores**:
* El segundo parámetro de `.then()` **solo puede capturar errores que provengan del nivel anterior** en la cadena. No puede capturar fallos que ocurran dentro de su propio bloque de éxito (`onFulfilled`).
* El método `.catch()` se coloca al final de la cadena o debajo de los bloques `.then()`, lo que le permite capturar de forma global tanto los errores de las promesas iniciales como los errores sobrevenidos dentro de cualquiera de los métodos `.then()` anteriores.

---

### Ejercicio 2 – Errores dentro de `.then()` (2 puntos)

#### 1️⃣ ¿Qué mostrará la consola?
La consola mostrará secuencialmente los siguientes dos mensajes:
```text
OK
Error capturado: Fallo interno
```

#### 2️⃣ ¿Por qué no se ejecuta un segundo `.then()` tras el error?
Porque cualquier error lanzado con la palabra clave `throw` dentro de un bloque `.then()` altera el flujo del programa. En JavaScript, un `throw` transforma inmediatamente la promesa devuelta por ese `.then()` de estado exitoso (`fulfilled`) a estado rechazado (`rejected`). Como el motor busca resolver la cadena y se encuentra ante un estado de rechazo, salta de largo todos los bloques `.then()` siguientes hasta encontrar el primer manejador de errores `.catch()` disponible.

---

### Ejercicio 3 – Re-lanzamiento de errores (2 puntos)

#### Código en JavaScript:
```javascript
// Creación de la promesa que nace rechazada
Promise.reject("Error inicial")
  .catch(err => {
    console.log("Manejo parcial");
    // Re-lanzamos el error para propagarlo al siguiente catch
    throw err; 
  })
  .catch(err => {
    console.log(`Error final: ${err}`);
  });
```

#### Salida esperada en consola:
```text
Manejo parcial
Error final: Error inicial
```

---

### Ejercicio 4 – Errores no manejados (2 puntos)

#### Código en JavaScript:
```javascript
// Añadimos el escuchador global antes del rechazo
window.addEventListener("unhandledrejection", event => {
  console.error("Promesa no manejada:", event.reason);
});

// Promesa huérfana (sin método .catch adjunto)
new Promise((_, reject) => reject("Error global"));
```

#### Explicación del evento:
El evento `unhandledrejection` es un mecanismo de red de seguridad global provisto por el entorno de ejecución (navegadores o entornos como Node.js) que se dispara cada vez que una promesa es rechazada y **no tiene ningún `.catch()`** asociado para procesar ese fallo.

Es extremadamente útil en producción en los siguientes contextos:
* **Sistemas de Monitorización:** Permite enviar los registros de errores críticos e imprevistos a servidores de analítica (como Sentry o LogRocket) para descubrir fallos en la aplicación que están afectando a los usuarios en tiempo real.
* **Depuración avanzada:** Evita fallos silenciosos en aplicaciones complejas, garantizando que el desarrollador sea consciente de las promesas "olvidadas" que rompen flujos asíncronos secundarios.

---

### Ejercicio 5 – Cadena con varios errores (3 puntos)

#### Código en JavaScript:
```javascript
// Flujo estructurado para la recuperación de errores intermedios
new Promise((resolve) => {
  console.log("Inicio del proceso");
  resolve();
})
  .then(() => {
    // Provocamos un fallo a propósito en el primer paso
    throw new Error("Algo salió mal");
  })
  .catch((err) => {
    // Capturamos el error anterior, lo subsanamos y devolvemos un mensaje de éxito
    return "Recuperado"; 
  })
  .then((datos) => {
    // Como el .catch anterior devolvió un valor limpio, este .then vuelve a ejecutarse
    console.log("Proceso terminado correctamente");
  });
```

#### Salida esperada en consola:
```text
Inicio del proceso
Proceso terminado correctamente
```
