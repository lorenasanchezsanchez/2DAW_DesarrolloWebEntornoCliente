---
marp: true
theme: default
paginate: true
footer: "UF1 · Promesas y Async/Await | 2.º DAW"
style: |
  section {
    font-family: "Aptos", "Arial", sans-serif;
    font-size: 25px;
    padding: 48px;
  }
  h1 { color: #315b78; }
  h2 { color: #397a8c; }
  h3 { color: #6b7280; }
  pre { font-size: 0.72em; }
  code { font-size: 0.9em; }
  table { font-size: 0.78em; }
---

<!-- _class: lead -->
## UF1. Promesas y Async/Await



---

### Índice


1. Introducción a la programación asíncrona
2. Callbacks: la primera solución
3. Promesas: estados, creación y encadenamiento
4. Manejo de errores en promesas
5. API avanzada de Promise
6. Promisificación
7. Async/Await
8. Resumen y buenas prácticas

---

# 1. Introducción a la programación asíncrona

JavaScript es un lenguaje **monohilo**: ejecuta una tarea a la vez en el hilo principal.

Sin embargo, muchas operaciones tardan tiempo:

- Cargar un archivo o un script externo.
- Consultar una API mediante HTTP.
- Esperar una respuesta del servidor.
- Ejecutar temporizadores (`setTimeout`, `setInterval`).
- Responder a eventos del usuario: clics, teclas o movimientos del ratón.

La asincronía permite iniciar una tarea y continuar ejecutando el programa mientras llega su resultado.

---

## ¿Qué es el *event loop*?

El **event loop** coordina la ejecución del código, las tareas pendientes y las operaciones asíncronas.

La idea fundamental es que una operación que tarda no tiene por qué bloquear todo el programa mientras se espera su resultado.

> JavaScript no ejecuta dos instrucciones del hilo principal exactamente a la vez; organiza cuándo se atienden las tareas pendientes.

---

### Ejemplo: `setTimeout()`

```js
console.log("Inicio");

setTimeout(() => {
  console.log("Mensaje retrasado");
}, 2000);

console.log("Fin");
```

**Salida:**

```text
Inicio
Fin
Mensaje retrasado
```

Aunque `setTimeout()` aparece en medio del código, programa el mensaje para más adelante. Por eso se muestra después de `"Fin"`.

---

# 2. Callbacks: la primera solución

Un **callback** es una función que se pasa como argumento a otra función para que se ejecute cuando ocurra algo o termine una operación.

Antes de las promesas y `async/await`, los callbacks eran una forma habitual de gestionar operaciones asíncronas.

---

### Ejemplo: cargar un script con callback

```js
function loadScript(src, callback) {
  const script = document.createElement("script");
  script.src = src;

  script.onload = () => callback(null, script);
  script.onerror = () => callback(new Error("Error al cargar"));

  document.head.append(script);
}

loadScript("script1.js", (err, script) => {
  if (err) {
    console.error(err);
  } else {
    console.log("Script cargado:", script.src);
  }
});
```

- `onload` indica que el script se ha cargado.
- `onerror` indica que ha ocurrido un error.
- El callback recibe el error o el resultado.

---

## Ventajas y desventajas de los callbacks

**Ventaja**
- Permiten ejecutar una función cuando termina una operación.

**Desventajas**
- El manejo de errores puede quedar repartido.
- Encadenar operaciones dependientes puede complicar el código.
- El código puede crecer hacia la derecha y resultar difícil de leer.

---

## *Callback hell* o pirámide infernal

Cuando cada operación depende de la anterior, los callbacks pueden anidarse:

```js
loadScript("1.js", () => {
  loadScript("2.js", () => {
    loadScript("3.js", () => {
      console.log("Todos los scripts cargados");
    });
  });
});
```

Este patrón se conoce como **callback hell**. A medida que se añaden tareas, el código se vuelve más difícil de mantener y depurar.

---

## Callbacks y manejo de errores

Es frecuente utilizar la convención **error-first**: el primer parámetro representa el error y el segundo, el resultado.

```js
function operacionAsincrona(callback) {
  const exito = Math.random() > 0.5;

  if (exito) {
    callback(null, "Operación correcta");
  } else {
    callback(new Error("Algo falló"));
  }
}

operacionAsincrona((err, resultado) => {
  if (err) {
    console.error("Error:", err.message);
  } else {
    console.log(resultado);
  }
});
```

---

## Problemas del modelo basado en callbacks

| Problema | Consecuencia |
|---|---|
| Muchos callbacks anidados | Código difícil de leer |
| Manejo manual de errores | Mantenimiento más complejo |
| Flujo de ejecución repartido | Cuesta seguir el orden |
| Callbacks específicos por tarea | Menor reutilización |

**Conclusión:** los callbacks funcionan, pero las promesas ofrecen una forma más uniforme de representar el resultado futuro de una operación.

---

# 3. Promesas: el nuevo modelo de asincronía

## ¿Qué es una promesa?

Una **Promise** es un objeto de JavaScript que representa el resultado futuro de una operación asíncrona.

Puede imaginarse como un contrato: la operación terminará correctamente o fallará, y el programa podrá reaccionar a ese resultado.

---

## Los tres estados de una promesa

| Estado | Significado |
|---|---|
| `pending` | La operación sigue pendiente. |
| `fulfilled` | La operación ha terminado correctamente. |
| `rejected` | La operación ha fallado. |

Una promesa pendiente pasa a cumplida o rechazada. Una vez establecida, no vuelve a `pending` ni cambia al estado opuesto.

---

## Crear una promesa

El constructor `Promise` recibe una función ejecutora con dos funciones:

- `resolve(valor)`: indica que la operación se ha completado correctamente.
- `reject(error)`: indica que la operación ha fallado.

```js
const promesa = new Promise((resolve, reject) => {
  setTimeout(() => {
    const exito = true;

    if (exito) {
      resolve("¡Operación completada!");
    } else {
      reject(new Error("Ha ocurrido un error"));
    }
  }, 1000);
});
```

La función ejecutora se ejecuta inmediatamente al crear la promesa.

---

## Consumir una promesa: `.then()` y `.catch()`

- `.then()` permite procesar el valor de una promesa cumplida.
- `.catch()` permite gestionar un rechazo o un error producido en la cadena.

```js
promesa
  .then(resultado => {
    console.log("Resultado:", resultado);
  })
  .catch(error => {
    console.error("Error:", error);
  });
```

El valor que recibe el callback de `.then()` es el que se pasa a `resolve()`.

---

### Ejemplo práctico: comprobar un usuario

```js
function comprobarUsuario(nombre) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (nombre === "Sergio") {
        resolve("Acceso concedido");
      } else {
        reject(new Error("Usuario no autorizado"));
      }
    }, 1500);
  });
}

comprobarUsuario("Sergio")
  .then(mensaje => console.log(mensaje))
  .catch(error => console.error(error.message));
```

Si se llama a `comprobarUsuario("Alex")`, la promesa se rechaza y se ejecuta el `.catch()`.

---

## El método `.finally()`

`.finally()` se ejecuta tanto si la promesa se cumple como si se rechaza.

Es útil para realizar tareas de limpieza: ocultar un indicador de carga, cerrar un recurso o mostrar que el proceso ha terminado.

```js
comprobarUsuario("Alex")
  .then(mensaje => console.log(mensaje))
  .catch(error => console.error(error.message))
  .finally(() => console.log("Operación completada"));
```

**Importante:** la función de `.finally()` no recibe directamente el resultado ni el error. Su finalidad es ejecutar acciones finales.

---

## Encadenamiento de promesas

Cada `.then()` devuelve una nueva promesa. El valor devuelto por un `.then()` se pasa al siguiente.

```js
new Promise(resolve => {
  setTimeout(() => resolve(2), 1000);
})
  .then(numero => numero * 2)   // 4
  .then(numero => numero + 3)   // 7
  .then(resultado => {
    console.log("Resultado final:", resultado);
  });
```

**Salida:**

```text
Resultado final: 7
```

Encadenar en vertical suele ser más legible que anidar callbacks.

---

## Resumen: promesas

- Representan el resultado futuro de una operación.
- `resolve()` cumple la promesa.
- `reject()` la rechaza.
- `.then()` procesa el resultado correcto.
- `.catch()` gestiona los errores.
- `.finally()` ejecuta tareas finales.
- Los `.then()` pueden encadenarse para transformar y pasar resultados.

---

# 4. Manejo de errores en promesas

## El método `.catch()`

`.catch()` se ejecuta cuando una promesa se rechaza o cuando se produce un error en un paso anterior de la cadena.

```js
fetch("https://api.inventada123.com/datos")
  .then(response => response.json())
  .catch(error => {
    console.error("Error al obtener datos:", error);
  });
```

El dominio del ejemplo es ficticio, por lo que la petición fallará. El `.catch()` captura los errores de red; más adelante veremos también cómo detectar respuestas HTTP no satisfactorias.

---

## Errores dentro de `.then()`

Si se lanza una excepción dentro de un `.then()`, la promesa que devuelve ese `.then()` queda rechazada y el error llega al `.catch()` de la cadena.

```js
Promise.resolve("OK")
  .then(() => {
    throw new Error("Algo falló dentro del then");
  })
  .catch(error => {
    console.error("Error capturado:", error.message);
  });
```

**Salida:**

```text
Error capturado: Algo falló dentro del then
```

No hace falta escribir un `try/catch` en cada `.then()` si el error se puede gestionar en un `.catch()` posterior.

---

## Capturar y volver a lanzar un error

Un `.catch()` puede registrar o analizar el error y volver a lanzarlo para que lo gestione otro bloque posterior.

```js
Promise.reject(new Error("Error inicial"))
  .catch(error => {
    console.warn("Primer manejo:", error.message);
    throw error;
  })
  .catch(error => {
    console.error("Error final:", error.message);
  });
```

**Salida:**

```text
Primer manejo: Error inicial
Error final: Error inicial
```

Se utiliza cuando una parte del programa no puede resolver el error, pero sí registrarlo o añadir información.

---

## Rechazos no gestionados

Si una promesa se rechaza y no existe un manejador de errores, puede producirse un aviso de **rechazo no gestionado**.

```js
Promise.reject(new Error("Fallo grave"));
```

En el navegador se puede escuchar el evento global `unhandledrejection`:

```js
window.addEventListener("unhandledrejection", event => {
  console.error("Rechazo no gestionado:", event.reason);
});
```

En Node.js existe el evento `unhandledRejection` de `process`. Estos mecanismos globales no sustituyen al manejo de errores en cada operación.

---

## Errores en una cadena mixta

```js
fetch("https://api.github.com/users/octocat")
  .then(respuesta => respuesta.json())
  .then(usuario => {
    if (!usuario.login) {
      throw new Error("Usuario no válido");
    }
    return usuario;
  })
  .then(usuario => {
    console.log("Usuario cargado:", usuario.login);
  })
  .catch(error => {
    console.error("Error detectado:", error.message);
  })
  .finally(() => {
    console.log("Proceso finalizado");
  });
```

El `.catch()` puede capturar errores de los pasos anteriores de la cadena. `.finally()` se ejecuta tanto si la cadena termina correctamente como si falla.

---

## Buenas prácticas con errores

- Coloca un `.catch()` al final de las cadenas de promesas.
- Usa errores descriptivos, por ejemplo `new Error("No se pudo cargar el usuario")`.
- Evita anidar `.then()` innecesariamente; encadena los pasos.
- Usa `.finally()` para limpiar recursos o cerrar indicadores de carga.
- No confundas un error de red con una respuesta HTTP de error: `fetch()` normalmente no rechaza por recibir un estado como `404`; conviene comprobar `response.ok`.

---

# 5. API avanzada de `Promise`

JavaScript ofrece métodos estáticos para coordinar varias promesas. Son útiles cuando se deben consultar varias API, cargar recursos o esperar varias operaciones.

| Método | Comportamiento principal |
|---|---|
| `Promise.all()` | Cumple cuando todas cumplen; rechaza si alguna rechaza. |
| `Promise.allSettled()` | Espera a todas e informa del resultado individual. |
| `Promise.race()` | Se resuelve o rechaza con la primera promesa que termina. |
| `Promise.any()` | Cumple con la primera promesa que se cumple correctamente. |
| `Promise.resolve()` | Crea una promesa cumplida con un valor. |
| `Promise.reject()` | Crea una promesa rechazada. |

---

# `Promise.all()`

Espera a que **todas** las promesas se cumplan. Si una se rechaza, la promesa resultante se rechaza.

```js
Promise.all([
  fetch("https://api.github.com/users/octocat"),
  fetch("https://api.github.com/users/torvalds"),
  fetch("https://api.github.com/users/mojombo")
])
  .then(respuestas => Promise.all(respuestas.map(r => r.json())))
  .then(usuarios => {
    console.log("Usuarios:", usuarios.map(usuario => usuario.login));
  })
  .catch(error => {
    console.error("Error en Promise.all:", error);
  });
```

Úsalo cuando todas las operaciones sean necesarias para continuar. Las tareas se inician de forma concurrente; no se espera a terminar una para iniciar la siguiente.

---

## `Promise.allSettled()`

Espera a que todas las promesas hayan terminado, aunque alguna falle. Devuelve un array de resultados con su estado.

```js
Promise.allSettled([
  Promise.resolve("Correcta"),
  Promise.reject(new Error("Falló")),
  Promise.resolve("Otra correcta")
]).then(resultados => {
  console.table(resultados);
});
```

Cada resultado tendrá:
- `status: "fulfilled"` y una propiedad `value`, o
- `status: "rejected"` y una propiedad `reason`.

Es útil cuando interesa conocer el resultado de todas las tareas, incluso las que fallan.

---

## `Promise.race()`

Devuelve una promesa que adopta el resultado de la primera promesa que termina, tanto si se cumple como si se rechaza.

```js
Promise.race([
  new Promise(resolve => {
    setTimeout(() => resolve("Gana A"), 1000);
  }),
  new Promise(resolve => {
    setTimeout(() => resolve("Gana B"), 2000);
  })
]).then(resultado => console.log(resultado));
```

**Salida prevista:** `Gana A`.

Puede utilizarse para competir entre operaciones. Para cancelar realmente una petición que tarda demasiado, hay que combinar el control del tiempo con mecanismos de cancelación, como `AbortController`.

---

## `Promise.any()`

Devuelve el resultado de la primera promesa que se cumple correctamente. Ignora los rechazos individuales mientras quede alguna posibilidad de éxito.

```js
Promise.any([
  Promise.reject(new Error("Servidor 1 caído")),
  Promise.resolve("Servidor 2 activo"),
  Promise.reject(new Error("Servidor 3 caído"))
])
  .then(resultado => console.log(resultado))
  .catch(error => console.error("Todas fallaron:", error));
```

**Salida:**

```text
Servidor 2 activo
```

Si todas las promesas se rechazan, `Promise.any()` rechaza con un `AggregateError` que agrupa los errores.

---

## `Promise.resolve()` y `Promise.reject()`

Sirven para crear promesas cumplidas o rechazadas de forma explícita.

```js
Promise.resolve("Listo")
  .then(mensaje => console.log(mensaje));

Promise.reject(new Error("Error forzado"))
  .catch(error => console.error(error.message));
```

Pueden resultar útiles al adaptar valores o errores a una función que trabaja con promesas.

---

## Comparativa de la API de Promise

| Método | ¿Cuándo termina la promesa resultante? | Resultado |
|---|---|---|
| `Promise.all()` | Cuando todas cumplen o una falla | Array de valores, o rechazo |
| `Promise.allSettled()` | Cuando todas terminan | Array con estados y valores/errores |
| `Promise.race()` | Cuando termina la primera | Primer valor o primer error |
| `Promise.any()` | Cuando cumple la primera; si todas fallan, rechaza | Primer valor correcto o `AggregateError` |
| `Promise.resolve()` | Inmediatamente queda cumplida | Valor |
| `Promise.reject()` | Inmediatamente queda rechazada | Error/razón del rechazo |

---

## ¿Qué método conviene utilizar?

- **Necesito todos los resultados:** `Promise.all()`.
- **Necesito conocer qué operaciones han funcionado y cuáles no:** `Promise.allSettled()`.
- **Me interesa la primera operación que termine, sea éxito o error:** `Promise.race()`.
- **Me basta con que una de varias alternativas funcione:** `Promise.any()`.

La elección depende de si son imprescindibles todas las respuestas, si interesa el primer resultado o si basta con el primer éxito.

---

# 6. Promisificación

## ¿Qué es la promisificación?

La **promisificación** consiste en convertir una función basada en callbacks en otra función que devuelve una promesa.

Así se puede utilizar con `.then()`, `.catch()` o `async/await`, haciendo que el código sea más fácil de encadenar y reutilizar.

Es habitual al adaptar código antiguo o APIs basadas en callbacks.

---

### Ejemplo clásico basado en callback

```js
function loadScript(src, callback) {
  const script = document.createElement("script");
  script.src = src;

  script.onload = () => callback(null, script);
  script.onerror = () => callback(new Error("Error al cargar el script"));

  document.head.append(script);
}

loadScript("main.js", (err, script) => {
  if (err) {
    console.error(err);
  } else {
    console.log("Script cargado:", script.src);
  }
});
```

Inconvenientes:
- El código de éxito y error se gestiona en el callback.
- Encadenar operaciones resulta menos directo.
- El anidamiento puede aumentar con cada nueva tarea.

---

## Convertir la función para que devuelva una promesa

```js
function loadScriptPromise(src) {
  return new Promise((resolve, reject) => {
    const script = document.createElement("script");
    script.src = src;

    script.onload = () => resolve(script);
    script.onerror = () => reject(new Error("Error al cargar el script"));

    document.head.append(script);
  });
}

loadScriptPromise("main.js")
  .then(script => console.log("Script cargado:", script.src))
  .catch(error => console.error(error));
```

Ventajas:
- Código más lineal.
- Manejo de errores uniforme.
- Compatible con `async/await`.
- Fácil de reutilizar en otros flujos.

---

## Una función genérica `promisify()`

Para funciones que usan la convención `callback(error, resultado)`, se puede crear un adaptador genérico:

```js
function promisify(func) {
  return function (...args) {
    return new Promise((resolve, reject) => {
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
```

Esta versión es didáctica: presupone que el callback sigue la convención `error, resultado` y que devuelve un único resultado principal.

---

### Ejemplo de `promisify()`

```js
function getData(callback) {
  setTimeout(() => {
    callback(null, "Datos cargados correctamente");
  }, 1000);
}

const getDataPromise = promisify(getData);

getDataPromise()
  .then(datos => console.log(datos))
  .catch(error => console.error(error));
```

**Salida:**

```text
Datos cargados correctamente
```

La función original sigue usando un callback; el adaptador permite consumirla mediante una promesa.

---

## Promisificar funciones con varios resultados

Algunas funciones pueden invocar un callback con más de un resultado: `callback(error, resultado1, resultado2)`.

```js
function promisifyMany(func) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      func(...args, (error, ...resultados) => {
        if (error) {
          reject(error);
        } else {
          resolve(resultados);
        }
      });
    });
  };
}

function dividir(a, b, callback) {
  if (b === 0) {
    callback(new Error("División por cero"));
  } else {
    callback(null, a / b, "Operación completada");
  }
}

const dividirPromise = promisifyMany(dividir);

dividirPromise(10, 2)
  .then(([resultado, mensaje]) => console.log(resultado, mensaje))
  .catch(error => console.error(error.message));
```

**Salida:** `5 Operación completada`.

---

# 7. Async/Await

`async` y `await` permiten trabajar con promesas con una sintaxis que se lee de arriba abajo, sin encadenar manualmente muchos `.then()`.

No eliminan las promesas: hacen que su consumo sea más cómodo.

---

## ¿Qué hace `async`?

Una función declarada con `async` **siempre devuelve una promesa**.

```js
async function saludar() {
  return "Hola mundo";
}

saludar().then(mensaje => console.log(mensaje));
```

Aunque la función devuelve un texto, JavaScript lo envuelve en una promesa cumplida.

Es equivalente, a efectos del resultado, a:

```js
function saludar() {
  return Promise.resolve("Hola mundo");
}
```

---

## ¿Qué hace `await`?

`await` espera a que una promesa termine y permite acceder directamente a su resultado.

```js
async function esperarMensaje() {
  console.log("Esperando...");

  const mensaje = await new Promise(resolve => {
    setTimeout(() => resolve("¡Listo!"), 2000);
  });

  console.log(mensaje);
}

esperarMensaje();
```

**Salida:**

```text
Esperando...
¡Listo!
```

`await` pausa la ejecución de la función `async`, pero no bloquea el hilo principal: otras tareas pueden continuar.

---

### Ejemplo práctico con `fetch()`

```js
async function mostrarUsuario() {
  try {
    const respuesta = await fetch(
      "https://api.github.com/users/octocat"
    );
    const datos = await respuesta.json();

    console.log("Usuario:", datos.login);
  } catch (error) {
    console.error("Error al cargar el usuario:", error);
  } finally {
    console.log("Petición completada");
  }
}

mostrarUsuario();
```

Hay dos esperas:
1. `fetch()` espera la respuesta HTTP.
2. `respuesta.json()` espera la lectura y conversión del cuerpo a JSON.

**Importante:** `fetch()` no rechaza automáticamente por respuestas HTTP como `404`. En código real conviene comprobar `respuesta.ok`.

---

## Manejo de errores con `try...catch`

En una función `async`, los errores de una promesa esperada con `await` se pueden gestionar mediante `try...catch`.

```js
async function cargarDatos() {
  try {
    const respuesta = await fetch("https://api.inventada123.com");
    if (!respuesta.ok) {
      throw new Error(`HTTP ${respuesta.status}`);
    }

    const datos = await respuesta.json();
    console.log(datos);
  } catch (error) {
    console.error("Error al obtener datos:", error.message);
  }
}

cargarDatos();
```

Si falla la petición, la lectura de JSON o se lanza un error explícito, el flujo pasa al bloque `catch`.

---

## `await` junto con `Promise.all()`

Si varias tareas son independientes, no es necesario esperarlas una a una. Podemos iniciarlas en paralelo con `Promise.all()`.

```js
async function cargarTodo() {
  const [usuario, repositorios] = await Promise.all([
    fetch("https://api.github.com/users/octocat").then(r => r.json()),
    fetch("https://api.github.com/users/octocat/repos").then(r => r.json())
  ]);

  console.log("Usuario:", usuario.login);
  console.log("Repositorios:", repositorios.length);
}

cargarTodo().catch(error => console.error("Error:", error));
```

Las dos peticiones se inician sin esperar a que termine la otra. La función espera el resultado de ambas antes de continuar.

---

## ¿Dónde se puede utilizar `await`?

Tradicionalmente, `await` se utiliza dentro de funciones `async`.

```js
async function obtenerUsuario() {
  const respuesta = await fetch(
    "https://api.github.com/users/octocat"
  );
  const datos = await respuesta.json();
  console.log(datos.login);
}

obtenerUsuario();
```

En entornos modernos también puede utilizarse `await` en el nivel superior de un **módulo ECMAScript** (*top-level await*). Fuera de esos contextos, provoca un error de sintaxis.

---

## `async/await` con funciones flecha

También se puede declarar una función flecha asíncrona:

```js
const obtenerUsuario = async () => {
  const respuesta = await fetch(
    "https://api.github.com/users/octocat"
  );
  const datos = await respuesta.json();

  console.log(datos.login);
};

obtenerUsuario();
```

`async` se coloca antes de los parámetros de la función flecha.

---

## Ventajas de `async/await`

- **Legibilidad:** el flujo se lee de arriba abajo.
- **Manejo de errores:** permite utilizar `try...catch`.
- **Compatibilidad:** trabaja con promesas.
- **Menos encadenamiento:** evita muchos `.then()` consecutivos.
- **Mantenimiento:** facilita seguir los pasos de un proceso asíncrono.

`async/await` no hace que una operación sea automáticamente más rápida; mejora la forma de expresar y organizar el código asíncrono.

---

## Comparación práctica

### Con promesas

```js
fetch("https://api.github.com/users/octocat")
  .then(respuesta => respuesta.json())
  .then(datos => console.log(datos.login))
  .catch(error => console.error(error));
```

### Con `async/await`

```js
async function ejemplo() {
  try {
    const respuesta = await fetch(
      "https://api.github.com/users/octocat"
    );
    const datos = await respuesta.json();
    console.log(datos.login);
  } catch (error) {
    console.error(error);
  }
}

ejemplo();
```

Ambos ejemplos persiguen el mismo objetivo; `async/await` ofrece una estructura secuencial más cómoda cuando hay varios pasos dependientes.

---

## Buenas prácticas con `async/await`

- Usa `try...catch` cuando una operación pueda fallar.
- Comprueba `response.ok` al trabajar con `fetch()`.
- Evita varios `await` secuenciales si las tareas son independientes.
- Utiliza `Promise.all()` para tareas independientes que deban completarse juntas.
- Encapsula las operaciones repetidas en funciones `async`.
- Usa `finally` cuando necesites realizar una acción final.
- Recuerda: `await` pausa la función actual, no todo JavaScript.

---

# 8. Resumen: de callbacks a `async/await`

| Enfoque | Características | Principal inconveniente |
|---|---|---|
| Callbacks | Se pasa una función para ejecutarla después | El anidamiento puede crecer (*callback hell*) |
| Promesas | Representan un resultado futuro y permiten encadenar | Las cadenas largas pueden ser difíciles de seguir |
| `async/await` | Sintaxis secuencial para consumir promesas | Hay que comprender promesas y gestionar los errores |

La evolución de estas herramientas ha facilitado escribir código asíncrono más legible y mantenible.

---

## Flujo de una promesa

```text
             Se crea la promesa
                     |
                 pending
                /       \
        resolve(valor)  reject(error)
              |             |
          fulfilled       rejected
              |             |
           .then()        .catch()
                \          /
                  .finally()
```

Una promesa termina cumpliéndose o rechazándose. `.finally()` permite ejecutar una acción final independientemente del resultado.

---

## Flujo de `async/await`

```js
async function tarea() {
  try {
    const resultado = await operacionAsincrona();
    console.log(resultado);
  } catch (error) {
    console.error(error);
  } finally {
    console.log("Tarea finalizada");
  }
}
```

1. `async` hace que la función devuelva una promesa.
2. `await` espera el resultado de la operación dentro de esa función.
3. `try...catch` permite manejar errores.
4. `finally` se ejecuta al finalizar, tanto si hay éxito como si hay error.

---

## Promesas frente a `async/await`

| Aspecto | Promesas | `async/await` |
|---|---|---|
| Sintaxis | Encadenada con `.then()` | Secuencial con `await` |
| Errores | `.catch()` | `try...catch` |
| Tareas paralelas | `Promise.all()` | `await Promise.all()` |
| Uso adecuado | Encadenar resultados y coordinar tareas | Expresar con claridad pasos dependientes |

No son tecnologías distintas: `async/await` se apoya en las promesas.

---

## Errores comunes

**Olvidar gestionar un rechazo**

Puede producir un rechazo no gestionado. Añade `.catch()` o usa `try...catch` al esperar la promesa.

**Usar `await` fuera de un contexto permitido**

Puede causar un error de sintaxis. Utiliza una función `async` o top-level await en un módulo compatible.

**No devolver un valor en un `.then()`**

Si el siguiente paso necesita ese resultado, debes devolverlo:

```js
obtenerDatos()
  .then(datos => {
    return transformar(datos);
  })
  .then(resultado => console.log(resultado))
  .catch(error => console.error(error));
```

---

## Patrón combinado: `Promise.all()` + `async/await`

```js
async function ejecutarTareas() {
  try {
    const [usuario, repositorios] = await Promise.all([
      fetch("https://api.github.com/users/octocat")
        .then(r => {
          if (!r.ok) throw new Error(`HTTP ${r.status}`);
          return r.json();
        }),
      fetch("https://api.github.com/users/octocat/repos")
        .then(r => {
          if (!r.ok) throw new Error(`HTTP ${r.status}`);
          return r.json();
        })
    ]);

    console.log("Usuario:", usuario.login);
    console.log("Repositorios:", repositorios.length);
  } catch (error) {
    console.error("Error:", error);
  }
}

ejecutarTareas();
```

Ventajas:
- Ejecuta las tareas independientes en paralelo.
- Mantiene el código organizado.
- Centraliza el manejo de errores.

---

## Buenas prácticas finales

- Gestiona los errores con `.catch()` o `try...catch`.
- Usa `await` solo cuando necesites el resultado para continuar.
- Combina `Promise.all()` para operaciones independientes.
- Documenta qué devuelve cada función asíncrona.
- Comprueba los estados HTTP cuando uses `fetch()`.
- Recuerda que esperar dentro de una función no bloquea globalmente el hilo principal.

---

<!-- _class: lead -->

# Conclusión

Las promesas y `async/await` son herramientas esenciales para gestionar la asincronía en JavaScript.

Permiten construir código más claro, legible y mantenible, con un control explícito de los resultados y los errores.

## Idea clave

**Usa promesas para representar y coordinar tareas asíncronas; usa `async/await` para consumirlas con un flujo fácil de seguir.**
