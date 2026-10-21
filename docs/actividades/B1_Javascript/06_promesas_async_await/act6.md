# Solución de Ejercicios Evaluables – Bloque 5
## Promisificación: transformar callbacks en Promesas

### Ejercicio 1 – Teórico (1 punto)

**Pregunta:** Define qué significa *promisificar una función* y explica por qué este proceso es útil al trabajar con código JavaScript moderno.

**Solución:**
**Promisificar** es el proceso de transformar una función clásica basada en callbacks (que acepta una función como argumento para gestionar su resultado) en una función moderna que devuelve un objeto `Promise`.

Este proceso es extremadamente útil en el desarrollo moderno de JavaScript por las siguientes razones:
1. **Sintaxis limpia y lineal:** Permite abandonar las estructuras anidadas del *Callback Hell* en favor de encadenamientos verticales con `.then()` y `.catch()`.
2. **Compatibilidad con Async/Await:** Las promesas son el requisito indispensable para poder utilizar la sintaxis `async/await`, la cual permite escribir código asíncrono con una estructura idéntica a la del código síncrono secuencial.
3. **Control de errores centralizado:** Evita tener que comprobar manualmente el parámetro `error` en cada función, delegando la gestión de fallos a bloques unificados `catch` o estructuras `try...catch`.

---

### Ejercicio 2 – Transformación básica (2 puntos)

#### Código en JavaScript:
```javascript
// Función original basada en callback
function sumar(a, b, callback) {
  setTimeout(() => callback(null, a + b), 1000);
}

// Nueva versión promisificada con validación de parámetros
function sumarPromise(a, b) {
  return new Promise((resolve, reject) => {
    // Validación: Comprobamos si los argumentos son de tipo numérico
    if (typeof a !== 'number' || typeof b !== 'number') {
      reject("Error: parámetros inválidos");
      return; // Detenemos la ejecución
    }

    // Ejecutamos la lógica original adaptando las salidas del callback
    sumar(a, b, (error, resultado) => {
      if (error) {
        reject(error);
      } else {
        resolve(resultado);
      }
    });
  });
}

// Ejemplo de uso exitoso
sumarPromise(4, 6)
  .then(resultado => console.log("Suma:", resultado))
  .catch(error => console.error(error));

// Ejemplo de uso con error de tipos
sumarPromise(4, "seis")
  .then(resultado => console.log("Suma:", resultado))
  .catch(error => console.error(error)); // Imprime: Error: parámetros inválidos
```

---

### Ejercicio 3 – Promisificación genérica (2 puntos)

#### Código en JavaScript:
```javascript
// Función helper para promisificar cualquier función estándar de estilo error-first callback
function promisify(func) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      // Añadimos nuestro callback personalizado al final de los argumentos
      func(...args, (error, resultado) => {
        if (error) {
          reject(error);
        } else {
          resolve(resultado);
        }
      });
    });
  };
}

// Ejemplo de función base
function obtenerMensaje(callback) {
  setTimeout(() => callback(null, "Todo bien 👍"), 1000);
}

// Aplicación del decorador genérico
const obtenerMensajePromise = promisify(obtenerMensaje);

// Ejecución de la nueva función promisificada
obtenerMensajePromise()
  .then(m => console.log(m))
  .catch(e => console.error(e));
```

---

### Ejercicio 4 – Callback múltiple (2 puntos)

#### Código en JavaScript:
```javascript
// Función helper que empaqueta múltiples valores devueltos por un callback en un array
function promisifyMany(func) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      // El callback recibe el error y el resto de parámetros mediante el operador rest (...values)
      func(...args, (error, ...valores) => {
        if (error) {
          reject(error);
        } else {
          // Resolvemos la promesa enviando todos los valores empaquetados
          resolve(valores); 
        }
      });
    });
  };
}

// Función base que devuelve más de un resultado en caso de éxito
function dividir(a, b, callback) {
  if (b === 0) {
    callback(new Error("División por cero"));
  } else {
    callback(null, a / b, "Operación completada");
  }
}

// Transformación
const dividirPromise = promisifyMany(dividir);

// Consumo desestructurando el array de resultados devuelto en el .then()
dividirPromise(10, 2)
  .then(([resultado, mensaje]) => console.log(resultado, mensaje))
  .catch(err => console.error(err.message));
```

#### Salida esperada en consola:
```text
5 Operación completada
```

---

### Ejercicio 5 – Promisificación aplicada (3 puntos)

#### Código en JavaScript:
```javascript
// Función base original del navegador
function loadScript(src, callback) {
  let script = document.createElement('script');
  script.src = src;
  script.onload = () => callback(null, script);
  script.onerror = () => callback(new Error("No se pudo cargar el script"));
  document.head.append(script);
}

// 1️⃣ Creación de la versión basada en Promesas
function loadScriptPromise(src) {
  return new Promise((resolve, reject) => {
    loadScript(src, (error, script) => {
      if (error) {
        reject(error);
      } else {
        resolve(script);
      }
    });
  });
}

// 2️⃣ y 3️⃣ Consumo de la función controlando las salidas solicitadas por consola
loadScriptPromise("https://cloudflare.com")
  .then(script => {
    console.log(`Script cargado: ${script.src}`);
  })
  .catch(error => {
    console.error("Error al cargar script");
  });
```
