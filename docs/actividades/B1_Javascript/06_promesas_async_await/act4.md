**Ejercicios evaluables – Bloque 4**

***Métodos estáticos de la clase Promise***

(Promise.all, Promise.allSettled, Promise.race, Promise.any, Promise.resolve, Promise.reject)

**🧠 Ejercicio 1 – Teórico (1 punto)**

**Pregunta:**
Completa la siguiente tabla indicando qué hace cada método:

| **Método** | **Descripción breve** |
| --- | --- |
| Promise.all() | … |
| Promise.allSettled() | … |
| Promise.race() | … |
| Promise.any() | … |

**💻 Ejercicio 2 – Promise.all() (2 puntos)**

Crea tres promesas:

* Una se resuelve en 1 segundo con el valor "A".
* Otra en 2 segundos con el valor "B".
* La tercera falla con "Error C".

Únelas con Promise.all() y observa el resultado.
Luego modifica el código para que el error no interrumpa el resto usando Promise.allSettled().

📘 **Salida esperada (Promise.all):**

Error: Error C

📘 **Salida esperada (Promise.allSettled):**

[

{ status: "fulfilled", value: "A" },

{ status: "fulfilled", value: "B" },

{ status: "rejected", reason: "Error C" }

]

**🧩 Ejercicio 3 – Promise.race() (2 puntos)**

Simula una carrera entre tres promesas:

const p1 = new Promise(resolve => setTimeout(() => resolve("🏁 Promesa 1"), 3000));

const p2 = new Promise(resolve => setTimeout(() => resolve("🏎️ Promesa 2"), 2000));

const p3 = new Promise(resolve => setTimeout(() => resolve("🚀 Promesa 3"), 1000));

Usa Promise.race([p1, p2, p3]) para mostrar cuál termina primero.
Luego modifica el código para que una de ellas falle y observa el efecto.

📘 **Salida esperada:**

🚀 Promesa 3

**⚙️ Ejercicio 4 – Promise.any() (2 puntos)**

Crea tres promesas:

* Dos se rechazan con distintos mensajes de error.
* Una se resuelve con "Servidor activo" tras 1 segundo.

Usa Promise.any() para devolver la primera que se cumpla correctamente.
Después, prueba que si todas fallan, el error resultante es de tipo **AggregateError**.

📘 **Salida esperada:**

Servidor activo

**⚡ Ejercicio 5 – Promise.resolve() y Promise.reject() (3 puntos)**

1️⃣ Usa Promise.resolve() para crear una promesa ya resuelta con el valor "Conexión establecida".
2️⃣ Usa Promise.reject() para crear una promesa rechazada con el mensaje "Error de conexión".
3️⃣ Maneja ambas con .then() y .catch() respectivamente, mostrando los mensajes por consola.

📘 **Salida esperada:**

Conexión establecida

Error de conexión