# INTRODUCCION A OBJETOS EN JAVASCRIPT {.objetos-heading}
2º DAW - Desarrollo Web en Entorno Cliente

# ¿Qué son objetos básicos? {.objetos-heading}

- Los objetos son usados para almacenar colecciones de varios datos y entidades más complejas asociados con un nombre clave. En JavaScript, los objetos penetran casi todos los aspectos del lenguaje. Por lo tanto, debemos comprenderlos primero antes de profundizar en cualquier otro lugar.

Podemos crear un objeto usando las llaves {…} con una lista opcional de propiedades. Una propiedad es un par “key:value”, donde key es un string (también llamado “nombre clave”), y value puede ser cualquier cosa.

Se puede crear un objeto vacío (“gabinete vacío”) utilizando una de las dos sintaxis (Normalmente se utilizan las llaves {...}.  Esa declaración se llama objeto literal):

![](imagenes/UD23%20-%20Objetos_0.jpg)

## Literales y propiedades {.objetos-heading}

Podemos poner inmediatamente algunas propiedades dentro de {...} como pares “clave:valor”:

![](imagenes/UD23%20-%20Objetos_1.jpg)

Una propiedad tiene una clave (también conocida como “nombre” o “identificador”) antes de los dos puntos ":" y un valor a la derecha. En el objeto user hay dos propiedades:

La primera propiedad tiene la clave "name" y el valor "John".

La segunda tienen la clave "age" y el valor 30.

Podemos imaginar al objeto user resultante como un gabinete con dos archivos firmados con las etiquetas “name” y “age”.

![](imagenes/UD23%20-%20Objetos_2.png)

Podemos agregar, eliminar y leer archivos de él en cualquier momento.

Se puede acceder a los valores de las propiedades utilizando la notación de punto:

![](imagenes/UD23%20-%20Objetos_3.jpg)

El valor puede ser de cualquier tipo. Agreguemos uno booleano:

![](imagenes/UD23%20-%20Objetos_4.png)

Para eliminar una propiedad podemos usar el operador delete:

![](imagenes/UD23%20-%20Objetos_5.png)

También podemos nombrar propiedades con más de una palabra. Pero, de ser así, debemos colocar la clave entre comillas "...":

![](imagenes/UD23%20-%20Objetos_6.png)

La última propiedad en la lista puede terminar con una coma:

![](imagenes/UD23%20-%20Objetos_7.png)

Eso se llama una coma “final” o “colgante”. Facilita agregar, eliminar y mover propiedades, porque todas las líneas se vuelven similares.

La notación de punto no funciona para acceder a propiedades con claves de más de una palabra:

![](imagenes/UD23%20-%20Objetos_8.png)

El punto requiere que la clave sea un identificador de variable válido. Eso implica que: no contenga espacios, no comience con un dígito y no incluya caracteres especiales ($ y _ sí se permiten).

Existe una “notación de corchetes” alternativa que funciona con cualquier string:

![](imagenes/UD23%20-%20Objetos_9.png)

Ahora todo está bien. Nota que el string dentro de los corchetes está adecuadamente entre comillas (cualquier tipo de comillas servirían).

Los corchetes también brindan una forma de obtener el nombre de la propiedad desde el resultado de una expresión (a diferencia de la cadena literal). Por ejemplo, a través de una variable:

![](imagenes/UD23%20-%20Objetos_10.png)

Aquí la variable key puede calcularse en tiempo de ejecución o depender de la entrada del usuario y luego lo usamos para acceder a la propiedad. Eso nos da mucha flexibilidad. Por ejemplo:

![](imagenes/UD23%20-%20Objetos_11.jpg)

![](imagenes/UD23%20-%20Objetos_12.png)

La notación de punto no puede ser usada de manera similar:

## Propiedades calculadas {.objetos-heading}


Las propiedades calculadas (*Computed Properties*) permiten generar el nombre de una propiedad dinámicamente utilizando una expresión.

```javascript
const clave = 'nombre';

const usuario = {
  [clave]: 'Lorena'
};
```

Resultado:

```javascript
{ nombre: 'Lorena' }
```

---

### Problema que Resuelven

Sin propiedades calculadas debes conocer el nombre de la propiedad al escribir el código.

```javascript
const usuario = {
  nombre: 'Lorena'
};
```

¿Y si el nombre llega desde una variable, un formulario o una API?

---

### Sintaxis

```javascript
const clave = 'nombre';

const objeto = {
  [clave]: 'Lorena'
};
```

La expresión entre corchetes se evalúa.

El resultado se convierte en el nombre de la propiedad.

---

### Sin Corchetes

```javascript
const clave = 'nombre';

const objeto = {
  clave: 'Lorena'
};
```

Resultado:

```javascript
{
  clave: 'Lorena'
}
```

La propiedad se llama literalmente "clave".

---

###  Con Corchetes

```javascript
const clave = 'nombre';

const objeto = {
  [clave]: 'Lorena'
};
```

Resultado:

```javascript
{
  nombre: 'Lorena'
}
```

---

### Qué Ocurre Internamente

```javascript
const clave = 'nombre';

const objeto = {
  [clave]: 'Lorena'
};
```

JavaScript evalúa:

```javascript
clave
```

Obtiene:

```javascript
'nombre'
```

Y crea:

```javascript
{
  nombre: 'Lorena'
}
```

---

### Expresiones Complejas

Dentro de los corchetes puede haber cualquier expresión válida.

```javascript
const id = 7;

const usuario = {
  ['user_' + id]: 'Lorena'
};
```

Resultado:

```javascript
{
  user_7: 'Lorena'
}
```

---

### Uso con Template Strings

```javascript
const id = 25;

const producto = {
  [`producto_${id}`]: 'Portátil'
};
```

Resultado:

```javascript
{
  producto_25: 'Portátil'
}
```

---

### Varias Propiedades Dinámicas

```javascript
const campo1 = 'nombre';
const campo2 = 'edad';

const persona = {
  [campo1]: 'Lorena',
  [campo2]: 30
};
```

Resultado:

```javascript
{
  nombre: 'Lorena',
  edad: 30
}
```

---

### Claves Numéricas

```javascript
const numero = 100;

const datos = {
  [numero]: 'valor'
};
```

Resultado:

```javascript
{
  '100': 'valor'
}
```

