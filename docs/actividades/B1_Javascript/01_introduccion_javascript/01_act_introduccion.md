---
marp: true
math: katex
paginate: true
html: true
size: 16:9
header: "2º DAM · 2026-2027"
theme: default
footer: "Lorena Sánchez Sánchez"
style: |
 :root { --fondo:#FFFFFF; --azul:#C8EDED; --rosa:#FDD4E3; --verde:#18D6C0; --amarillo:#F9EAC1; --rosa-fuerte:#FDB3CA; --texto:#4E4A42; --lila:#EE4091; }
  section { font-family: "Aptos", "Segoe UI", sans-serif; background:#FFF; color:#4E4A42; padding:50px 60px 40px; font-size:1.15em; line-height:1.30; }
  h1 { color:#EE4091; font-size:2.65em; font-weight:800; border-bottom:6px solid #C8EDED; padding-bottom:10px; }
  h2 { color:#18D6C0; font-size:2.15em; }
  h3 { color:#EE4091; }
  strong { color:#18D6C0; }
  header { position:absolute; top:0; left:0; width:100%; height:40px; line-height:40px; background:#C8EDED; color:#4E4A42; font-weight:600; text-align:center; font-size:1.05em; }
  section::after { background:white; border:3px solid #18D6C0; color:#18D6C0; width:36px; height:36px; border-radius:50%; right:15px; bottom:2px; display:flex; justify-content:center; align-items:center; font-size:1.3em; font-weight:700; }
  img { max-height:430px; display:block; margin:auto; }
  .small { font-size:.78em; }
  .tiny { font-size:.65em; }
  .center { text-align:center; }
  .two { display:grid; grid-template-columns:1fr 1fr; gap:30px; align-items:center; }
  .box { padding:18px 24px; background:#F4FCFC; border-left:8px solid #18D6C0; }
  .warn { padding:18px 24px; background:#FFF3F7; border-left:8px solid #EE4091; }
  .activity { padding:20px 26px; background:#F4FCFC; border:3px solid #18D6C0; border-radius:16px; }
  code { font-size:.86em; }
  footer { position:absolute; bottom:0; left:0; width:100%; height:30px; line-height:42px; background:var(--rosa-fuerte); color:var(--texto); text-align:center; font-size:0.80em; font-weight:600; }
---




# ACTIVIDADES – UD2 INTRODUCCIÓN A JAVASCRIPT

## 2º DAM · Sesión práctica

**Tiempo máximo total: 2 horas**

### Objetivo
Practicar especialmente los contenidos que requieren más razonamiento:
- conversiones de tipos
- `==` frente a `===`
- `null` y `undefined`
- valores *truthy/falsy*
- `&&`, `||`, `!` y `??`
- precedencia y comportamiento de los operadores
- condicionales y operador ternario

---

# Organización de la sesión

### Tiempo máximo: 120 minutos

| Parte | Tiempo |
|---|---:|
| 🧠 Actividad 1 – Tipo test | 20 min |
| 🔎 Actividad 2 – ¿Qué devuelve JavaScript? | 25 min |
| ⚙️ Actividad 3 – Condiciones y operadores lógicos | 30 min |
| 💻 Actividad 4 – Mini programa | 35 min |
| 🚀 Reto final | 10 min |


---

# ACTIVIDAD 1 · TIPO TEST

### 20 minutos · 10 preguntas

Selecciona **una única respuesta correcta**.

### 1. ¿Qué devuelve `typeof null`?

A. `"null"`  
B. `"undefined"`  
C. `"object"`  
D. `"boolean"`

### 2. ¿Qué resultado produce?

```javascript
Number("25")
```

A. `"25"`  
B. `25`  
C. `NaN`  
D. `true`

---

### 3. ¿Cuál es un valor *falsy*?

A. `"0"`  
B. `[]`  
C. `0`  
D. `"false"`


### 4. ¿Qué devuelve?

```javascript
Boolean("0")
```

A. `false`  
B. `true`  
C. `0`  
D. `NaN`

---

### 5. ¿Qué diferencia principal existe entre `==` y `===`?

A. `===` convierte siempre a string  
B. `==` permite conversión de tipos y `===` exige igualdad estricta  
C. Son exactamente iguales  
D. `==` solo funciona con números

---

### 6. ¿Qué devuelve?

```javascript
null == undefined
```

A. `true`  
B. `false`  
C. `null`  
D. `NaN`

---

### 7. ¿Qué devuelve?

```javascript
null === undefined
```

A. `true`  
B. `false`  
C. `null`  
D. `undefined`

---

### 8. ¿Qué devuelve?

```javascript
"Hola" || "Adiós"
```

A. `"Hola"`  
B. `"Adiós"`  
C. `true`  
D. `false`

### 9. ¿Qué devuelve?

```javascript
0 || "Sin datos"
```

A. `0`  
B. `false`  
C. `"Sin datos"`  
D. `null`

---

### 10. ¿Qué diferencia fundamental hay entre `||` y `??`?

A. `??` considera `0` como ausencia de valor  
B. `||` solo funciona con booleanos  
C. `??` solo sustituye `null` y `undefined`  
D. No existe diferencia

---

# ACTIVIDAD 2 · ¿QUÉ DEVUELVE JAVASCRIPT?

### 25 minutos

Sin ejecutar el código, escribe el resultado.

Después **comprueba tus respuestas en la consola**.

### Ejercicio 1

```javascript
console.log(Number("15"));
console.log(Number("15px"));
console.log(Number(""));
console.log(Number(null));
console.log(Number(undefined));
```

Indica qué aparece en cada línea.

---

# ACTIVIDAD 2 · ¿QUÉ DEVUELVE JAVASCRIPT?

### Ejercicio 2

Completa la tabla:

| Expresión | Resultado |
|---|---|
| `Boolean(0)` | |
| `Boolean(1)` | |
| `Boolean("")` | |
| `Boolean("0")` | |
| `Boolean(null)` | |
| `Boolean(undefined)` | |
| `Boolean("false")` | |

---

### Ejercicio 3

Indica `true` o `false`:

```javascript
5 == "5"
5 === "5"

0 == false
0 === false

null == undefined
null === undefined
```

**Explica al menos dos de las respuestas.**

---


### Ejercicio 4 · El más importante

Predice el resultado y después compruébalo:

```javascript
console.log(0 || "A");
console.log(0 ?? "A");

console.log("" || "B");
console.log("" ?? "B");

console.log(null || "C");
console.log(null ?? "C");

console.log(undefined || "D");
console.log(undefined ?? "D");
```

### Pregunta

¿Por qué `0` y `""` se comportan de forma diferente con `||` y `??`?

---

# ACTIVIDAD 3 · CONDICIONES Y OPERADORES LÓGICOS

### 30 minutos

Crea:

```javascript
let edad = 20;
let tieneEntrada = true;
let estaInvitado = false;
```

### Ejercicio 1

Escribe una condición que permita entrar si:

- tiene entrada **Y**
- es mayor o igual que 18

---


### Ejercicio 2

Modifica el programa para permitir entrar si:

- tiene entrada **Y** tiene 18 años o más

**O**

- está invitado

Utiliza `&&` y `||`.

### Ejercicio 3

Añade:

```javascript
let usuarioBloqueado = false;
```

La persona **no puede entrar** si está bloqueada.

Utiliza `!`.

---


### Ejercicio 4 · Atención a los paréntesis

Analiza:

```javascript
let edad = 17;
let tieneEntrada = true;
let estaInvitado = false;

let puedeEntrar =
    edad >= 18 && tieneEntrada || estaInvitado;
```

1. ¿Qué valor tiene `puedeEntrar`?
2. ¿Qué condición se está evaluando?
3. ¿Cambiaría el resultado con:

```javascript
edad >= 18 && (tieneEntrada || estaInvitado)
```

4. Explica por qué.

---


### Ejercicio 5 · `??`

Crea:

```javascript
let nombre = null;
```

Utiliza `??` para mostrar:

```text
Usuario desconocido
```

si `nombre` no tiene valor.

Después prueba:

```javascript
nombre = "";
nombre = "Ana";
```

Explica qué ocurre en cada caso.

---

# ACTIVIDAD 4 · MINI PROGRAMA

### 35 minutos

## Sistema de acceso a una plataforma DAM

Crea un programa que solicite:

```javascript
let usuario = prompt("Usuario:");
let edad = Number(prompt("Edad:"));
let esProfesor = ...
let bloqueado = ...
```

El programa debe determinar si la persona puede acceder.

---

# ACTIVIDAD 4 · REQUISITOS

### Acceso permitido

El acceso se permite cuando:

- la edad es **18 o superior**
- el usuario no está bloqueado
- y además:
  - es profesor **O**
  - el usuario es `"admin"`

Utiliza obligatoriamente:

- `Number()`
- `===`
- `&&`
- `||`
- `!`
- `if / else`

---

# ACTIVIDAD 4 · VALIDACIÓN

El programa también debe detectar:

### Edad no válida

Si la edad introducida no es válida, muestra:

```text
La edad introducida no es válida.
```

### Usuario vacío

Si no se introduce usuario, utiliza:

```javascript
?? 
```

para mostrar un usuario alternativo.


---

### Resultado

Si puede acceder:

```text
Acceso permitido
```

En caso contrario:

```text
Acceso denegado
```

---

# ACTIVIDAD 4 · CONDICIÓN FINAL

Antes de ejecutar el programa completo, escribe primero en una hoja o comentario la condición:

```javascript
puedeAcceder = ...
```

Debe representar exactamente:

> Tiene 18 años o más, no está bloqueado y además es profesor o es admin.

Después comprueba varios casos:

| Edad | Usuario | Profesor | Bloqueado | Resultado |
|---:|---|---|---|---|
| 20 | ana | sí | no | |
| 17 | ana | sí | no | |
| 25 | admin | no | no | |
| 25 | ana | no | no | |
| 25 | ana | sí | sí | |

---

# 🚀 RETO FINAL

## 10 minutos

Sin copiar el ejercicio anterior, crea una condición para decidir si un alumno:

### Puede presentarse a un examen cuando:

- tiene una nota de evaluación de **5 o más**
- y **no** tiene una incidencia
- o tiene una autorización especial

---

Utiliza:

```javascript
&&
||
!
```

Después transforma el resultado en un mensaje mediante:

```javascript
condición ? "Puede presentarse" : "No puede presentarse"
```

---

# ENTREGA

### Al finalizar los 120 minutos

Entrega un único archivo:

```text
UD2_Actividades_NombreAlumno.js
```

Debe contener:

1. Respuestas del tipo test mediante comentarios.
2. Resultados de la Actividad 2.
3. Actividad 3 completa.
4. Mini programa de acceso.
5. Reto final.

---

### Importante

Los ejercicios deben estar **probados en la consola**.

No basta con escribir lo que crees que devuelve JavaScript:
**predice → ejecuta → compara → explica los errores.**

---

# OBJETIVOS CONSEGUIDOS

Al terminar deberías ser capaz de:

- Diferenciar `==` y `===`.
- Trabajar con `null` y `undefined`.
- Convertir valores con `Number()` y `Boolean()`.
- Identificar valores *truthy/falsy*.
- Entender qué devuelven `&&` y `||`.
- Diferenciar `||` de `??`.
- Construir condiciones con varios operadores.
- Utilizar correctamente `!`.
- Resolver condiciones con `if/else`.
- Utilizar el operador ternario.
