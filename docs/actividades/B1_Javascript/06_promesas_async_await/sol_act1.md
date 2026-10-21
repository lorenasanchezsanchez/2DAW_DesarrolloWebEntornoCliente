# Solución de Ejercicios Evaluables – Bloque 1
## Callbacks y asincronía

### Ejercicio 1 – Teórico (1 punto)

**Pregunta:** Explica con tus propias palabras qué significa que JavaScript sea un lenguaje *monohilo* y cómo consigue ejecutar tareas asíncronas sin bloquear la ejecución del programa.

**Solución:**
Que JavaScript sea **monohilo** significa que tiene un único hilo de ejecución y un solo montón de memoria (*Call Stack*). Por lo tanto, solo puede procesar **una única instrucción o tarea a la vez** de forma secuencial. 

Para evitar bloquear la interfaz del navegador con tareas pesadas (como peticiones HTTP o temporizadores), JavaScript delega estas operaciones al **entorno de ejecución (las Web APIs del navegador o la API de Node.js)**. El mecanismo clave es el **Event Loop (bucle de eventos)**:
1. Cuando se detecta una tarea asíncrona, se saca del hilo principal y se envía a las Web APIs.
2. Mientras la Web API procesa la tarea en segundo plano, el hilo principal de JavaScript sigue ejecutando el resto del código sin detenerse.
3. Cuando la tarea asíncrona termina, su función asociada (*callback*) se envía a una cola de espera (*Callback Queue*).
4. El *Event Loop* monitoriza constantemente el hilo principal. En el momento en que la pila de ejecución principal se queda completamente vacía, recoge el *callback* de la cola y lo introduce en el hilo para ejecutarlo.

---

### Ejercicio 2 – Práctico (1 punto)

#### Código en JavaScript:
```javascript
console.log("Inicio");

setTimeout(() => {
  console.log("Mensaje asíncrono");
}, 2000);

console.log("Fin");
```

#### Explicación:
El mensaje `"Fin"` aparece antes que `"Mensaje asíncrono"` debido al comportamiento asíncrono de `setTimeout()`. Aunque se encuentra en medio del flujo de lectura, JavaScript no espera a que pasen los 2 segundos de forma síncrona. En su lugar, registra la petición en las Web APIs del navegador e inmediatamente continúa con la siguiente línea ejecutable de la pila (`console.log("Fin")`). 

Solo cuando la pila principal se vacía y el temporizador expira tras 2000ms, el *Event Loop* introduce la función del `setTimeout` en el hilo de ejecución para imprimir `"Mensaje asíncrono"`.

---

### Ejercicio 3 – Callback simple (2 puntos)

#### Código en JavaScript:
```javascript
// Definición de la función con el callback
function operacion(num1, num2, callback) {
  const suma = num1 + num2;
  callback(suma);
}

// Ejecución de la función
operacion(5, 3, resultado => {
  console.log("Resultado:", resultado);
});
```

---

### Ejercicio 4 – Encadenamiento de callbacks (3 puntos)

#### Código en JavaScript:
```javascript
function paso1(callback) {
  setTimeout(() => {
    console.log("Paso 1 completado");
    callback();
  }, 1000);
}

function paso2(callback) {
  setTimeout(() => {
    console.log("Paso 2 completado");
    callback();
  }, 1000);
}

function paso3(callback) {
  setTimeout(() => {
    console.log("Paso 3 completado");
    callback();
  }, 1000);
}

// Ejecución secuencial encadenando los callbacks
paso1(() => {
  paso2(() => {
    paso3(() => {
      console.log("Todos los pasos se han ejecutado en orden.");
    });
  });
});
```

---

### Ejercicio 5 – Reflexión (3 puntos)

**Pregunta:** Explica qué problema de arquitectura y legibilidad tiene el código proporcionado y cómo lo solucionarías conceptualmente utilizando Promesas.

#### Diagnóstico del problema:
El código sufre de un problema de diseño conocido como **Callback Hell** (infierno de callbacks) o *Pirámide del Destino*. Al depender la ejecución de cada script del éxito del anterior, las funciones se anidan una dentro de otra de forma indefinida. 

Esto provoca tres grandes fallos arquitectónicos:
1. **Pésima legibilidad y mantenimiento:** El código crece horizontalmente hacia la derecha de la pantalla, volviéndose extremadamente difícil de seguir.
2. **Manejo de errores complejo:** Si quisiéramos capturar un fallo de carga, tendríamos que añadir lógica de control de errores de forma manual e individual en cada uno de los niveles de anidación.
3. **Rigidez:** Modificar el orden de los pasos o reutilizar las funciones es una tarea propensa a fallos.

#### Solución conceptual con Promesas:
Las promesas solucionan este problema transformando la estructura piramidal horizontal en una estructura lineal vertical mucho más limpia mediante el **encadenamiento de métodos `.then()`**, devolviendo una nueva promesa en cada paso:

```javascript
// Solución conceptual usando Promesas con encadenamiento limpio (.then)
loadScript("1.js")
  .then(() => loadScript("2.js"))
  .then(() => loadScript("3.js"))
  .then(() => {
    console.log("Todos los scripts cargados de manera secuencial y limpia");
  })
  .catch(error => {
    // Un solo punto centralizado para capturar CUALQUIER error en la cadena
    console.error("Error al cargar uno de los scripts:", error);
  });
```