Las claves de los objetos siempre son cadenas o símbolos.

---

###  Uso con Symbols

```javascript
const id = Symbol('id');

const usuario = {
  [id]: 123
};
```

Los símbolos generan propiedades únicas.

---

### Formularios

Muy utilizado para capturar cambios de campos.

```javascript
const campo = 'email';
const valor = 'correo@email.com';

const usuario = {
  [campo]: valor
};
```

Resultado:

```javascript
{
  email: 'correo@email.com'
}
```

---

### React: Caso Real

```javascript
setUsuario({
  ...usuario,
  [e.target.name]: e.target.value
});
```

Si el input contiene:

```html
<input name="email" />
```

Se actualiza:

```javascript
usuario.email
```

---

### Configuración Dinámica

```javascript
const entorno = 'produccion';

const config = {
  [`api_${entorno}`]: 'https://api.com'
};
```

Resultado:

```javascript
{
  api_produccion: 'https://api.com'
}
```

---

### Combinación con Spread

```javascript
const clave = 'edad';

const persona = {
  nombre: 'Lorena',
  [clave]: 30
};
```

Resultado:

```javascript
{
  nombre: 'Lorena',
  edad: 30
}
```

---

###  Errores Comunes

#### Error 1

```javascript
const clave = 'nombre';

const obj = {
  clave: 'Lorena'
};
```

No crea la propiedad nombre.

Crea la propiedad clave.

---

#### Error 2

```javascript
const obj = {
  [undefined]: 'valor'
};
```

Resultado:

```javascript
{
  undefined: 'valor'
}
```

Comprueba siempre el contenido de la variable.

---

### Diferencia entre Crear y Acceder

Crear:

```javascript
const clave = 'nombre';

const obj = {
  [clave]: 'Lorena'
};
```

Acceder:

```javascript
obj[clave]
```

Resultado:

```javascript
'Lorena'
```

---

### Regla de Oro

Sin corchetes:

```javascript
{
  clave: valor
}
```

La propiedad se llama literalmente:

```javascript
'clave'
```

Con corchetes:

```javascript
{
  [clave]: valor
}
```

La propiedad se llama como el valor almacenado en la variable.

---

### Resumen Final

✅ Permiten crear propiedades dinámicas.
✅ Utilizan la sintaxis `[expresion]`.
✅ La expresión se evalúa antes de crear la propiedad.
✅ Se usan mucho en React y formularios.
✅ Admiten variables, concatenaciones, template strings y símbolos.
✅ Son una característica fundamental para construir objetos de manera flexible.







## Atajo para valores de propiedad {.objetos-heading}

En el código real, a menudo usamos variables existentes como valores de los nombres de propiedades. Por ejemplo:

![](imagenes/UD23%20-%20Objetos_16.png)

En el ejemplo anterior las propiedades tienen los mismos nombres que las variables. El uso de variables para la creación de propiedades es tán común que existe un atajo para valores de propiedad especial para hacerla más corta.

En lugar de name:name, simplemente podemos escribir name, tal cual:

![](imagenes/UD23%20-%20Objetos_17.png)

Podemos usar ambos tipos de notación en un mismo objeto, la normal y el atajo:

![](imagenes/UD23%20-%20Objetos_18.png)

## Limitaciones de nombres de propiedad {.objetos-heading}

Como sabemos, una variable no puede tener un nombre igual a una de las palabras reservadas del lenguaje, como “for”, “let”, “return”, etc. Pero para una propiedad de objeto no existe tal restricción:

![](imagenes/UD23%20-%20Objetos_19.png)

En resumen, no hay limitaciones en los nombres de propiedades. Pueden ser cadenas o símbolos (un tipo especial para identificadores que se cubrirán más adelante). Otros tipos se convierten automáticamente en cadenas.

Por ejemplo, un número 0 se convierte en cadena "0" cuando se usa como clave de propiedad:

![](imagenes/UD23%20-%20Objetos_20.jpg)

Hay  una  pequeña  sorpresa  por  una  propiedad  especial  llamada  _	_ proto _	_ .  No  podemos establecerlo dentro de un valor que no sea de objeto:

![](imagenes/UD23%20-%20Objetos_21.jpg)

Como podemos ver en el código, se ignora la asignación de un valor primitivo 5.



# __ proto __ en JavaScript

## ¿Qué es?

`__proto__` es una propiedad interna que apunta al **prototipo** de un objeto.

Gracias a ella, los objetos pueden heredar propiedades y métodos de otros objetos.

```javascript
const persona = {
  nombre: 'Lorena'
};

console.log(persona.__proto__);
```

---

## La cadena de prototipos

Cuando accedes a una propiedad:

```javascript
persona.nombre
```

JavaScript busca:

1. En el propio objeto.
2. En su prototipo.
3. En el prototipo del prototipo.
4. Hasta llegar a `null`.

Esto se llama **Prototype Chain**.

---

## Ejemplo sencillo

```javascript
const animal = {
  respirar() {
    console.log('Respirando');
  }
};

const perro = {
  nombre: 'Toby'
};

perro.__proto__ = animal;

perro.respirar();
```

Resultado:

```text
Respirando
```

Aunque `perro` no tiene el método `respirar`, lo encuentra en su prototipo.

---

## Qué ocurre internamente

```javascript
perro.respirar()
```

JavaScript busca:

```javascript
perro.respirar
```

No existe.

Entonces busca en:

```javascript
perro.__proto__
```

Y encuentra:

```javascript
animal.respirar
```

---

## Todos los objetos tienen prototipo

```javascript
const obj = {};

console.log(obj.__proto__);
```

Resultado aproximado:

```javascript
Object.prototype
```

Por eso todos los objetos disponen de métodos como:

```javascript
obj.toString();
obj.hasOwnProperty('x');
```

---

## Object.prototype

Es el prototipo base de casi todos los objetos.

```javascript
const usuario = {};

console.log(usuario.__proto__ === Object.prototype);
```

Resultado:

```javascript
true
```

---

## ¿Por qué no se recomienda usar __proto__?

Aunque funciona, hoy se considera una API heredada.

Se recomienda utilizar:

```javascript
Object.getPrototypeOf(obj);
```

Para obtener el prototipo.

Y:

```javascript
Object.setPrototypeOf(obj, proto);
```

Para modificarlo.

---

