# Solución de Ejercicios Evaluables – Bloque 2
## Promesas: creación, estados y métodos básicos

### Ejercicio 1 – Teórico (1 punto)

**Pregunta:** Explica los tres estados por los que puede pasar una promesa en JavaScript e indica qué método se usa para reaccionar cuando se cumple con éxito o cuando ocurre un error.

**Solución:**
Una promesa en JavaScript se comporta como un objeto asíncrono que actúa como un "marcador de posición" para un valor que aún no se conoce. Puede encontrarse en uno de los siguientes **tres estados**:

1. **`pending` (Pendiente):** Es el estado inicial predeterminado. La operación asíncrona subyacente aún se está ejecutando en segundo plano y la promesa no se ha cumplido ni se ha rechazado.
2. **`fulfilled` (Cumplida):** Significa que la operación asíncrona se completó con éxito y de manera satisfactoria. La promesa ahora posee un valor de resolución inmutable.
3. **`rejected` (Rechazada):** Significa que la operación asíncrona falló debido a un problema o error. La promesa ahora posee una razón o motivo del rechazo (usualmente un objeto de error).

#### Métodos para reaccionar al cambio de estado:
* Para reaccionar cuando la promesa pasa a estado **`fulfilled`** con éxito, se consume utilizando el método **`.then()`**.
* Para reaccionar cuando la promesa pasa a estado **`rejected`** por un error, se consume utilizando el método **`.catch()`**.

---

### Ejercicio 2 – Práctico (2 puntos)

#### Código en JavaScript:
```javascript
// Declaración de la variable para la prueba
let edad = 17;

// Creación de la promesa que depende de la variable externa edad
const verificarEdad = new Promise((resolve, reject) => {
  setTimeout(() => {
    if (edad >= 18) {
      resolve("Acceso permitido ✅");
    } else {
      reject("Acceso denegado ❌");
    }
  }, 2000);
});

// Consumo y ejecución de la promesa
verificarEdad
  .then(msg => console.log(msg))
  .catch(err => console.log(err))
  .finally(() => console.log("Comprobación terminada"));
```

#### Salida obtenida en consola (con edad = 17):
```text
Acceso denegado ❌
Comprobación terminada
```

---

### Ejercicio 3 – Encadenamiento (2 puntos)

#### Código en JavaScript:
```javascript
// Función auxiliar para generar retardos estructurados en el encadenamiento
function retrasarMensaje(mensaje, tiempo) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(mensaje);
      resolve();
    }, tiempo);
  });
}

// Ejecución secuencial mediante encadenamiento lineal de .then()
retrasarMensaje("Iniciando proceso...", 1000)
  .then(() => retrasarMensaje("Procesando datos...", 1000))
  .then(() => retrasarMensaje("Proceso completado ✅", 1000));
```

---

### Ejercicio 4 – Análisis de código (2 puntos)

#### Código analizado:
```javascript
let promesa = new Promise((resolve, reject) => {
  resolve("Todo correcto");
  reject("Algo falló");
});

promesa
  .then(msg => console.log("Éxito:", msg))
  .catch(err => console.log("Error:", err));
```

#### Qué mostrará la consola:
```text
Éxito: Todo correcto
```

#### Por qué ocurre:
La consola mostrará únicamente el bloque de éxito porque **las promesas son inmutables una vez que cambian de estado**. El ciclo de vida de una promesa dicta que esta solo puede resolverse o rechazarse **una sola vez**. 

En la función ejecutora, la instrucción `resolve("Todo correcto")` se ejecuta primero, lo que transiciona inmediatamente el estado de la promesa de `pending` a `fulfilled`. Una vez que la promesa está resuelta con éxito, cualquier llamada posterior a `reject()` o a otro `resolve()` dentro del mismo bloque se ignora por completo de manera silenciosa.

---

### Ejercicio 5 – Error y limpieza (3 puntos)

#### Código en JavaScript:
```javascript
// Definición de la función constructora de la promesa
function obtenerUsuario(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id > 0) {
        resolve("Usuario encontrado 🧍‍♂️");
      } else {
        reject("ID inválido ❌");
      }
    }, 2000);
  });
}

// Ejecución de prueba pasando un ID negativo (-1)
obtenerUsuario(-1)
  .then(msg => console.log(msg))
  .catch(err => console.error(err))
  .finally(() => console.log("Operación finalizada"));
```

#### Salida obtenida en consola:
```text
ID inválido ❌
Operación finalizada
```
