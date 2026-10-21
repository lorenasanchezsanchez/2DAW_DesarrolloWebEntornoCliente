**Ejercicios evaluables – Bloque 2**

***Promesas: creación, estados y métodos básicos (then, catch, finally)***

**🧠 Ejercicio 1 – Teórico (1 punto)**

**Pregunta:**
Explica los tres estados por los que puede pasar una promesa en JavaScript e indica qué método se usa para reaccionar cuando:

1. Se cumple con éxito
2. Ocurre un error

**💻 Ejercicio 2 – Práctico (2 puntos)**

Crea una promesa llamada verificarEdad que:

* Espere 2 segundos antes de resolverse.
* Si la variable edad es mayor o igual a 18, se resuelve con el mensaje "Acceso permitido ✅".
* Si es menor, se rechaza con el mensaje "Acceso denegado ❌".

Ejemplo de uso:

let edad = 17;

verificarEdad

.then(msg => console.log(msg))

.catch(err => console.log(err))

.finally(() => console.log("Comprobación terminada"));

📘 **Salida esperada:**

Acceso denegado ❌

Comprobación terminada

**⚙️ Ejercicio 3 – Encadenamiento (2 puntos)**

Crea una promesa que simule un proceso en tres fases:

1. “Iniciando proceso…”
2. “Procesando datos…”
3. “Proceso completado ✅”

Cada fase debe ejecutarse tras 1 segundo, usando **encadenamiento de .then()**.

**🧩 Ejercicio 4 – Análisis de código (2 puntos)**

Analiza el siguiente código y explica **qué mostrará la consola** y **por qué**:

let promesa = new Promise((resolve, reject) => {

resolve("Todo correcto");

reject("Algo falló");

});

promesa

.then(msg => console.log("Éxito:", msg))

.catch(err => console.log("Error:", err));

**⚡ Ejercicio 5 – Error y limpieza (3 puntos)**

Crea una función obtenerUsuario(id) que devuelva una promesa.
Debe:

* Simular una llamada a servidor con setTimeout() (2 segundos).
* Si id es mayor que 0, resolver con "Usuario encontrado 🧍‍♂️".
* Si id es 0 o negativo, rechazar con "ID inválido ❌".
* Mostrar "Operación finalizada" siempre, usando .finally().

Ejemplo de uso:

obtenerUsuario(-1)

.then(msg => console.log(msg))

.catch(err => console.error(err))

.finally(() => console.log("Operación finalizada"));

📘 **Salida esperada:**

ID inválido ❌

Operación finalizada