## Equivalencias

Obtener prototipo:

```javascript
obj.__proto__
```

Equivale a:

```javascript
Object.getPrototypeOf(obj)
```

---

Modificar prototipo:

```javascript
obj.__proto__ = animal;
```

Equivale a:

```javascript
Object.setPrototypeOf(obj, animal);
```

---

## Funciones y prototipos

Las funciones constructoras tienen una propiedad especial:

```javascript
function Persona() {}

console.log(Persona.prototype);
```

No es lo mismo que:

```javascript
obj.__proto__
```

---

## Diferencia importante

```javascript
Persona.prototype
```

Es el objeto que usarán las instancias como prototipo.

Mientras que:

```javascript
instancia.__proto__
```

Es el prototipo real de esa instancia.

---

## Ejemplo

```javascript
function Persona() {}

const lorena = new Persona();

console.log(lorena.__proto__ === Persona.prototype);
```

Resultado:

```javascript
true
```

---

## Resumen

✅ `__proto__` apunta al prototipo de un objeto.
✅ Permite la herencia prototípica.
✅ JavaScript busca propiedades recorriendo la cadena de prototipos.
✅ Todos los objetos suelen heredar de `Object.prototype`.
✅ Actualmente es preferible usar:

```javascript
Object.getPrototypeOf()
Object.setPrototypeOf()
```

✅ Relación clave:

```javascript
instancia.__proto__ === Constructor.prototype
```


## La prueba de propiedad existente, el operador “in” {.objetos-heading}

La lectura de una propiedad no existente solo devuelve undefined. Así que podemos probar fácilmente si la propiedad existe:

![](imagenes/UD23%20-%20Objetos_22.jpg)

También existe un operador especial para ello: "in". La sintaxis es:

![](imagenes/UD23%20-%20Objetos_23.png)

![](imagenes/UD23%20-%20Objetos_24.jpg)

Nota que a la izquierda de in debe estar el nombre de la propiedad que suele ser un string entre comillas. Si omitimos las comillas, significa que es una variable. Esta variable debe almacenar la clave real que será probada. Por ejemplo:

![](imagenes/UD23%20-%20Objetos_25.jpg)

La mayoría de las veces las comparaciones con undefined funcionan bien. Pero hay un caso especial donde esto falla y aún así "in" funciona correctamente. Es cuando existe una propiedad de objeto, pero almacena undefined:

![](imagenes/UD23%20-%20Objetos_26.jpg)

En el código anterior, la propiedad obj.test técnicamente existe. Entonces el operador in funciona correctamente. Situaciones como esta suceden raramente ya que undefined no debe ser explícitamente asignado. Comúnmente usamos null para valores “desconocidos” o “vacíos”.

## El bucle "for..in" {.objetos-heading}

Para recorrer todas las claves de un objeto existe una forma especial de bucle: for..in. Esto es algo completamente diferente a la construcción for(;;) que estudiaremos más adelante. La sintaxis:

![](imagenes/UD23%20-%20Objetos_27.jpg)

Por ejemplo, mostremos todas las propiedades de user:

![](imagenes/UD23%20-%20Objetos_28.png)

Nota que todas las construcciones “for” nos permiten declarar variables para bucle dentro del bucle, como let key aquí. A demás podríamos usar otros nombres de variables en lugar de key. Por ejemplo, "for (let prop in obj)" también se usa bastante.

## Ordenado como un objeto {.objetos-heading}

¿Los objetos están ordenados? Es decir, si creamos un bucle sobre un objeto, ¿obtenemos todas las propiedades en el mismo orden en el que se agregaron? ¿Podemos confiar en ello?

La respuesta corta es: “ordenados de una forma especial”: las propiedades de números enteros se ordenan, los demás aparecen en el orden de la creación. Entremos en detalle. Como ejemplo, consideremos un objeto con códigos telefónicos:

![](imagenes/UD23%20-%20Objetos_29.png)

El objeto puede usarse para sugerir al usuario una lista de opciones. Si estamos haciendo un sitio principalmente para el público alemán, probablemente queremos que 49 sea el primero.

Pero si ejecutamos el código, veremos una imagen totalmente diferente:

USA (1) va primero

Luego Switzerland (41) y así sucesivamente.

Los códigos telefónicos van en orden ascendente porque son números enteros. Entonces vemos 1, 41, 44, 49.

…Por otro lado, si las claves no son enteras, se enumeran en el orden de creación, por ejemplo:

![](imagenes/UD23%20-%20Objetos_30.jpg)

Entonces, para solucionar el problema con los códigos telefónicos, podemos “hacer trampa” haciendo que los códigos no sean enteros. Agregar un signo más "+" antes de cada código será más que suficiente. Justo así:

![](imagenes/UD23%20-%20Objetos_31.png)

## RESUMEN {.objetos-heading}

Los objetos son arreglos asociativos con varias características especiales. Almacenan propiedades (pares   de clave-valor), donde:

- Las claves de propiedad deben ser cadenas o símbolos (generalmente strings).

- Los valores pueden ser de cualquier tipo.

Para acceder a una propiedad, podemos usar:

- La notación de punto: obj.property.

- La notación de corchetes obj["property"]. Los corchetes permiten tomar la clave de una variable, como obj[varWithKey].

Operadores adicionales:

- Para eliminar una propiedad: delete obj.prop.
- Para comprobar si existe una propiedad con la clave proporcionada: "key" in obj.
- Para crear bucles sobre un objeto: bucle for (let key in obj).
- Lo que hemos estudiado en este capítulo se llama “objeto simple”, o solamente Object.

Hay muchos otros tipos de objetos en JavaScript:

- Array para almacenar colecciones de datos ordenados,
- Date para almacenar la información sobre fecha y hora,
- Error para almacenar información sobre un error.

Tienen sus características especiales que estudiaremos más adelante. A veces las personas dicen algo como “Tipo array" o "Tipo date", pero formalmente no son tipos en sí, sino que pertenecen a un tipo de datos de “objeto” simple y lo amplían a varias maneras.

Los objetos en JavaScript son muy poderosos. Aquí acabamos de arañar la superficie de un tema que es    realmente enorme. Trabajaremos estrechamente con los objetos y aprenderemos más sobre ellos en otras partes del tutorial.

# TAREAS {.objetos-heading}

## Hola, objeto {.objetos-heading}

