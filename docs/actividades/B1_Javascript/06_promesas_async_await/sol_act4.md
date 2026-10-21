# Solución de Ejercicios Evaluables – Bloque 4
## Métodos estáticos de la clase Promise

### Ejercicio 1 – Teórico (1 punto)

**Pregunta:** Completa la siguiente tabla indicando qué hace cada método estático de la clase `Promise`.

**Solución:**

| **Método** | **Descripción breve** |
| :--- | :--- |
| `Promise.all()` | Ejecuta un array de promesas en paralelo. Espera a que **todas** se cumplan con éxito. Si **una sola falla**, se cancela inmediatamente todo el grupo y devuelve el error. |
| `Promise.allSettled()` | Ejecuta un array de promesas en paralelo. Espera a que **todas terminen**, sin importar si se cumplen o fallan. Devuelve un array de objetos con el estado (`status`) y el resultado de cada una. |
| `Promise.race()` | Lanza una carrera entre las promesas. Devuelve el resultado de la **primera promesa en terminar** (cambiar de estado), ya sea porque se resolvió con éxito o porque falló. |
| `Promise.any()` | Espera a que la **primera promesa exitosa** se cumpla. Ignora las promesas que fallan a menos que **todas fallen**, en cuyo caso lanza un error de tipo `AggregateError`. |

---

### Ejercicio 2 – Promise.all() y Promise.allSettled() (2 puntos)

#### Código en JavaScript:
```javascript
// Definición de las tres promesas base
const pA = new Promise(resolve => setTimeout(() => resolve("A"), 1000));
const pB = new Promise(resolve => setTimeout(() => resolve("B"), 2000));
const pC = new Promise((_, reject) => reject("Error C"));

// --- PRUEBA 1: Con Promise.all() ---
Promise.all([pA, pB, pC])
  .then(resultados => console.log("Éxito:", resultados))
  .catch(err => console.error("Error:", err)); // Al fallar pC, interrumpe el flujo

// --- PRUEBA 2: Con Promise.allSettled() ---
// Usamos un retraso para que no se pisen las salidas en la consola
setTimeout(() => {
  Promise.allSettled([pA, pB, pC])
    .then(resultados => console.log(resultados));
}, 2500);
```

#### Salida esperada de `Promise.all()`:
```text
Error: Error C
```

#### Salida esperada de `Promise.allSettled()`:
```json
[
  { "status": "fulfilled", "value": "A" },
  { "status": "fulfilled", "value": "B" },
  { "status": "rejected", "reason": "Error C" }
]
```

---

### Ejercicio 3 – Promise.race() (2 puntos)

#### Código en JavaScript:
```javascript
const p1 = new Promise(resolve => setTimeout(() => resolve("🏁 Promesa 1"), 3000));
const p2 = new Promise(resolve => setTimeout(() => resolve("🏎️ Promesa 2"), 2000));
const p3 = new Promise(resolve => setTimeout(() => resolve("🚀 Promesa 3"), 1000));

// Caso 1: Carrera normal, p3 es la más rápida
Promise.race([p1, p2, p3])
  .then(ganadora => console.log(ganadora))
  .catch(err => console.error("Falló la más rápida:", err));

// Caso 2: Modificación donde una de ellas falla de inmediato
const pFalloInmediato = new Promise((_, reject) => reject("💥 Fallo crítico instantáneo"));

Promise.race([p1, p2, pFalloInmediato])
  .then(ganadora => console.log(ganadora))
  .catch(err => console.error("Resultado de la carrera con fallo:", err));
```

#### Salida esperada (Caso 1):
```text
🚀 Promesa 3
```

#### Efecto al añadir la promesa fallida (Caso 2):
La consola mostrará `Resultado de la carrera con fallo: 💥 Fallo crítico instantáneo`. Esto ocurre porque `Promise.race()` no busca la primera promesa *exitosa*, sino la **absolutamente primera en cambiar su estado**. Como `pFalloInmediato` se rechaza de forma instantánea (0 ms), gana la carrera saltando directamente al bloque `.catch()`.

---

### Ejercicio 4 – Promise.any() (2 puntos)

#### Código en JavaScript:
```javascript
const pError1 = new Promise((_, reject) => reject("Fallo en servidor secundario 1"));
const pError2 = new Promise((_, reject) => reject("Fallo en servidor secundario 2"));
const pExito = new Promise(resolve => setTimeout(() => resolve("Servidor activo"), 1000));

// Caso 1: Se obtiene la primera exitosa ignorando los rechazos
Promise.any([pError1, pError2, pExito])
  .then(resultado => console.log(resultado))
  .catch(err => console.error(err));

// Caso 2: Comprobación de AggregateError si todas las promesas fallan
setTimeout(() => {
  Promise.any([pError1, pError2])
    .then(resultado => console.log(resultado))
    .catch(err => {
      console.error("Tipo de error:", err.name); // Imprime: AggregateError
      console.error("Errores individuales:", err.errors); 
    });
}, 1500);
```

#### Salida esperada (Caso 1):
```text
Servidor activo
```

#### Salida esperada (Caso 2 - Fallo total):
```text
Tipo de error: AggregateError
Errores individuales: [ 'Fallo en servidor secundario 1', 'Fallo en servidor secundario 2' ]
```

---

### Ejercicio 5 – Promise.resolve() y Promise.reject() (3 puntos)

#### Código en JavaScript:
```javascript
// 1️⃣ Creación de una promesa ya resuelta de forma síncrona
const promesaExitosa = Promise.resolve("Conexión establecida");

// 2️⃣ Creación de una promesa ya rechazada de forma síncrona
const promesaFallida = Promise.reject("Error de conexión");

// 3️⃣ Manejo y consumo por consola de ambas promesas
promesaExitosa
  .then(msg => console.log(msg));

promesaFallida
  .catch(err => console.error(err));
```

#### Salida esperada en consola:
```text
Conexión establecida
Error de conexión
```
