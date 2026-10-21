## Ejercicios evaluables – Bloque 1

***Callbacks y asincronía***

### Ejercicio 1 – Teórico (1 punto)

**Pregunta:**
Explica con tus propias palabras qué significa que JavaScript sea un lenguaje *monohilo* y cómo consigue ejecutar tareas asíncronas sin bloquear la ejecución del programa.

---

### Ejercicio 2 – Práctico (1 punto)

Escribe un fragmento de código que muestre en consola los mensajes:
* Inicio
* Fin
* Mensaje asíncrono

Debes usar `setTimeout()` para retrasar el mensaje final 2 segundos. Explica brevemente por qué "Fin" aparece antes que "Mensaje asíncrono".

---

### Ejercicio 3 – Callback simple (2 puntos)

Crea una función llamada `operacion` que reciba dos números y una función callback. La función deberá:
1. Sumar los dos números.
2. Llamar al callback pasando el resultado.

#### Ejemplo esperado:
```javascript
operacion(5, 3, resultado => console.log("Resultado:", resultado));
```

#### Salida esperada:
```text
Resultado: 8
```

---

### Ejercicio 4 – Encadenamiento de callbacks (3 puntos)

Crea tres funciones:
```javascript
function paso1(callback) { ... }
function paso2(callback) { ... }
function paso3(callback) { ... }
```

Cada una debe usar `setTimeout()` (1 segundo) y mostrar un mensaje respectivo:
* Paso 1 completado
* Paso 2 completado
* Paso 3 completado

Ejecuta las tres funciones de forma **encadenada** usando callbacks para simular un proceso secuencial.

---

### Ejercicio 5 – Reflexión (3 puntos)

Explica qué problema de arquitectura y legibilidad tiene el siguiente código y cómo lo solucionarías conceptualmente utilizando Promesas:

```javascript
loadScript("1.js", function() {
  loadScript("2.js", function() {
    loadScript("3.js", function() {
      console.log("Todos los scripts cargados");
    });
  });
});
```