Escribe el código, una línea para cada acción:

- Crea un objeto user vacío.

Agrega la propiedad name con el valor John. Agrega la propiedad surname con el valor Smith. Cambia el valor de name a Pete.

Remueve la propiedad name del objeto.

### Solución:

```javascript

const user = {};
user.name = "John";
user.surname = "Smith";
user.name = "Pete";
delete user.name;

````

## Verificar los vacíos {.objetos-heading}

Escribe la función isEmpty(obj) que devuelva el valor true si el objeto no tiene propiedades, en caso contrario false.

Debería funcionar así:

```javascript
let schedule = {};
alert( isEmpty(schedule) ); // true
schedule["8:30"] = "Hora de levantarse"; alert( isEmpty(schedule) ); // false
```

### Solución:


```javascript
let schedule = {};
alert( isEmpty(schedule) ); // true
schedule["8:30"] = "Hora de levantarse"; alert( isEmpty(schedule) ); // false
```

### Ejemplo de uso de la función isEmpty:

```javascript
let schedule = {};
console.log(isEmpty(schedule)); // true
schedule["8:30"] = "Hora de levantarse";
console.log(isEmpty(schedule)); // false
```

## Multiplicar propiedades numéricas por 2 {.objetos-heading}

Crea una función multiplyNumeric(obj) que multiplique todas las propiedades numéricas de obj por 2.

Por ejemplo:

```javascript
// Antes de la llamada
let menu = {
  width: 200,
  height: 300,
  title: "Mi menú"
};

multiplyNumeric(menu);

// Después de la llamada
menu = {
  width: 400,
  height: 600,
  title: "Mi menú"
};
```

Nota que multiplyNumeric no necesita devolver nada. Debe modificar el objeto en su lugar.

P.D. Usa typeof para verificar si hay un número aquí.



 ### Solución:



```javascript
 function multiplyNumeric(obj) {
  for (let key in obj) {
    if (typeof obj[key] === 'number') {
      obj[key] *= 2;
    }
  }
}
```

# Referencias de objetos y copias {.objetos-heading}

Una de las diferencias fundamentales entre objetos y primitivos es que los objetos son

almacenados y copiados “por referencia”, en cambio los primitivos: strings, number, boolean, etc.; son asignados y copiados “como un valor completo”.

Esto es fácil de entender si miramos un poco “bajo cubierta” de lo que pasa cuando copiamos por valor. Empecemos por un primitivo como string. Aquí ponemos una copia de message en phrase:

![](imagenes/UD23%20-%20Objetos_32.jpg)

Una variable no almacena el objeto mismo sino su “dirección en memoria”, en otras palabras “una referencia” a él. Veamos un ejemplo de tal variable:

![](imagenes/UD23%20-%20Objetos_33.png)

El objeto es almacenado en algún lugar de la memoria (a la derecha de la imagen), mientras que la variable user (a la izquierda) tiene una “referencia” a él.

Podemos pensar de una variable objeto, como user, como una hoja de papel con la dirección del objeto escrita en ella.

Cuando ejecutamos acciones con el objeto, por ejemplo, tomar una propiedad user.name, el motor JavaScript busca aquella dirección y ejecuta la operación en el objeto mismo.

Ahora, por qué esto es importante. Cuando una variable de objeto es copiada, se copia solo la referencia. El objeto no es duplicado. Por ejemplo:

![](imagenes/UD23%20-%20Objetos_34.jpg)

Como puedes ver, aún hay un objeto, ahora con dos variables haciendo referencia a él. Podemos usar cualquiera de las variables para acceder al objeto y modificar su contenido:

![](imagenes/UD23%20-%20Objetos_35.jpg)

Es como si tuviéramos un gabinete con dos llaves y usáramos una de ellas (admin) para acceder a él y hacer cambios. Si más tarde usamos la llave (user), estaríamos abriendo el mismo gabinete y accediendo al contenido cambiado.

## Comparación por referencia {.objetos-heading}

Dos objetos son iguales solamente si ellos son el mismo objeto.

Por ejemplo, aquí a y b tienen referencias al mismo objeto, por lo tanto son iguales:

![](imagenes/UD23%20-%20Objetos_36.jpg)

Y aquí dos objetos independientes no son iguales, aunque se vean iguales (ambos están vacíos):

![](imagenes/UD23%20-%20Objetos_37.png)

Para comparaciones como obj1 > obj2, o comparaciones contra un primitivo obj == 5, los objetos son convertidos a primitivos. Estudiaremos cómo funciona la conversión de objetos pronto, pero a decir verdad tales comparaciones ocurren raramente y suelen ser errores de código.

### NOTA: Un efecto importante de almacenar objetos como referencias es que un objeto declarado como const puede ser modificado. 

## Clonación y mezcla, Object.assign {.objetos-heading}

Entonces copiar una variable de objeto crea una referencia adicional al mismo objeto. Podemos crear un nuevo objeto y replicar la estructura del existente iterando a través de sus propiedades y copiándolas en el nivel primitivo. Como esto:

![](imagenes/UD23%20-%20Objetos_38.jpg)

También podemos usar el método Object.assign. La sintaxis es:

![](imagenes/UD23%20-%20Objetos_39.png)

El primer argumento dest es el objeto destinatario.

Los argumentos que siguen son una lista de objetos fuentes.

Esto copia las propiedades de todos los objetos fuentes dentro del destino dest y lo devuelve como resultado. Por ejemplo, tenemos el objeto user, agreguemos un par de permisos:

![](imagenes/UD23%20-%20Objetos_40.jpg)

Si la propiedad por copiar ya existe, se sobrescribe:

![](imagenes/UD23%20-%20Objetos_41.png)

También podemos usar Object.assign para hacer una clonación simple:

![](imagenes/UD23%20-%20Objetos_42.png)

Aquí, copia todas las propiedades de user en un objeto vacío y lo devuelve. También hay otras formas de clonar un objeto, por ejemplo, usando la sintaxis spread clone = {...user}, cubierto más adelante en el tutorial.

## Clonación anidada {.objetos-heading}

Hasta ahora supusimos que todas las propiedades de user eran primitivas. Pero las propiedades pueden ser referencias a otros objetos. Como esto:

![](imagenes/UD23%20-%20Objetos_43.png)

Ahora no es suficiente copiar clone.sizes = user.sizes, porque user.sizes es un objeto y será copiado por referencia. Entonces clone y user compartirán las mismas tallas (.sizes):

![](imagenes/UD23%20-%20Objetos_44.jpg)

Para corregir esto, debemos hacer que user y clone sean objetos completamente separados, debemos usar un bucle que examine cada valor de user[key] y, si es un objeto, que replique su estructura también. Esto es conocido como “clonación profunda” o “clonación estructurada”. Existe un método structuredClone que implementa tal clonación profunda.

La  llamada  a  structuredClone(object)  clona  el object  con todas sus propiedadas  anidadas. Podemos usarlo en nuestro ejemplo:

![](imagenes/UD23%20-%20Objetos_45.jpg)

El método structuredClone puede clonar la mayoría de los tipos de datos, como objetos, arrays, valores primitivos. También soporta referencias circulares, cuando una propiedad de objeto referencia el objeto mismo (directamente o por una cadena de referencias). Por ejemplo:

![](imagenes/UD23%20-%20Objetos_46.png)

Como puedes ver, clone.me hace referencia a clone, no a user! Así que la referencia circular fue clonada correctamente también. Pero hay casos en que structuredClone falla. Por ejemplo, cuando un objeto tiene una propiedad “function”:

![](imagenes/UD23%20-%20Objetos_47.png)

Las propiedades de función no están soportadas. Para manejar estos casos complejos podemos necesitar una combinación de métodos de clonación, escribir código personalizado o, para no reinventar la rueda, tomar una implementación existente, por ejemplo _.cloneDeep(obj) de la librería JavaScript lodash.

## RESUMEN {.objetos-heading}

Los objetos son asignados y copiados por referencia. En otras palabras, una variable almacena no el valor del objeto sino una referencia (la dirección en la memoria) del valor. Entonces, copiar tal variable o pasarla como argumento de función copia la referencia, no el objeto.

Todas las operaciones a través de referencias copiadas (como agregar y borrar propiedades) son efectuadas en el mismo y único objeto.

Para hacer una “verdadera copia” (un clon), podemos usar  Object.assing  para la denominada “clonación superficial” (los objetos anidados son copiados por referencia), o la función de “clonación profunda” structuredClone o usar una implementación personalizada como   _[.cloneDeep(obj)](https://lodash.com/docs#cloneDeep)_  .

# Método del objeto “this” {.objetos-heading}
Los objetos son creados usualmente para representar entidades del mundo real, como usuarios, órdenes, etc.:

![](imagenes/UD23%20-%20Objetos_48.png)

Las acciones son representadas en JavaScript por funciones en las propiedades. Ejemplos de métodos: Para empezar, enseñemos al usuario user a decir hola:

![](imagenes/UD23%20-%20Objetos_49.png)

Aquí simplemente usamos una expresión de función para crear la función y asignarla a la propiedad user.sayHi del objeto. Entonces la llamamos con user.sayHi().

Una función que es la propiedad de un objeto es denominada su método. Así, aquí tenemos un método sayHi del objeto user. Por supuesto, podríamos usar una función pre-declarada como un método, parecido a esto:

![](imagenes/UD23%20-%20Objetos_50.png)

## Formas abreviadas para los métodos {.objetos-heading}

Existe una sintaxis más corta para los métodos en objetos literales:

![](imagenes/UD23%20-%20Objetos_51.jpg)

Como se demostró, podemos omitir "function" y simplemente escribir sayHi(). A decir verdad, las notaciones no son completamente idénticas. Hay diferencias sutiles relacionadas a la herencia de objetos (por cubrir más adelante) que por ahora no son relevantes. En casi todos los casos la sintaxis abreviada es la preferida.

## “this” en métodos {.objetos-heading}

Es común que un método de objeto necesite acceder a la información almacenada en el objeto para cumplir su tarea. Por ejemplo, el código dentro de user.sayHi() puede necesitar el nombre del usuario user.

Para acceder al objeto, un método puede usar la palabra clave this. El valor de this es el objeto “antes del punto”, el usado para llamar al método. Por ejemplo:

![](imagenes/UD23%20-%20Objetos_52.png)

Aquí durante la ejecución de user.sayHi(), el valor de this será user. Técnicamente, también es posible acceder al objeto sin this, haciendo referencia a él por medio de la variable externa:

![](imagenes/UD23%20-%20Objetos_53.png)

…Pero tal código no es confiable. Si decidimos copiar user a otra variable, por ejemplo admin = user y sobrescribir user con otra cosa, entonces accederá al objeto incorrecto. Eso queda demostrado en las siguientes lineas:

![](imagenes/UD23%20-%20Objetos_54.jpg)

Si usamos this.name en vez de user.name dentro de alert, entonces el código funciona.

## “this” no es vinculado {.objetos-heading}

En JavaScript, la palabra clave this se comporta de manera distinta a la mayoría de otros lenguajes de programación. Puede ser usado en cualquier función, incluso si no es el método de un objeto. No hay error de sintaxis en el siguiente ejemplo:

![](imagenes/UD23%20-%20Objetos_55.png)

El valor de this es evaluado durante el tiempo de ejecución, dependiendo del contexto. Por ejemplo, aquí la función es asignada a dos objetos diferentes y tiene diferentes “this” en sus llamados:

![](imagenes/UD23%20-%20Objetos_56.jpg)

La regla es simple: si obj.f() es llamado, entonces this es obj durante el llamado de f. Entonces es tanto user o admin en el ejemplo anterior.

## Las funciones de flecha no tienen “this” {.objetos-heading}

Las funciones de flecha son especiales: ellas no tienen su “propio” this. Si nosotros hacemos referencia a this desde tales funciones, esta será tomada desde afuera de la función “normal”. Por ejemplo, aquí arrow() usa this desde fuera del método user.sayHi():

![](imagenes/UD23%20-%20Objetos_57.png)

Esto es una característica especial de las funciones de flecha, útil cuando no queremos realmente un this separado sino tomarlo de un contexto externo. Más adelante en el capítulo Funciones de flecha revisadas las trataremos en profundidad.

## RESUMEN {.objetos-heading}

* Las funciones que son almacenadas en propiedades de objeto son llamadas“métodos”.
  * Los método permiten a los objetos “actuar”, como object.doSomething().
  *   Los métodos pueden hacer referencia al objeto con this.
* El valor de this es definido en tiempo de ejecución.
* Cuando una función es declarada, puede usar this, pero ese this no tiene valor hasta que la función es llamada.
* Una función puede ser copiada entre objetos.
* Cuando una función es llamada en la sintaxis de método: object.method(),  el valor this durante el llamado es object.
* Tened en cuenta que las funciones de flecha son especiales: ellas no tienen this. Cuando this es accedido dentro de una función de flecha, su valor es tomado desde el exterior.


# TAREAS {.objetos-heading}

## Usando el "this" en un objeto literal {.objetos-heading}

Aquí la función makeUser devuelve un objeto.

¿Cuál es el resultado de acceder a su ref? ¿Por qué?

```javascript
function makeUser() {
  return {
    name: "John",
    ref: this
  };
}
let user = makeUser();
alert( user.ref.name ); // ¿Cuál es el resultado?
```


## Solución:

El resultado de ejecutar este código es un error (específicamente un TypeError: Cannot read properties of undefined (reading 'name')) si se ejecuta en modo estricto ('use strict'), que es el comportamiento por defecto en los entornos modernos de JavaScript (como los módulos de ES6).

¿Por qué ocurre esto?
El valor de this:
La función makeUser() se está llamando como una función normal (makeUser()), y no como un método de un objeto (es decir, no se llama como algo.makeUser()).

En una llamada de función normal en modo estricto, el valor de this es undefined.

(Nota: Si estuviera en modo no estricto o "sloppy mode", this apuntaría al objeto global, que es window en el navegador, por lo que user.ref sería window y user.ref.name devolvería una cadena vacía "").

1. Evaluación del objeto:
Al crearse el objeto dentro de makeUser:
```javascript

return {
  name: "John",
  ref: this // 'this' es undefined
};
```

2. La propiedad ref toma el valor de this, que es undefined. Por lo tanto, el objeto user resultante es:

```javascript
{
  name: "John",
  ref: undefined
}
```
3. El acceso a la propiedad:
Cuando intentas ejecutar user.ref.name, en realidad estás intentando hacer undefined.name, lo cual provoca un error en JavaScript porque no se pueden leer propiedades de undefined.


## Crea una calculadora {.objetos-heading}

Crea un objeto calculator con tres métodos:

read() pide dos valores y los almacena como propiedades de objeto con

nombres a y b.

sum() devuelve la suma de los valores almacenados.

mul() multiplica los valores almacenados y devuelve el resultado.

```javascript
let calculator = {
  // ... tu código ...
};
calculator.read();
alert( calculator.sum() );
alert( calculator.mul() );
```

 _[Ejecutar](https://es.javascript.info/object-methods)_  _[ ](https://es.javascript.info/object-methods)_  _[el](https://es.javascript.info/object-methods)_  _[ ](https://es.javascript.info/object-methods)_  _[demo](https://es.javascript.info/object-methods)_ 

 _[Abrir](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_  _[ ](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_  _[en](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_  _[ ](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_  _[entorno](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_  _[ ](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_  _[controlado](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_  _[ ](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_  _[con](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_  _[ ](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_  _[pruebas.](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ 

## Encadenamiento {.objetos-heading}

Hay un objeto ladder que permite subir y bajar:

```javascript
let ladder = {
  step: 0,
  up() {
    this.step++;
  },
  down() {
    this.step--;
  },
  showStep() {
    // muestra el peldaño actual
    alert(this.step);
  }
};
```

Ahora, si necesitamos hacer varios llamados en secuencia podemos hacer algo como esto:

```javascript
ladder.up();
ladder.up();
ladder.down();
ladder.showStep(); // 1
ladder.down();
ladder.showStep(); // 0
```

Modifica el código de “arriba” up, “abajo” down y “mostrar peldaño” showStep para hacer los llamados encadenables como esto:

```javascript
ladder.up().up().down().showStep().down().showStep(); // muestra 1 y luego 0
```

Tal enfoque es ampliamente usado entre las librerías JavaScript.

 _[Abrir](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_  _[ ](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_  _[en](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_  _[ ](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_  _[entorno](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_  _[ ](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_  _[controlado](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_  _[ ](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_  _[con](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_  _[ ](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_  _[pruebas.](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ 


## Solución:

Para conseguir que los métodos sean encadenables (lo que se conoce como method chaining), cada uno de los métodos (up, down y showStep) debe devolver el propio objeto this al final de su ejecución.

Aquí tienes el objeto ladder modificado:

```javascript

let ladder = {
  step: 0,
  up() {
    this.step++;
    return this; // Devuelve el objeto para permitir el encadenamiento
  },
  down() {
    this.step--;
    return this; // Devuelve el objeto para permitir el encadenamiento
  },
  showStep() {
    alert(this.step);
    return this; // Devuelve el objeto para permitir el encadenamiento
  }
};

// Ahora ya puedes encadenar las llamadas:
ladder.up().up().down().showStep().down().showStep(); // Muestra 1 y luego 0
```

# Constructor, operador “new” {.objetos-heading}

La sintaxis habitual {...} nos permite crear un objeto. Pero a menudo necesitamos crear varios objetos similares, como múltiples usuarios, elementos de menú, etcétera.

Esto se puede realizar utilizando el constructor de funciones y el operador "new".

## Función constructora {.objetos-heading}

La función constructora es técnicamente una función normal. Aunque hay dos convenciones:

Son nombradas con la primera letra mayúscula.

Sólo deben ejecutarse con el operador "new".

Por ejemplo:

![](imagenes/UD23%20-%20Objetos_58.png)

Cuando una función es ejecutada con new, realiza los siguientes pasos:

Se crea un nuevo objeto vacío y se asigna a this.

Se ejecuta el cuerpo de la función. Normalmente se modifica this y se le agrega nuevas propiedades.

Se devuelve el valor de this.

En otras palabras, new User(...) realiza algo como:

![](imagenes/UD23%20-%20Objetos_59.png)

Entonces let user = new User("Jack") da el mismo resultado que:

![](imagenes/UD23%20-%20Objetos_60.png)

Ahora si queremos crear otros usuarios, podemos llamar a new User("Ann"), new User("Alice"), etcétera. Mucho más corto que usar literales todo el tiempo y también fácil de leer.

Este es el principal propósito del constructor – implementar código de creación de objetos re-utilizables.

Tomemos nota otra vez: técnicamente cualquier función (excepto las de flecha pues no tienen this) puede ser utilizada como constructor. Puede ser llamada con new, y ejecutará el algoritmo de arriba. La “primera letra mayúscula” es un acuerdo general, para dejar en claro que la función debe ser ejecutada con new.

Dentro de una función, podemos verificar si ha sido llamada con o sin el new utilizando una propiedad especial: new.target.

En las llamadas normales devuelve undefined, y cuando es llamada con new devuelve la función:

![](imagenes/UD23%20-%20Objetos_61.png)

Esto puede ser utilizado dentro de la función para conocer si ha sido llamada con new, "en modo constructor "; o sin él, “en modo regular”.

También podemos hacer que ambas formas de llamarla, con new y “regular”, realicen lo mismo:

![](imagenes/UD23%20-%20Objetos_62.jpg)

Este enfoque es utilizado a veces en las librerías para hacer la sintaxis más flexible. Así la gente puede llamar a la función con o sin new y aún funciona.

Sin embargo, probablemente no sea algo bueno para usar en todas partes, porque omitir new hace que sea un poco menos obvio lo que está sucediendo. Con new todos sabemos que se está creando el nuevo objeto.

## Return desde constructores {.objetos-heading}

Normalmente, los constructores no tienen una sentencia return. Su tarea es escribir todo lo necesario al this, y automáticamente este se convierte en el resultado.

Pero si hay una sentencia return, entonces la regla es simple:

Si return es llamado con un objeto, entonces se devuelve tal objeto en vez de this.

Si return es llamado con un tipo de dato primitivo, es ignorado.

En otras palabras, return con un objeto devuelve ese objeto, en todos los demás casos se devuelve this. Por ejemplo, aquí return anula this al devolver un objeto:

![](imagenes/UD23%20-%20Objetos_63.jpg)

Y aquí un ejemplo con un return vacío (o podemos colocar un primitivo después de él, no importa):

![](imagenes/UD23%20-%20Objetos_64.png)

Normalmente	los  constructores  no  tienen  una  sentencia  return.  Aquí  mencionamos  el comportamiento especial con devolución de objetos principalmente por el bien de la integridad.

## Métodos en constructor {.objetos-heading}

Utilizar constructor de funciones para crear objetos nos da mucha flexibilidad. La función constructora puede tener argumentos que definan cómo construir el objeto y qué colocar dentro.

Por supuesto podemos agregar a this no sólo propiedades, sino también métodos. Por ejemplo, new User(name) de abajo, crea un objeto con el name dado y el método sayHi:

![](imagenes/UD23%20-%20Objetos_65.png)

Para crear objetos complejos existe una sintaxis más avanzada, classes.

## RESUMEN {.objetos-heading}

Las funciones Constructoras o, más corto, constructores, son funciones normales, pero existe un común acuerdo para nombrarlas con la primera letra en mayúscula.

Las funciones Constructoras sólo deben ser llamadas utilizando new. Tal llamado implica la creación de un this vacío al comienzo y devolver el this rellenado al final.

Podemos utilizar funciones constructoras para crear múltiples objetos similares.

JavaScript proporciona funciones constructoras para varios objetos de lenguaje incorporados: como Date para fechas, Set para conjuntos y otros que planeamos estudiar.

# TAREAS {.objetos-heading}

## Crear nueva Calculadora {.objetos-heading}

Crear una función constructora Calculator que crea objetos con 3 métodos:

read() pide dos valores usando prompt y los guarda en las propiedades del objeto con los nombres a y b.

sum() devuelve la suma de estas propiedades.

mul() devuelve el producto de la multiplicación de estas propiedades.

Por ejemplo:

```javascript
let calculator = new Calculator();
calculator.read();
alert("Sum=" + calculator.sum());
alert("Mul=" + calculator.mul());
```

 _[Ejecutar](https://es.javascript.info/constructor-new)_  _[ ](https://es.javascript.info/constructor-new)_  _[el](https://es.javascript.info/constructor-new)_  _[ ](https://es.javascript.info/constructor-new)_  _[demo](https://es.javascript.info/constructor-new)_ 

 _[Abrir](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_  _[ ](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_  _[en](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_  _[ ](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_  _[entorno](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_  _[ ](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_  _[controlado](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_  _[ ](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_  _[con](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_  _[ ](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_  _[pruebas.](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ 

## Crear nuevo Acumulador {.objetos-heading}

Crear una función constructor Accumulator(startingValue).

El objeto que crea debería:

Almacene el “valor actual” en la propiedad value. El valor inicial se establece en el argumento del constructor startingValue.

El método read() debe usar prompt para leer un nuevo número y agregarlo a value.

En otras palabras, la propiedad value es la suma de todos los valores ingresados por el usuario con el valor inicial startingValue.

Aquí está la demostración del código:

```javascript
let accumulator = new Accumulator(1); // valor inicial 1
accumulator.read(); // agrega el valor introducido por el usuario
accumulator.read(); // agrega el valor introducido por el usuario
alert(accumulator.value); // muestra la suma de estos valores
```

 _[Ejecutar](https://es.javascript.info/constructor-new)_  _[ ](https://es.javascript.info/constructor-new)_  _[el](https://es.javascript.info/constructor-new)_  _[ ](https://es.javascript.info/constructor-new)_  _[demo](https://es.javascript.info/constructor-new)_ 

 _[Abrir](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_  _[ ](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_  _[en](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_  _[ ](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_  _[entorno](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_  _[ ](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_  _[controlado](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_  _[ ](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_  _[con](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_  _[ ](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_  _[pruebas.](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ 

# Encadenamiento opcional '?.' {.objetos-heading}

_Esta es una adición reciente al lenguaje. Los navegadores antiguos pueden necesitar polyfills._

El encadenamiento opcional ?. es una forma a prueba de errores para acceder a las propiedades anidadas de los objetos, incluso si no existe una propiedad intermedia.

## El problema de la propiedad que no existe {.objetos-heading}

Si acaba de comenzar a leer el tutorial y aprender JavaScript, quizás el problema aún no lo haya tocado, pero es bastante común. Como ejemplo, digamos que tenemos objetos user que contienen información de nuestros usuarios. La mayoría de nuestros usuarios tienen la dirección en  la  propiedad  user.address,  con  la  calle  en  user.address.street,  pero  algunos  no  la proporcionaron.

En  tal  caso,  cuando  intentamos  obtener  user.address.streeten  un  usuario  sin  dirección obtendremos un error:

![](imagenes/UD23%20-%20Objetos_66.png)

Este es el resultado esperado. JavaScript funciona así, como user.address es undefined, el intento de obtener user.address.street falla dando un error.

En muchos casos prácticos preferiríamos obtener undefined en lugar del error (dando a entender “sin calle”)

… y otro ejemplo. En desarrollo web, podemos obtener un objeto que corresponde a un elemento   de   página   web   usando   el   llamado   a   un   método   especial   como document.querySelector('.elem'), que devuelve null cuando no existe tal elemento.

![](imagenes/UD23%20-%20Objetos_67.jpg)

Una vez más, si el elemento no existe, obtendremos un error al intentar acceder a la propiedad

.innerHTML de null. Y en algunos casos, cuando la ausencia del elemento es normal, quisiéramos evitar el error y simplemente aceptar html = null como resultado.

¿Cómo podemos hacer esto? La solución obvia sería chequear el valor usando if o el operador condicional? antes de usar la propiedad:

![](imagenes/UD23%20-%20Objetos_68.jpg)

Esto funciona, no hay error… Pero es bastante poco elegante. Como puedes ver, "user.address" aparece   dos   veces   en   el   código.   El   mismo   caso,   pero   con   la   búsqueda   de document.querySelector:

```javascript
let html = document.querySelector('.elem')
  ? document.querySelector('.elem').innerHTML
  : null;
```

Podemos ver que el elemento de búsqueda document.querySelector('.elem') es llamado dos veces aquí. En propiedades anidadas más profundamente, esto se vuelve un problema porque se requerirán más repeticiones.

Ejemplo: Tratemos de obtener user.address.street.name de manera similar.

![](imagenes/UD23%20-%20Objetos_69.jpg)

Esto es horrible, podemos tener problemas para siquiera entender tal código. Hay una mejor manera de escribirlo, usando el operador &&:

![](imagenes/UD23%20-%20Objetos_70.jpg)

Poniendo AND en el camino completo a la propiedad asegura que todos los componentes existen (si no, la evaluación se detiene), pero no es lo ideal.

Como puedes ver, los nombres de propiedad aún están duplicados en el código. Por ejemplo en el código de arriba user.address aparece tres veces. Es por ello que el encadenamiento opcional ?. fue agregado al lenguaje.

## Encadenamiento opcional {.objetos-heading}

El encadenamiento opcional ?. detiene la evaluación y devuelve undefined si el valor antes del

?. es undefined o null.

__De aquí en adelante en este artículo, por brevedad, diremos que algo “existe” si no es null o undefined.__

En otras palabras, value?.prop:

funciona como value.prop si value existe,

de otro modo (cuando value es undefined/null) devuelve undefined.

Aquí está la forma segura de acceder a user.address.street usando ?.:

![](imagenes/UD23%20-%20Objetos_71.jpg)

El código es corto y claro, no hay duplicación en absoluto. Aquí tenemos un ejemplo con document.querySelector:

![](imagenes/UD23%20-%20Objetos_72.jpg)

Leer la dirección con user?.Address funciona incluso si el objeto user no existe:

![](imagenes/UD23%20-%20Objetos_73.png)

Tenga en cuenta: la sintaxis ?. hace opcional el valor delante de él, pero no más allá.

Por ejemplo, en user?.address.street.name, el ?. permite que user sea null/undefined (y devuelve undefined en tal caso), pero solo a user. El resto de las propiedades son accedidas de la manera normal. Si queremos que algunas de ellas sean opcionales, necesitamos reemplazar más . con ?..

__NOTA:  Si  por  ejemplo  no  hay  una  variable  user  declarada  previamente,  entonces user?.anything provocará un error.__

## Short-circuiting (Cortocircuitos) {.objetos-heading}

Como se dijo antes, el ?. detiene inmediatamente (“cortocircuito”) la evaluación si la parte izquierda no existe. Entonces, si a la derecha de ?. hay funciones u operaciones adicionales, estas no se ejecutarán. Por ejemplo:

![](imagenes/UD23%20-%20Objetos_74.jpg)

## Otros casos: ?.(), ?.[] {.objetos-heading}

El encadenamiento opcional ?. no es un operador, es una construcción de sintaxis especial que también funciona con funciones y corchetes. Por ejemplo, ?.() se usa para llamar a una función que puede no existir.

En el siguiente código, algunos de nuestros usuarios tienen el método admin, y otros no:

![](imagenes/UD23%20-%20Objetos_75.jpg)

Aquí, en ambas líneas, primero usamos el punto (userAdmin.admin) para obtener la propiedad admin, porque asumimos que el objeto user existe y es seguro leerlo.

Entonces ?.() comprueba la parte izquierda: si la función admin existe, entonces se ejecuta (para userAdmin). De lo contrario (para userGuest) la evaluación se detiene sin errores.

La sintaxis ?.[] también funciona si quisiéramos usar corchetes [] para acceder a las propiedades en lugar de punto .. Al igual que en casos anteriores, permite leer de forma segura una propiedad de un objeto que puede no existir.

![](imagenes/UD23%20-%20Objetos_76.png)

También podemos usar ?. con delete:

![](imagenes/UD23%20-%20Objetos_77.jpg)

## RESUMEN {.objetos-heading}

La sintaxis de encadenamiento opcional ?. tiene tres formas:

obj?.prop – devuelve obj.prop si obj existe, si no, undefined.

obj?.[prop] – devuelve obj[prop] si obj existe, si no, undefined.

obj.method?.() – llama a obj.method() si obj.method existe, si no devuelve undefined.

Como podemos ver, todos ellos son sencillos y fáciles de usar. El ?. comprueba   si la parte izquierda es null/undefined y permite que la evaluación continúe si no es así.

Una cadena de ?. permite acceder de forma segura a las propiedades anidadas.

Aun así, debemos aplicar ?. con cuidado, solamente donde sea aceptable     que, de acuerdo con nuestra lógica, la parte izquierda no exista. Esto es para que no nos oculte errores de programación, si ocurren.
