# INTRODUCCION A OBJETOS EN JAVASCRIPT
2º DAW - Desarrollo Web en Entorno Cliente

# ¿Qué son objetos básicos?

<span style="color:#a42f0f">\- </span>  <span style="color:#404040">Los</span>  <span style="color:#404040"> </span>  <span style="color:#404040">objetos</span>  <span style="color:#404040"> </span>  <span style="color:#404040">son</span>  <span style="color:#404040"> </span>  <span style="color:#404040">usados</span>  <span style="color:#404040"> </span>  <span style="color:#404040">para</span>  <span style="color:#404040"> </span>  <span style="color:#404040">almacenar</span>  <span style="color:#404040"> </span>  <span style="color:#404040">colecciones</span>  <span style="color:#404040"> </span>  <span style="color:#404040">de</span>  <span style="color:#404040"> </span>  <span style="color:#404040">varios</span>  <span style="color:#404040"> datos</span>  <span style="color:#404040"> </span>  <span style="color:#404040">y</span>  <span style="color:#404040"> </span>  <span style="color:#404040">entidades</span>  <span style="color:#404040"> </span>  <span style="color:#404040">más</span>  <span style="color:#404040"> </span>  <span style="color:#404040">complejas</span>  <span style="color:#404040"> </span>  <span style="color:#404040">asociados</span>  <span style="color:#404040"> </span>  <span style="color:#404040">con</span>  <span style="color:#404040"> </span>  <span style="color:#404040">un</span>  <span style="color:#404040"> </span>  <span style="color:#404040">nombre</span>  <span style="color:#404040"> clave\.</span>  <span style="color:#404040"> </span>  <span style="color:#404040">En</span>  <span style="color:#404040"> </span>  <span style="color:#404040">JavaScript\,</span>  <span style="color:#404040"> </span>  <span style="color:#404040">los</span>  <span style="color:#404040"> </span>  <span style="color:#404040">objetos</span>  <span style="color:#404040"> </span>  <span style="color:#404040">penetran</span>  <span style="color:#404040"> </span>  <span style="color:#404040">casi</span>  <span style="color:#404040"> </span>  <span style="color:#404040">todos</span>  <span style="color:#404040"> </span>  <span style="color:#404040">los</span>  <span style="color:#404040"> </span>  <span style="color:#404040">aspectos</span>  <span style="color:#404040"> </span>  <span style="color:#404040">del</span>  <span style="color:#404040"> </span>  <span style="color:#404040">lenguaje\.</span>  <span style="color:#404040"> </span>  <span style="color:#404040">Por</span>  <span style="color:#404040"> </span>  <span style="color:#404040">lo</span>  <span style="color:#404040"> </span>  <span style="color:#404040">tanto\,</span>  <span style="color:#404040"> </span>  <span style="color:#404040">debemos</span>  <span style="color:#404040"> </span>  <span style="color:#404040">comprenderlos</span>  <span style="color:#404040"> </span>  <span style="color:#404040">primero</span>  <span style="color:#404040"> </span>  <span style="color:#404040">antes</span>  <span style="color:#404040"> </span>  <span style="color:#404040">de</span>  <span style="color:#404040"> </span>  <span style="color:#404040">profundizar</span>  <span style="color:#404040"> </span>  <span style="color:#404040">en</span>  <span style="color:#404040"> </span>  <span style="color:#404040">cualquier</span>  <span style="color:#404040"> </span>  <span style="color:#404040">otro </span>  <span style="color:#404040">lugar\.</span>

<span style="color:#404040">Podemo</span>  <span style="color:#404040">s</span>  <span style="color:#404040"> </span>  <span style="color:#404040">crear</span>  <span style="color:#404040"> </span>  <span style="color:#404040">un</span>  <span style="color:#404040"> </span>  <span style="color:#404040">objeto</span>  <span style="color:#404040"> </span>  <span style="color:#404040">usando</span>  <span style="color:#404040"> </span>  <span style="color:#404040">las</span>  <span style="color:#404040"> </span>  <span style="color:#404040">llaves</span>  <span style="color:#404040"> </span>  <span style="color:#404040">\{…\}</span>  <span style="color:#404040"> </span>  <span style="color:#404040">con</span>  <span style="color:#404040"> </span>  <span style="color:#404040">una</span>  <span style="color:#404040"> </span>  <span style="color:#404040">lista</span>  <span style="color:#404040"> </span>  <span style="color:#404040">opcional</span>  <span style="color:#404040"> </span>  <span style="color:#404040">de</span>  <span style="color:#404040"> </span>  <span style="color:#404040">propiedades\.</span>  <span style="color:#404040"> </span>  <span style="color:#404040">Una</span>  <span style="color:#404040"> </span>  <span style="color:#404040">propiedad</span>  <span style="color:#404040"> </span>  <span style="color:#404040">es</span>  <span style="color:#404040"> </span>  <span style="color:#404040">un</span>  <span style="color:#404040"> </span>  <span style="color:#404040">par</span>  <span style="color:#404040"> </span>  <span style="color:#404040">“key:value”\,</span>  <span style="color:#404040"> </span>  <span style="color:#404040">donde</span>  <span style="color:#404040"> </span>  <span style="color:#404040">key</span>  <span style="color:#404040"> </span>  <span style="color:#404040">es</span>  <span style="color:#404040"> </span>  <span style="color:#404040">un</span>  <span style="color:#404040"> </span>  <span style="color:#404040">string</span>  <span style="color:#404040"> </span>  <span style="color:#404040">\(también</span>  <span style="color:#404040"> </span>  <span style="color:#404040">llamado</span>  <span style="color:#404040"> </span>  <span style="color:#404040">“nombre</span>  <span style="color:#404040"> </span>  <span style="color:#404040">clave”\)\,</span>  <span style="color:#404040"> </span>  <span style="color:#404040">y</span>  <span style="color:#404040"> </span>  <span style="color:#404040">value</span>  <span style="color:#404040"> </span>  <span style="color:#404040">puede</span>  <span style="color:#404040"> </span>  <span style="color:#404040">ser</span>  <span style="color:#404040"> </span>  <span style="color:#404040">cualquier</span>  <span style="color:#404040"> </span>  <span style="color:#404040">cosa</span>  <span style="color:#404040">\.</span>

<span style="color:#404040">Se</span>  <span style="color:#404040"> </span>  <span style="color:#404040">puede</span>  <span style="color:#404040"> </span>  <span style="color:#404040">crear</span>  <span style="color:#404040"> </span>  <span style="color:#404040">un</span>  <span style="color:#404040"> </span>  <span style="color:#404040">objeto</span>  <span style="color:#404040"> </span>  <span style="color:#404040">vacío</span>  <span style="color:#404040"> </span>  <span style="color:#404040">\(“gabinete</span>  <span style="color:#404040"> </span>  <span style="color:#404040">vacío”\)</span>  <span style="color:#404040"> </span>  <span style="color:#404040">utilizando</span>  <span style="color:#404040"> </span>  <span style="color:#404040">una</span>  <span style="color:#404040"> </span>  <span style="color:#404040">de </span>  <span style="color:#404040">las</span>  <span style="color:#404040"> dos </span>  <span style="color:#404040">sintaxis</span>  <span style="color:#404040"> </span>  <span style="color:#404040">\(Normalmente</span>  <span style="color:#404040"> </span>  <span style="color:#404040">se</span>  <span style="color:#404040"> </span>  <span style="color:#404040">utilizan</span>  <span style="color:#404040"> </span>  <span style="color:#404040">las</span>  <span style="color:#404040"> </span>  <span style="color:#404040">llaves</span>  <span style="color:#404040"> </span>  <span style="color:#404040">\{\.\.\.\}\.</span>  <span style="color:#404040"> </span>  <span style="color:#404040"> </span>  <span style="color:#404040">Esa</span>  <span style="color:#404040"> </span>  <span style="color:#404040">declaración</span>  <span style="color:#404040"> </span>  <span style="color:#404040">se</span>  <span style="color:#404040"> </span>  <span style="color:#404040">llama</span>  <span style="color:#404040"> </span>  <span style="color:#404040">objeto</span>  <span style="color:#404040"> literal\):</span>

![](imagenes%5CUD23%20-%20Objetos_0.jpg)

_Literales y propiedades_

Podemos poner inmediatamente algunas propiedades dentro de \{\.\.\.\} como pares “clave:valor”:

![](imagenes%5CUD23%20-%20Objetos_1.jpg)

Una propiedad tiene una clave \(también conocida como “nombre” o “identificador”\) antes de los dos puntos ":" y un valor a la derecha\. En el objeto user hay dos propiedades:

La primera propiedad tiene la clave "name" y el valor "John"\.

La segunda tienen la clave "age" y el valor 30\.

Podemos imaginar al objeto user resultante como un gabinete con dos archivos firmados con las etiquetas “name” y “age”\.

![](imagenes%5CUD23%20-%20Objetos_2.png)

Podemos agregar\, eliminar y leer archivos de él en cualquier momento\.

Se puede acceder a los valores de las propiedades utilizando la notación de punto:

![](imagenes%5CUD23%20-%20Objetos_3.jpg)

El valor puede ser de cualquier tipo\. Agreguemos uno booleano:

![](imagenes%5CUD23%20-%20Objetos_4.png)

Para eliminar una propiedad podemos usar el operador delete:

![](imagenes%5CUD23%20-%20Objetos_5.png)

También podemos nombrar propiedades con más de una palabra\. Pero\, de ser así\, debemos colocar la clave entre comillas "\.\.\.":

![](imagenes%5CUD23%20-%20Objetos_6.png)

La última propiedad en la lista puede terminar con una coma:

![](imagenes%5CUD23%20-%20Objetos_7.png)

Eso se llama una coma “final” o “colgante”\. Facilita agregar\, eliminar y mover propiedades\, porque todas las líneas se vuelven similares\.

La notación de punto no funciona para acceder a propiedades con claves de más de una palabra:

![](imagenes%5CUD23%20-%20Objetos_8.png)

El punto requiere que la clave sea un identificador de variable válido\. Eso implica que: no contenga espacios\, no comience con un dígito y no incluya caracteres especiales \($ y \_ sí se permiten\)\.

Existe una “notación de corchetes” alternativa que funciona con cualquier string:

![](imagenes%5CUD23%20-%20Objetos_9.png)

Ahora todo está bien\. Nota que el string dentro de los corchetes está adecuadamente entre comillas \(cualquier tipo de comillas servirían\)\.

Los corchetes también brindan una forma de obtener el nombre de la propiedad desde el resultado de una expresión \(a diferencia de la cadena literal\)\. Por ejemplo\, a través de una variable:

![](imagenes%5CUD23%20-%20Objetos_10.png)

Aquí la variable key puede calcularse en tiempo de ejecución o depender de la entrada del usuario y luego lo usamos para acceder a la propiedad\. Eso nos da mucha flexibilidad\. Por ejemplo:

![](imagenes%5CUD23%20-%20Objetos_11.jpg)

![](imagenes%5CUD23%20-%20Objetos_12.png)

La notación de punto no puede ser usada de manera similar:

_Propiedades calculadas_

Podemos usar corchetes en un objeto literal al crear un objeto\. A esto se le llama propiedades calculadas\. Por ejemplo:

![](imagenes%5CUD23%20-%20Objetos_13.jpg)

El significado de una propiedad calculada es simple: \[fruit\] significa que se debe tomar la clave de la propiedad fruit\. Entonces\, si un visitante ingresa "apple"\, bag se convertirá en \{apple: 5\}\. Esencialmente esto funciona igual que:

![](imagenes%5CUD23%20-%20Objetos_14.jpg)

Podemos usar expresiones más complejas dentro de los corchetes:

![](imagenes%5CUD23%20-%20Objetos_15.png)

Los corchetes son mucho más potentes que la notación de punto\. Permiten cualquier nombre de propiedad\, incluso variables\. Pero también es más engorroso escribirlos\. Entonces\, la mayoría de las veces\, cuando los nombres de propiedad son conocidos y simples\, se utiliza el punto\. Y si necesitamos algo más complejo\, entonces cambiamos a corchetes\.

_Atajo para valores de propiedad_

En el código real\, a menudo usamos variables existentes como valores de los nombres de propiedades\. Por ejemplo:

![](imagenes%5CUD23%20-%20Objetos_16.png)

En el ejemplo anterior las propiedades tienen los mismos nombres que las variables\. El uso de variables para la creación de propiedades es tán común que existe un atajo para valores de propiedad especial para hacerla más corta\.

En lugar de name:name\, simplemente podemos escribir name\, tal cual:

![](imagenes%5CUD23%20-%20Objetos_17.png)

Podemos usar ambos tipos de notación en un mismo objeto\, la normal y el atajo:

![](imagenes%5CUD23%20-%20Objetos_18.png)

_Limitaciones de nombres de propiedad_

Como sabemos\, una variable no puede tener un nombre igual a una de las palabras reservadas del lenguaje\, como “for”\, “let”\, “return”\, etc\. Pero para una propiedad de objeto no existe tal restricción:

![](imagenes%5CUD23%20-%20Objetos_19.png)

En resumen\, no hay limitaciones en los nombres de propiedades\. Pueden ser cadenas o símbolos \(un tipo especial para identificadores que se cubrirán más adelante\)\. Otros tipos se convierten automáticamente en cadenas\.

Por ejemplo\, un número 0 se convierte en cadena "0" cuando se usa como clave de propiedad:

![](imagenes%5CUD23%20-%20Objetos_20.jpg)

Hay  una  pequeña  sorpresa  por  una  propiedad  especial  llamada  _	_ proto _	_ \.  No  podemos establecerlo dentro de un valor que no sea de objeto:

![](imagenes%5CUD23%20-%20Objetos_21.jpg)

Como podemos ver en el código\, se ignora la asignación de un valor primitivo 5\.

_La prueba de propiedad existente\, el operador “in”_

La lectura de una propiedad no existente solo devuelve undefined\. Así que podemos probar fácilmente si la propiedad existe:

![](imagenes%5CUD23%20-%20Objetos_22.jpg)

También existe un operador especial para ello: "in"\. La sintaxis es:

![](imagenes%5CUD23%20-%20Objetos_23.png)

![](imagenes%5CUD23%20-%20Objetos_24.jpg)

Nota que a la izquierda de in debe estar el nombre de la propiedad que suele ser un string entre comillas\. Si omitimos las comillas\, significa que es una variable\. Esta variable debe almacenar la clave real que será probada\. Por ejemplo:

![](imagenes%5CUD23%20-%20Objetos_25.jpg)

La mayoría de las veces las comparaciones con undefined funcionan bien\. Pero hay un caso especial donde esto falla y aún así "in" funciona correctamente\. Es cuando existe una propiedad de objeto\, pero almacena undefined:

![](imagenes%5CUD23%20-%20Objetos_26.jpg)

En el código anterior\, la propiedad obj\.test técnicamente existe\. Entonces el operador in funciona correctamente\. Situaciones como esta suceden raramente ya que undefined no debe ser explícitamente asignado\. Comúnmente usamos null para valores “desconocidos” o “vacíos”\.

_El bucle "for\.\.in"_

Para recorrer todas las claves de un objeto existe una forma especial de bucle: for\.\.in\. Esto es algo completamente diferente a la construcción for\(;;\) que estudiaremos más adelante\. La sintaxis:

![](imagenes%5CUD23%20-%20Objetos_27.jpg)

Por ejemplo\, mostremos todas las propiedades de user:

![](imagenes%5CUD23%20-%20Objetos_28.png)

Nota que todas las construcciones “for” nos permiten declarar variables para bucle dentro del bucle\, como let key aquí\. A demás podríamos usar otros nombres de variables en lugar de key\. Por ejemplo\, "for \(let prop in obj\)" también se usa bastante\.

_Ordenado como un objeto_

¿Los objetos están ordenados? Es decir\, si creamos un bucle sobre un objeto\, ¿obtenemos todas las propiedades en el mismo orden en el que se agregaron? ¿Podemos confiar en ello?

La respuesta corta es: “ordenados de una forma especial”: las propiedades de números enteros se ordenan\, los demás aparecen en el orden de la creación\. Entremos en detalle\. Como ejemplo\, consideremos un objeto con códigos telefónicos:

![](imagenes%5CUD23%20-%20Objetos_29.png)

El objeto puede usarse para sugerir al usuario una lista de opciones\. Si estamos haciendo un sitio principalmente para el público alemán\, probablemente queremos que 49 sea el primero\.

Pero si ejecutamos el código\, veremos una imagen totalmente diferente:

USA \(1\) va primero

Luego Switzerland \(41\) y así sucesivamente\.

Los códigos telefónicos van en orden ascendente porque son números enteros\. Entonces vemos 1\, 41\, 44\, 49\.

…Por otro lado\, si las claves no son enteras\, se enumeran en el orden de creación\, por ejemplo:

![](imagenes%5CUD23%20-%20Objetos_30.jpg)

Entonces\, para solucionar el problema con los códigos telefónicos\, podemos “hacer trampa” haciendo que los códigos no sean enteros\. Agregar un signo más "\+" antes de cada código será más que suficiente\. Justo así:

![](imagenes%5CUD23%20-%20Objetos_31.png)

# RESUMEN

<span style="color:#404040">Los objetos son arreglos asociativos con varias características especiales\. Almacenan propiedades \(pares   de clave\-valor\)\, donde:</span>

<span style="color:#404040">Las claves de propiedad deben ser cadenas o símbolos \(generalmente strings\)\.</span>

<span style="color:#404040">Los valores pueden ser de cualquier tipo\.</span>

<span style="color:#404040">Para acceder a una propiedad\, podemos usar:</span>

<span style="color:#404040">La notación de punto: obj\.property\.</span>

<span style="color:#404040">La notación de corchetes obj\["property"\]\. Los corchetes permiten tomar la clave de una variable\, como obj\[varWithKey\]\.</span>

<span style="color:#404040">Operadores</span>  <span style="color:#404040"> adicionales:</span>

<span style="color:#404040">Para eliminar una propiedad: delete obj\.prop\.</span>

<span style="color:#404040">Para comprobar si existe una propiedad con la clave proporcionada: "key" in obj\.</span>

<span style="color:#404040">Para crear bucles sobre un objeto: bucle for \(let key in obj\)\.</span>

<span style="color:#404040">Lo que hemos estudiado en este capítulo se llama “objeto simple”\, o solamente Object\.</span>

<span style="color:#404040">Hay muchos otros tipos de objetos en JavaScript:</span>

<span style="color:#404040">Array para almacenar colecciones de datos ordenados\,</span>

<span style="color:#404040">Date para almacenar la información sobre fecha y hora\,</span>

<span style="color:#404040">Error para almacenar información sobre un error\.</span>

<span style="color:#404040">Tienen sus características especiales que estudiaremos más adelante\. A veces las personas </span>  <span style="color:#404040">dicen</span>  <span style="color:#404040"> algo como “</span>  <span style="color:#404040">Tipo array" o "Tipo date"\, pero formalmente no son tipos en sí\, sino que pertenecen a un tipo de datos de “objeto” simple y lo amplían a varias maneras\.</span>

<span style="color:#404040">Los objetos en JavaScript son muy poderosos\. Aquí acabamos de arañar la superficie de un tema que es    realmente enorme\. Trabajaremos estrechamente con los objetos y aprenderemos más sobre ellos en otras partes del tutorial\.</span>

# TAREAS

<span style="color:#e1e2e7"> _Hola\,_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _objeto_ </span>

<span style="color:#e1e2e7">Escribe</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">código\,</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">una</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">línea</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">para</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">cada</span>  <span style="color:#e1e2e7"> acción:</span>

<span style="color:#e1e2e7">Crea</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">un</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">objeto</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">user</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">vacío\.</span>

<span style="color:#e1e2e7">Agrega</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">propiedad</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">name</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">con</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">John</span>  <span style="color:#e1e2e7">\. </span>  <span style="color:#e1e2e7">Agrega</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">propiedad</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">surname</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">con</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">Smith</span>  <span style="color:#e1e2e7">\. </span>  <span style="color:#e1e2e7">Cambia</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">name</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">a</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">Pete</span>  <span style="color:#e1e2e7">\.</span>

<span style="color:#e1e2e7">Remueve</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">propiedad</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">name</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">del</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">objeto\.</span>

<span style="color:#e1e2e7"> _Verificar_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _los_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _vacíos_ </span>

<span style="color:#e1e2e7">Escribe</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">función</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">isEmpty\(obj\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">que</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">devuelva</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">true</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">si el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">objeto</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">no</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">tiene </span>  <span style="color:#e1e2e7">propiedades\,</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">en</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">caso</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">contrario</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">false</span>  <span style="color:#e1e2e7">\.</span>

<span style="color:#e1e2e7">Debería</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">funcionar</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">así:</span>

<span style="color:#e1e2e7">let</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">schedule</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">=</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\{\};</span>

<span style="color:#e1e2e7">alert\(</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">isEmpty\(</span>  <span style="color:#e1e2e7">schedule</span>  <span style="color:#e1e2e7">\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\);</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">true</span>

<span style="color:#e1e2e7">schedule</span>  <span style="color:#e1e2e7">\["8:30"\]</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">=</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">"Hora</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">levantarse"; </span>  <span style="color:#e1e2e7">alert\(</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">isEmpty\(</span>  <span style="color:#e1e2e7">schedule</span>  <span style="color:#e1e2e7">\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\);</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">false</span>

<span style="color:#e1e2e7"> _Multiplicar_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _propiedades_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _numéricas_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _por_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _2_ </span>

<span style="color:#e1e2e7">Crea</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">una</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">función </span>  <span style="color:#e1e2e7">multiplyNumeric\(obj\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">que</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">multiplique</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">todas</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">las</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">propiedades </span>  <span style="color:#e1e2e7">numéricas</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">obj</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">por</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">2</span>  <span style="color:#e1e2e7">\.</span>

<span style="color:#e1e2e7">Por </span>  <span style="color:#e1e2e7">ejemplo:</span>

<span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">Antes</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">llamada </span>  <span style="color:#e1e2e7">let</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">menu</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">=</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\{</span>

<span style="color:#e1e2e7">width</span>  <span style="color:#e1e2e7">:</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">200\,</span>

<span style="color:#e1e2e7">height</span>  <span style="color:#e1e2e7">:</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">300\,</span>

<span style="color:#e1e2e7">title</span>  <span style="color:#e1e2e7">:</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">"Mi</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">menú"</span>

<span style="color:#e1e2e7">\};</span>

<span style="color:#e1e2e7">multiplyNumeric\(</span>  <span style="color:#e1e2e7">menu</span>  <span style="color:#e1e2e7">\);</span>

<span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">Después</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">llamada</span>

<span style="color:#e1e2e7">menu</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">=</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\{</span>

<span style="color:#e1e2e7">width</span>  <span style="color:#e1e2e7">:</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">400\,</span>

<span style="color:#e1e2e7">height</span>  <span style="color:#e1e2e7">:</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">600\,</span>

<span style="color:#e1e2e7">title</span>  <span style="color:#e1e2e7">:</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">"Mi</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">menú"</span>

<span style="color:#e1e2e7">\};</span>

<span style="color:#e1e2e7">Nota</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">que</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">multiplyNumeric</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">no</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">necesita</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">devolver</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">nada\.</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">Debe</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">modificar</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">objeto </span>  <span style="color:#e1e2e7">en</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">su</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">lugar\.</span>

<span style="color:#e1e2e7">P\.D\.</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">Usa</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">typeof</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">para</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">verificar</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">si</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">hay</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">un</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">número</span>  <span style="color:#e1e2e7"> aquí\.</span>

<span style="color:#fa4917"> _[Abrir](https://plnkr.co/edit/7xbmJvXLyJXoSpHW?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/7xbmJvXLyJXoSpHW?p=preview)_ </span>  <span style="color:#fa4917"> _[en](https://plnkr.co/edit/7xbmJvXLyJXoSpHW?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/7xbmJvXLyJXoSpHW?p=preview)_ </span>  <span style="color:#fa4917"> _[entorno](https://plnkr.co/edit/7xbmJvXLyJXoSpHW?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/7xbmJvXLyJXoSpHW?p=preview)_ </span>  <span style="color:#fa4917"> _[controlado](https://plnkr.co/edit/7xbmJvXLyJXoSpHW?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/7xbmJvXLyJXoSpHW?p=preview)_ </span>  <span style="color:#fa4917"> _[con](https://plnkr.co/edit/7xbmJvXLyJXoSpHW?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/7xbmJvXLyJXoSpHW?p=preview)_ </span>  <span style="color:#fa4917"> _[pruebas\.](https://plnkr.co/edit/7xbmJvXLyJXoSpHW?p=preview)_ </span>

# Referencias de objetos y copias

Una de las diferencias fundamentales entre objetos y primitivos es que los objetos son

almacenados y copiados “por referencia”\, en cambio los primitivos: strings\, number\, boolean\, etc\.; son asignados y copiados “como un valor completo”\.

Esto es fácil de entender si miramos un poco “bajo cubierta” de lo que pasa cuando copiamos por valor\. Empecemos por un primitivo como string\. Aquí ponemos una copia de message en phrase:

![](imagenes%5CUD23%20-%20Objetos_32.jpg)

Una variable no almacena el objeto mismo sino su “dirección en memoria”\, en otras palabras “una referencia” a él\. Veamos un ejemplo de tal variable:

![](imagenes%5CUD23%20-%20Objetos_33.png)

El objeto es almacenado en algún lugar de la memoria \(a la derecha de la imagen\)\, mientras que la variable user \(a la izquierda\) tiene una “referencia” a él\.

Podemos pensar de una variable objeto\, como user\, como una hoja de papel con la dirección del objeto escrita en ella\.

Cuando ejecutamos acciones con el objeto\, por ejemplo\, tomar una propiedad user\.name\, el motor JavaScript busca aquella dirección y ejecuta la operación en el objeto mismo\.

Ahora\, por qué esto es importante\. Cuando una variable de objeto es copiada\, se copia solo la referencia\. El objeto no es duplicado\. Por ejemplo:

![](imagenes%5CUD23%20-%20Objetos_34.jpg)

Como puedes ver\, aún hay un objeto\, ahora con dos variables haciendo referencia a él\. Podemos usar cualquiera de las variables para acceder al objeto y modificar su contenido:

![](imagenes%5CUD23%20-%20Objetos_35.jpg)

Es como si tuviéramos un gabinete con dos llaves y usáramos una de ellas \(admin\) para acceder a él y hacer cambios\. Si más tarde usamos la llave \(user\)\, estaríamos abriendo el mismo gabinete y accediendo al contenido cambiado\.

_Comparación por referencia_

Dos objetos son iguales solamente si ellos son el mismo objeto\.

Por ejemplo\, aquí a y b tienen referencias al mismo objeto\, por lo tanto son iguales:

![](imagenes%5CUD23%20-%20Objetos_36.jpg)

Y aquí dos objetos independientes no son iguales\, aunque se vean iguales \(ambos están vacíos\):

![](imagenes%5CUD23%20-%20Objetos_37.png)

Para comparaciones como obj1 > obj2\, o comparaciones contra un primitivo obj == 5\, los objetos son convertidos a primitivos\. Estudiaremos cómo funciona la conversión de objetos pronto\, pero a decir verdad tales comparaciones ocurren raramente y suelen ser errores de código\.

_NOTA: Un efecto importante de almacenar objetos como referencias es que un objeto_  __ __  _declarado como const puede ser modificado\._

_Clonación y mezcla\, Object\.assign_

Entonces copiar una variable de objeto crea una referencia adicional al mismo objeto\. Podemos crear un nuevo objeto y replicar la estructura del existente iterando a través de sus propiedades y copiándolas en el nivel primitivo\. Como esto:

![](imagenes%5CUD23%20-%20Objetos_38.jpg)

También podemos usar el método Object\.assign\. La sintaxis es:

![](imagenes%5CUD23%20-%20Objetos_39.png)

El primer argumento dest es el objeto destinatario\.

Los argumentos que siguen son una lista de objetos fuentes\.

Esto copia las propiedades de todos los objetos fuentes dentro del destino dest y lo devuelve como resultado\. Por ejemplo\, tenemos el objeto user\, agreguemos un par de permisos:

![](imagenes%5CUD23%20-%20Objetos_40.jpg)

Si la propiedad por copiar ya existe\, se sobrescribe:

![](imagenes%5CUD23%20-%20Objetos_41.png)

También podemos usar Object\.assign para hacer una clonación simple:

![](imagenes%5CUD23%20-%20Objetos_42.png)

Aquí\, copia todas las propiedades de user en un objeto vacío y lo devuelve\. También hay otras formas de clonar un objeto\, por ejemplo\, usando la sintaxis spread clone = \{\.\.\.user\}\, cubierto más adelante en el tutorial\.

_Clonación anidada_

Hasta ahora supusimos que todas las propiedades de user eran primitivas\. Pero las propiedades pueden ser referencias a otros objetos\. Como esto:

![](imagenes%5CUD23%20-%20Objetos_43.png)

Ahora no es suficiente copiar clone\.sizes = user\.sizes\, porque user\.sizes es un objeto y será copiado por referencia\. Entonces clone y user compartirán las mismas tallas \(\.sizes\):

![](imagenes%5CUD23%20-%20Objetos_44.jpg)

Para corregir esto\, debemos hacer que user y clone sean objetos completamente separados\, debemos usar un bucle que examine cada valor de user\[key\] y\, si es un objeto\, que replique su estructura también\. Esto es conocido como “clonación profunda” o “clonación estructurada”\. Existe un método structuredClone que implementa tal clonación profunda\.

La  llamada  a  structuredClone\(object\)  clona  el object  con todas sus propiedadas  anidadas\. Podemos usarlo en nuestro ejemplo:

![](imagenes%5CUD23%20-%20Objetos_45.jpg)

El método structuredClone puede clonar la mayoría de los tipos de datos\, como objetos\, arrays\, valores primitivos\. También soporta referencias circulares\, cuando una propiedad de objeto referencia el objeto mismo \(directamente o por una cadena de referencias\)\. Por ejemplo:

![](imagenes%5CUD23%20-%20Objetos_46.png)

Como puedes ver\, clone\.me hace referencia a clone\, no a user\! Así que la referencia circular fue clonada correctamente también\. Pero hay casos en que structuredClone falla\. Por ejemplo\, cuando un objeto tiene una propiedad “function”:

![](imagenes%5CUD23%20-%20Objetos_47.png)

Las propiedades de función no están soportadas\. Para manejar estos casos complejos podemos necesitar una combinación de métodos de clonación\, escribir código personalizado o\, para no reinventar la rueda\, tomar una implementación existente\, por ejemplo \_\.cloneDeep\(obj\) de la librería JavaScript lodash\.

# RESUMEN

Los objetos son asignados y copiados por referencia\. En otras palabras\, una variable almacena no el valor del objeto sino una referencia \(la dirección en la memoria\) del valor\. Entonces\, copiar tal variable o pasarla como argumento de función copia la referencia\, no el objeto\.

Todas las operaciones a través de referencias copiadas \(como agregar y borrar propiedades\) son efectuadas en el mismo y único objeto\.

Para hacer una “verdadera copia” \(un clon\)\, podemos usar  Object\.assing  para la denominada “clonación superficial” \(los objetos anidados son copiados por referencia\)\, o la función de “clonación profunda” structuredClone o usar una implementación personalizada como  <span style="color:#fa4917"> _[\.cloneDeep\(obj\)](https://lodash.com/docs#cloneDeep)_ </span> \.

# Método del objeto “this”
Los objetos son creados usualmente para representar entidades del mundo real, como usuarios, órdenes, etc.:

![](imagenes%5CUD23%20-%20Objetos_48.png)

Las acciones son representadas en JavaScript por funciones en las propiedades\. Ejemplos de métodos: Para empezar\, enseñemos al usuario user a decir hola:

![](imagenes%5CUD23%20-%20Objetos_49.png)

Aquí simplemente usamos una expresión de función para crear la función y asignarla a la propiedad user\.sayHi del objeto\. Entonces la llamamos con user\.sayHi\(\)\.

Una función que es la propiedad de un objeto es denominada su método\. Así\, aquí tenemos un método sayHi del objeto user\. Por supuesto\, podríamos usar una función pre\-declarada como un método\, parecido a esto:

![](imagenes%5CUD23%20-%20Objetos_50.png)

_Formas abreviadas para los métodos_

Existe una sintaxis más corta para los métodos en objetos literales:

![](imagenes%5CUD23%20-%20Objetos_51.jpg)

Como se demostró\, podemos omitir "function" y simplemente escribir sayHi\(\)\. A decir verdad\, las notaciones no son completamente idénticas\. Hay diferencias sutiles relacionadas a la herencia de objetos \(por cubrir más adelante\) que por ahora no son relevantes\. En casi todos los casos la sintaxis abreviada es la preferida\.

_“this” en métodos_

Es común que un método de objeto necesite acceder a la información almacenada en el objeto para cumplir su tarea\. Por ejemplo\, el código dentro de user\.sayHi\(\) puede necesitar el nombre del usuario user\.

Para acceder al objeto\, un método puede usar la palabra clave this\. El valor de this es el objeto “antes del punto”\, el usado para llamar al método\. Por ejemplo:

![](imagenes%5CUD23%20-%20Objetos_52.png)

Aquí durante la ejecución de user\.sayHi\(\)\, el valor de this será user\. Técnicamente\, también es posible acceder al objeto sin this\, haciendo referencia a él por medio de la variable externa:

![](imagenes%5CUD23%20-%20Objetos_53.png)

…Pero tal código no es confiable\. Si decidimos copiar user a otra variable\, por ejemplo admin = user y sobrescribir user con otra cosa\, entonces accederá al objeto incorrecto\. Eso queda demostrado en las siguientes lineas:

![](imagenes%5CUD23%20-%20Objetos_54.jpg)

Si usamos this\.name en vez de user\.name dentro de alert\, entonces el código funciona\.

_“this” no es vinculado_

En JavaScript\, la palabra clave this se comporta de manera distinta a la mayoría de otros lenguajes de programación\. Puede ser usado en cualquier función\, incluso si no es el método de un objeto\. No hay error de sintaxis en el siguiente ejemplo:

![](imagenes%5CUD23%20-%20Objetos_55.png)

El valor de this es evaluado durante el tiempo de ejecución\, dependiendo del contexto\. Por ejemplo\, aquí la función es asignada a dos objetos diferentes y tiene diferentes “this” en sus llamados:

![](imagenes%5CUD23%20-%20Objetos_56.jpg)

La regla es simple: si obj\.f\(\) es llamado\, entonces this es obj durante el llamado de f\. Entonces es tanto user o admin en el ejemplo anterior\.

_Las funciones de flecha no tienen “this”_

Las funciones de flecha son especiales: ellas no tienen su “propio” this\. Si nosotros hacemos referencia a this desde tales funciones\, esta será tomada desde afuera de la función “normal”\. Por ejemplo\, aquí arrow\(\) usa this desde fuera del método user\.sayHi\(\):

![](imagenes%5CUD23%20-%20Objetos_57.png)

Esto es una característica especial de las funciones de flecha\, útil cuando no queremos realmente un this separado sino tomarlo de un contexto externo\. Más adelante en el capítulo Funciones de flecha revisadas las trataremos en profundidad\.

# RESUMEN



* Las funciones que son almacenadas en propiedades de objeto son llamadas“métodos”\.
  * Los método permiten a los objetos “actuar”\, como object\.doSomething\(\)\.
  * <span style="color:#a42f0f"> </span> Los métodos pueden hacer referencia al objeto con this\.
* El valor de this es definido en tiempo de ejecución\.
* Cuando una función es declarada\, puede usar this\, pero ese this no tiene valor hasta que la función es llamada\.
* Una función puede ser copiada entre objetos\.
* Cuando una función es llamada en la sintaxis de método: object\.method\(\)\,  el valor this durante el llamado es object\.
* Tened en cuenta que las funciones de flecha son especiales: ellas no tienen this\. Cuando this es accedido dentro de una función de flecha\, su valor es tomado desde el exterior\.


# TAREAS

<span style="color:#e1e2e7"> _Usando_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _el_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _"this"_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _en_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _un_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _objeto_ </span>  <span style="color:#e1e2e7"> _ literal_ </span>

<span style="color:#e1e2e7">Aquí</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">función </span>  <span style="color:#e1e2e7">makeUser</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">devuelve</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">un</span>  <span style="color:#e1e2e7"> objeto\.</span>

<span style="color:#e1e2e7">¿Cuál</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">es</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">resultado</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">acceder</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">a</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">su</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">ref</span>  <span style="color:#e1e2e7">?</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">¿Por</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">qué?</span>

<span style="color:#e1e2e7">function</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">makeUser\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\{ </span>  <span style="color:#e1e2e7">return</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\{</span>

<span style="color:#e1e2e7">name</span>  <span style="color:#e1e2e7">:</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">"John"\,</span>

<span style="color:#e1e2e7">ref</span>  <span style="color:#e1e2e7">:</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">this</span>

<span style="color:#e1e2e7">\};</span>

<span style="color:#e1e2e7">\}</span>

<span style="color:#e1e2e7">let</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">user</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">=</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">makeUser\(\);</span>

<span style="color:#e1e2e7">alert\(</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">user</span>  <span style="color:#e1e2e7">\.</span>  <span style="color:#e1e2e7">ref</span>  <span style="color:#e1e2e7">\.</span>  <span style="color:#e1e2e7">name</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\);</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">¿Cuál</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">es</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">resultado?</span>

<span style="color:#e1e2e7"> _Crea_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _una_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _calculadora_ </span>

<span style="color:#e1e2e7">Crea</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">un</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">objeto</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">calculator</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">con</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">tres</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">métodos:</span>

<span style="color:#e1e2e7">read\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">pide</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">dos</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valores</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">y</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">los</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">almacena</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">como</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">propiedades</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">objeto</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">con</span>

<span style="color:#e1e2e7">nombres</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">a</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">y</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">b</span>  <span style="color:#e1e2e7">\.</span>

<span style="color:#e1e2e7">sum\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">devuelve</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">suma</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">los</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valores</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">almacenados\.</span>

<span style="color:#e1e2e7">mul\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">multiplica</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">los</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valores</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">almacenados</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">y</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">devuelve</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">resultado\.</span>

<span style="color:#e1e2e7">let</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">calculator</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">=</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\{</span>

<span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\.\.\.</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">tu</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">código</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\.\.\.</span>

<span style="color:#e1e2e7">\};</span>

<span style="color:#e1e2e7">calculator</span>  <span style="color:#e1e2e7">\.read\(\);</span>

<span style="color:#e1e2e7">alert\(</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">calculator</span>  <span style="color:#e1e2e7">\.sum\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\); </span>  <span style="color:#e1e2e7">alert\(</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">calculator</span>  <span style="color:#e1e2e7">\.mul\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\);</span>

<span style="color:#fa4917"> _[Ejecutar](https://es.javascript.info/object-methods)_ </span>  <span style="color:#fa4917"> _[ ](https://es.javascript.info/object-methods)_ </span>  <span style="color:#fa4917"> _[el](https://es.javascript.info/object-methods)_ </span>  <span style="color:#fa4917"> _[ ](https://es.javascript.info/object-methods)_ </span>  <span style="color:#fa4917"> _[demo](https://es.javascript.info/object-methods)_ </span>

<span style="color:#fa4917"> _[Abrir](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ </span>  <span style="color:#fa4917"> _[en](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ </span>  <span style="color:#fa4917"> _[entorno](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ </span>  <span style="color:#fa4917"> _[controlado](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ </span>  <span style="color:#fa4917"> _[con](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ </span>  <span style="color:#fa4917"> _[pruebas\.](https://plnkr.co/edit/A6BH6X0blqSvXzs4?p=preview)_ </span>

<span style="color:#e1e2e7"> _Encadenamiento_ </span>

<span style="color:#e1e2e7">Hay</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">un</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">objeto</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">ladder</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">que</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">permite</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">subir</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">y</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">bajar:</span>

<span style="color:#e1e2e7">let</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">ladder</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">=</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\{ </span>  <span style="color:#e1e2e7">step</span>  <span style="color:#e1e2e7">:</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">0\,</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">up\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\{</span>

<span style="color:#e1e2e7">this\.</span>  <span style="color:#e1e2e7">step</span>  <span style="color:#e1e2e7">\+\+;</span>

<span style="color:#e1e2e7">\}\,</span>

<span style="color:#e1e2e7">down\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\{</span>

<span style="color:#e1e2e7">this\.</span>  <span style="color:#e1e2e7">step</span>  <span style="color:#e1e2e7">\-</span>  <span style="color:#e1e2e7">\-</span>  <span style="color:#e1e2e7">;</span>

<span style="color:#e1e2e7">\}\,</span>

<span style="color:#e1e2e7">showStep:</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">function\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\{</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">muestra</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">peldaño</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">actual </span>  <span style="color:#e1e2e7">alert\(</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">this\.</span>  <span style="color:#e1e2e7">step</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\);</span>

<span style="color:#e1e2e7">\}</span>

<span style="color:#e1e2e7">\};</span>

<span style="color:#e1e2e7">Ahora\,</span>  <span style="color:#e1e2e7"> si </span>  <span style="color:#e1e2e7">necesitamos</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">hacer</span>  <span style="color:#e1e2e7"> varios</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">llamados</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">en</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">secuencia</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">podemos</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">hacer</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">algo </span>  <span style="color:#e1e2e7">como</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">esto:</span>

<span style="color:#e1e2e7">ladder</span>  <span style="color:#e1e2e7">\.up\(\);</span>

<span style="color:#e1e2e7">ladder</span>  <span style="color:#e1e2e7">\.up\(\);</span>

<span style="color:#e1e2e7">ladder</span>  <span style="color:#e1e2e7">\.down\(\); </span>  <span style="color:#e1e2e7">ladder</span>  <span style="color:#e1e2e7">\.showStep\(\);</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">1 </span>  <span style="color:#e1e2e7">ladder</span>  <span style="color:#e1e2e7">\.down\(\); </span>  <span style="color:#e1e2e7">ladder</span>  <span style="color:#e1e2e7">\.showStep\(\);</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">0</span>

<span style="color:#e1e2e7">Modifica</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el </span>  <span style="color:#e1e2e7">código</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">“arriba”</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">up</span>  <span style="color:#e1e2e7">\, </span>  <span style="color:#e1e2e7">“abajo”</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">down</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">y</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">“mostrar</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">peldaño”</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">showStep</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">para </span>  <span style="color:#e1e2e7">hacer</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">los</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">llamados</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">encadenables</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">como</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">esto:</span>

<span style="color:#e1e2e7">ladder</span>  <span style="color:#e1e2e7">\.up\(\)\.up\(\)\.down\(\)\.showStep\(\)\.down\(\)\.showStep\(\);</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">shows</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">1</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">then</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">0</span>

<span style="color:#e1e2e7">Tal</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">enfoque</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">es</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">ampliamente</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">usado</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">entre</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">las</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">librerías</span>  <span style="color:#e1e2e7"> JavaScript\.</span>

<span style="color:#fa4917"> _[Abrir](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ </span>  <span style="color:#fa4917"> _[en](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ </span>  <span style="color:#fa4917"> _[entorno](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ </span>  <span style="color:#fa4917"> _[controlado](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ </span>  <span style="color:#fa4917"> _[con](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ </span>  <span style="color:#fa4917"> _[pruebas\.](https://plnkr.co/edit/qr6ASfJci9DEGyvi?p=preview)_ </span>

# Constructor, operador “new”

La sintaxis habitual \{\.\.\.\} nos permite crear un objeto\. Pero a menudo necesitamos crear varios objetos similares\, como múltiples usuarios\, elementos de menú\, etcétera\.

Esto se puede realizar utilizando el constructor de funciones y el operador "new"\.

_Función_  _ _  _constructora_

La función constructora es técnicamente una función normal\. Aunque hay dos convenciones:

Son nombradas con la primera letra mayúscula\.

Sólo deben ejecutarse con el operador "new"\.

Por ejemplo:

![](imagenes%5CUD23%20-%20Objetos_58.png)

Cuando una función es ejecutada con new\, realiza los siguientes pasos:

Se crea un nuevo objeto vacío y se asigna a this\.

Se ejecuta el cuerpo de la función\. Normalmente se modifica this y se le agrega nuevas propiedades\.

Se devuelve el valor de this\.

En otras palabras\, new User\(\.\.\.\) realiza algo como:

![](imagenes%5CUD23%20-%20Objetos_59.png)

Entonces let user = new User\("Jack"\) da el mismo resultado que:

![](imagenes%5CUD23%20-%20Objetos_60.png)

Ahora si queremos crear otros usuarios\, podemos llamar a new User\("Ann"\)\, new User\("Alice"\)\, etcétera\. Mucho más corto que usar literales todo el tiempo y también fácil de leer\.

Este es el principal propósito del constructor – implementar código de creación de objetos re\-utilizables\.

Tomemos nota otra vez: técnicamente cualquier función \(excepto las de flecha pues no tienen this\) puede ser utilizada como constructor\. Puede ser llamada con new\, y ejecutará el algoritmo de arriba\. La “primera letra mayúscula” es un acuerdo general\, para dejar en claro que la función debe ser ejecutada con new\.

Dentro de una función\, podemos verificar si ha sido llamada con o sin el new utilizando una propiedad especial: new\.target\.

En las llamadas normales devuelve undefined\, y cuando es llamada con new devuelve la función:

![](imagenes%5CUD23%20-%20Objetos_61.png)

Esto puede ser utilizado dentro de la función para conocer si ha sido llamada con new\, "en modo constructor "; o sin él\, “en modo regular”\.

También podemos hacer que ambas formas de llamarla\, con new y “regular”\, realicen lo mismo:

![](imagenes%5CUD23%20-%20Objetos_62.jpg)

Este enfoque es utilizado a veces en las librerías para hacer la sintaxis más flexible\. Así la gente puede llamar a la función con o sin new y aún funciona\.

Sin embargo\, probablemente no sea algo bueno para usar en todas partes\, porque omitir new hace que sea un poco menos obvio lo que está sucediendo\. Con new todos sabemos que se está creando el nuevo objeto\.

_Return desde constructores_

Normalmente\, los constructores no tienen una sentencia return\. Su tarea es escribir todo lo necesario al this\, y automáticamente este se convierte en el resultado\.

Pero si hay una sentencia return\, entonces la regla es simple:

Si return es llamado con un objeto\, entonces se devuelve tal objeto en vez de this\.

Si return es llamado con un tipo de dato primitivo\, es ignorado\.

En otras palabras\, return con un objeto devuelve ese objeto\, en todos los demás casos se devuelve this\. Por ejemplo\, aquí return anula this al devolver un objeto:

![](imagenes%5CUD23%20-%20Objetos_63.jpg)

Y aquí un ejemplo con un return vacío \(o podemos colocar un primitivo después de él\, no importa\):

![](imagenes%5CUD23%20-%20Objetos_64.png)

Normalmente	los  constructores  no  tienen  una  sentencia  return\.  Aquí  mencionamos  el comportamiento especial con devolución de objetos principalmente por el bien de la integridad\.

_Métodos en constructor_

Utilizar constructor de funciones para crear objetos nos da mucha flexibilidad\. La función constructora puede tener argumentos que definan cómo construir el objeto y qué colocar dentro\.

Por supuesto podemos agregar a this no sólo propiedades\, sino también métodos\. Por ejemplo\, new User\(name\) de abajo\, crea un objeto con el name dado y el método sayHi:

![](imagenes%5CUD23%20-%20Objetos_65.png)

Para crear objetos complejos existe una sintaxis más avanzada\, classes\.

# RESUMEN

<span style="color:#404040">Las funciones Constructoras o\, más corto\, constructores\, son funciones normales\, pero existe un </span>  <span style="color:#404040">común</span>  <span style="color:#404040"> </span>  <span style="color:#404040">acuerdo</span>  <span style="color:#404040"> </span>  <span style="color:#404040">para nombrarlas con la primera letra en </span>  <span style="color:#404040">mayúscula</span>  <span style="color:#404040">\.</span>

<span style="color:#404040">Las funciones Constructoras sólo deben ser llamadas utilizando new\. Tal llamado implica la creación de un this vacío al comienzo y devolver el this rellenado al final\.</span>

<span style="color:#404040">Podemos utilizar funciones constructoras para crear múltiples objetos similares\.</span>

<span style="color:#404040">JavaScript proporciona funciones constructoras para varios objetos de lenguaje incorporados: como Date para fechas\, Set para conjuntos y otros que planeamos estudiar\.</span>

# TAREAS

<span style="color:#e1e2e7"> _Crear_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _nueva_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _Calculadora_ </span>

<span style="color:#e1e2e7">Crear</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">una</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">función</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">constructora</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">Calculator</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">que</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">crea</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">objetos</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">con</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">3</span>  <span style="color:#e1e2e7"> métodos:</span>

<span style="color:#e1e2e7">read\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">pide</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">dos</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valores</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">usando</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">prompt</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">y</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">los</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">guarda</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">en</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">las</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">propiedades</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">del </span>  <span style="color:#e1e2e7">objeto</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">con</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">los</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">nombres</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">a</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">y</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">b</span>  <span style="color:#e1e2e7">\.</span>

<span style="color:#e1e2e7">sum\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">devuelve</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">suma</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">estas</span>  <span style="color:#e1e2e7"> propiedades\.</span>

<span style="color:#e1e2e7">mul\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">devuelve</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">producto</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">multiplicación</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">estas</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">propiedades\.</span>

<span style="color:#e1e2e7">Por </span>  <span style="color:#e1e2e7">ejemplo:</span>

<span style="color:#e1e2e7">let</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">calculator</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">=</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">new</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">Calculator\(\);</span>

<span style="color:#e1e2e7">calculator</span>  <span style="color:#e1e2e7">\.read\(\);</span>

<span style="color:#e1e2e7">alert\(</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">"Sum="</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\+</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">calculator</span>  <span style="color:#e1e2e7">\.sum\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\);</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">alert\(</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">"Mul="</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\+</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">calculator</span>  <span style="color:#e1e2e7">\.mul\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">\);</span>

<span style="color:#fa4917"> _[Ejecutar](https://es.javascript.info/constructor-new)_ </span>  <span style="color:#fa4917"> _[ ](https://es.javascript.info/constructor-new)_ </span>  <span style="color:#fa4917"> _[el](https://es.javascript.info/constructor-new)_ </span>  <span style="color:#fa4917"> _[ ](https://es.javascript.info/constructor-new)_ </span>  <span style="color:#fa4917"> _[demo](https://es.javascript.info/constructor-new)_ </span>

<span style="color:#fa4917"> _[Abrir](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ </span>  <span style="color:#fa4917"> _[en](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ </span>  <span style="color:#fa4917"> _[entorno](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ </span>  <span style="color:#fa4917"> _[controlado](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ </span>  <span style="color:#fa4917"> _[con](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ </span>  <span style="color:#fa4917"> _[pruebas\.](https://plnkr.co/edit/3nR68H2HWFG661Ca?p=preview)_ </span>

<span style="color:#e1e2e7"> _Crear_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _nuevo_ </span>  <span style="color:#e1e2e7"> _ _ </span>  <span style="color:#e1e2e7"> _Acumulador_ </span>

<span style="color:#e1e2e7">Crear</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">una</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">función</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">constructor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">Accumulator\(startingValue\)</span>  <span style="color:#e1e2e7">\.</span>

<span style="color:#e1e2e7">El</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">objeto</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">que</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">crea</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">debería:</span>

<span style="color:#e1e2e7">Almacene</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">“valor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">actual”</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">en</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">propiedad</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">value</span>  <span style="color:#e1e2e7">\. El</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">inicial</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">se</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">establece</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">en </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">argumento</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">del</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">constructor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">startingValue</span>  <span style="color:#e1e2e7">\.</span>

<span style="color:#e1e2e7">El</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">método</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">read\(\)</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">debe</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">usar</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">prompt</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">para</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">leer</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">un</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">nuevo</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">número</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">y</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">agregarlo </span>  <span style="color:#e1e2e7">a</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">value</span>  <span style="color:#e1e2e7">\.</span>

<span style="color:#e1e2e7">En</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">otras</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">palabras\,</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">propiedad</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">value</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">es</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">suma</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">todos</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">los</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valores</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">ingresados </span>  <span style="color:#e1e2e7">por</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">usuario</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">con</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">inicial</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">startingValue</span>  <span style="color:#e1e2e7">\.</span>

<span style="color:#e1e2e7">Aquí</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">está</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">demostración</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">del</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">código:</span>

<span style="color:#e1e2e7">let</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">accumulator</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">=</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">new</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">Accumulator\(1\);</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">inicial</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">1</span>

<span style="color:#e1e2e7">accumulator</span>  <span style="color:#e1e2e7">\.read\(\);</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">agrega</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">introducido</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">por</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">usuario</span>

<span style="color:#e1e2e7">accumulator</span>  <span style="color:#e1e2e7">\.read\(\);</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">agrega</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valor</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">introducido</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">por</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">el</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">usuario</span>

<span style="color:#e1e2e7">alert\(</span>  <span style="color:#e1e2e7">accumulator</span>  <span style="color:#e1e2e7">\.</span>  <span style="color:#e1e2e7">value</span>  <span style="color:#e1e2e7">\);</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">//</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">muestra</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">la</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">suma</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">de</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">estos</span>  <span style="color:#e1e2e7"> </span>  <span style="color:#e1e2e7">valores</span>

<span style="color:#fa4917"> _[Ejecutar](https://es.javascript.info/constructor-new)_ </span>  <span style="color:#fa4917"> _[ ](https://es.javascript.info/constructor-new)_ </span>  <span style="color:#fa4917"> _[el](https://es.javascript.info/constructor-new)_ </span>  <span style="color:#fa4917"> _[ ](https://es.javascript.info/constructor-new)_ </span>  <span style="color:#fa4917"> _[demo](https://es.javascript.info/constructor-new)_ </span>

<span style="color:#fa4917"> _[Abrir](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ </span>  <span style="color:#fa4917"> _[en](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ </span>  <span style="color:#fa4917"> _[entorno](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ </span>  <span style="color:#fa4917"> _[controlado](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ </span>  <span style="color:#fa4917"> _[con](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ </span>  <span style="color:#fa4917"> _[ ](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ </span>  <span style="color:#fa4917"> _[pruebas\.](https://plnkr.co/edit/Uhk0b96PaSMW96RZ?p=preview)_ </span>

# Encadenamiento opcional '?.'

_Esta es una adición reciente al lenguaje\. Los navegadores antiguos pueden necesitar polyfills\._

El encadenamiento opcional ?\. es una forma a prueba de errores para acceder a las propiedades anidadas de los objetos\, incluso si no existe una propiedad intermedia\.

_El problema de la propiedad que no existe_

Si acaba de comenzar a leer el tutorial y aprender JavaScript\, quizás el problema aún no lo haya tocado\, pero es bastante común\. Como ejemplo\, digamos que tenemos objetos user que contienen información de nuestros usuarios\. La mayoría de nuestros usuarios tienen la dirección en  la  propiedad  user\.address\,  con  la  calle  en  user\.address\.street\,  pero  algunos  no  la proporcionaron\.

En  tal  caso\,  cuando  intentamos  obtener  user\.address\.streeten  un  usuario  sin  dirección obtendremos un error:

![](imagenes%5CUD23%20-%20Objetos_66.png)

Este es el resultado esperado\. JavaScript funciona así\, como user\.address es undefined\, el intento de obtener user\.address\.street falla dando un error\.

En muchos casos prácticos preferiríamos obtener undefined en lugar del error \(dando a entender “sin calle”\)

… y otro ejemplo\. En desarrollo web\, podemos obtener un objeto que corresponde a un elemento   de   página   web   usando   el   llamado   a   un   método   especial   como document\.querySelector\('\.elem'\)\, que devuelve null cuando no existe tal elemento\.

![](imagenes%5CUD23%20-%20Objetos_67.jpg)

Una vez más\, si el elemento no existe\, obtendremos un error al intentar acceder a la propiedad

\.innerHTML de null\. Y en algunos casos\, cuando la ausencia del elemento es normal\, quisiéramos evitar el error y simplemente aceptar html = null como resultado\.

¿Cómo podemos hacer esto? La solución obvia sería chequear el valor usando if o el operador condicional? antes de usar la propiedad:

![](imagenes%5CUD23%20-%20Objetos_68.jpg)

Esto funciona\, no hay error… Pero es bastante poco elegante\. Como puedes ver\, "user\.address" aparece   dos   veces   en   el   código\.   El   mismo   caso\,   pero   con   la   búsqueda   de document\.querySelector:

<span style="color:#ffffff">let	=	</span>  <span style="color:#f8f8f1">document\.</span>  <span style="color:#ffffff">querySelector</span>  <span style="color:#f8f8f1">\(</span>  <span style="color:#ffffff">'\.elem'</span>  <span style="color:#f8f8f1">\)	</span>  <span style="color:#ffffff">?</span>

<span style="color:#f8f8f1">document\.</span>  <span style="color:#ffffff">querySelector</span>  <span style="color:#f8f8f1">\(</span>  <span style="color:#ffffff">'\.elem'</span>  <span style="color:#f8f8f1">\)\.innerHTML </span>  <span style="color:#ffffff">: null</span>  <span style="color:#f8f8f1">;</span>

Podemos ver que el elemento de búsqueda document\.querySelector\('\.elem'\) es llamado dos veces aquí\. En propiedades anidadas más profundamente\, esto se vuelve un problema porque se requerirán más repeticiones\.

Ejemplo: Tratemos de obtener user\.address\.street\.name de manera similar\.

![](imagenes%5CUD23%20-%20Objetos_69.jpg)

Esto es horrible\, podemos tener problemas para siquiera entender tal código\. Hay una mejor manera de escribirlo\, usando el operador &&:

![](imagenes%5CUD23%20-%20Objetos_70.jpg)

Poniendo AND en el camino completo a la propiedad asegura que todos los componentes existen \(si no\, la evaluación se detiene\)\, pero no es lo ideal\.

Como puedes ver\, los nombres de propiedad aún están duplicados en el código\. Por ejemplo en el código de arriba user\.address aparece tres veces\. Es por ello que el encadenamiento opcional ?\. fue agregado al lenguaje\.

_Encadenamiento opcional_

El encadenamiento opcional ?\. detiene la evaluación y devuelve undefined si el valor antes del

?\. es undefined o null\.

__De aquí en adelante en este artículo\, por brevedad\, diremos que algo “existe” si no es null o undefined\.__

En otras palabras\, value?\.prop:

funciona como value\.prop si value existe\,

de otro modo \(cuando value es undefined/null\) devuelve undefined\.

Aquí está la forma segura de acceder a user\.address\.street usando ?\.:

![](imagenes%5CUD23%20-%20Objetos_71.jpg)

El código es corto y claro\, no hay duplicación en absoluto\. Aquí tenemos un ejemplo con document\.querySelector:

![](imagenes%5CUD23%20-%20Objetos_72.jpg)

Leer la dirección con user?\.Address funciona incluso si el objeto user no existe:

![](imagenes%5CUD23%20-%20Objetos_73.png)

Tenga en cuenta: la sintaxis ?\. hace opcional el valor delante de él\, pero no más allá\.

Por ejemplo\, en user?\.address\.street\.name\, el ?\. permite que user sea null/undefined \(y devuelve undefined en tal caso\)\, pero solo a user\. El resto de las propiedades son accedidas de la manera normal\. Si queremos que algunas de ellas sean opcionales\, necesitamos reemplazar más \. con ?\.\.

__NOTA:  Si  por  ejemplo  no  hay  una  variable  user  declarada  previamente\,  entonces user?\.anything provocará un error\.__

_Short\-circuiting \(Cortocircuitos\)_

Como se dijo antes\, el ?\. detiene inmediatamente \(“cortocircuito”\) la evaluación si la parte izquierda no existe\. Entonces\, si a la derecha de ?\. hay funciones u operaciones adicionales\, estas no se ejecutarán\. Por ejemplo:

![](imagenes%5CUD23%20-%20Objetos_74.jpg)

_Otros casos: ?\.\(\)\, ?\.\[\]_

El encadenamiento opcional ?\. no es un operador\, es una construcción de sintaxis especial que también funciona con funciones y corchetes\. Por ejemplo\, ?\.\(\) se usa para llamar a una función que puede no existir\.

En el siguiente código\, algunos de nuestros usuarios tienen el método admin\, y otros no:

![](imagenes%5CUD23%20-%20Objetos_75.jpg)

Aquí\, en ambas líneas\, primero usamos el punto \(userAdmin\.admin\) para obtener la propiedad admin\, porque asumimos que el objeto user existe y es seguro leerlo\.

Entonces ?\.\(\) comprueba la parte izquierda: si la función admin existe\, entonces se ejecuta \(para userAdmin\)\. De lo contrario \(para userGuest\) la evaluación se detiene sin errores\.

La sintaxis ?\.\[\] también funciona si quisiéramos usar corchetes \[\] para acceder a las propiedades en lugar de punto \.\. Al igual que en casos anteriores\, permite leer de forma segura una propiedad de un objeto que puede no existir\.

![](imagenes%5CUD23%20-%20Objetos_76.png)

También podemos usar ?\. con delete:

![](imagenes%5CUD23%20-%20Objetos_77.jpg)

# RESUMEN

<span style="color:#404040">La sintaxis de encadenamiento opcional ?\. tiene tres formas:</span>

<span style="color:#404040">obj?\.prop – devuelve obj\.prop si obj existe\, si no\, undefined\.</span>

<span style="color:#404040">obj?\.\[prop\] – devuelve obj\[prop\] si obj existe\, si no\, undefined\.</span>

<span style="color:#404040">obj\.method?\.\(\) – llama a obj\.method\(\) si obj\.method existe\, si no devuelve undefined\.</span>

<span style="color:#404040">Como podemos ver\, todos ellos son sencillos y fáciles de usar\. El ?\. comprueba   si la parte izquierda es </span>  <span style="color:#404040">null</span>  <span style="color:#404040">/</span>  <span style="color:#404040">undefined</span>  <span style="color:#404040"> y permite que la evaluación continúe si no es así\.</span>

<span style="color:#404040">Una cadena de ?\. permite acceder de forma segura a las </span>  <span style="color:#404040">propiedade</span>  <span style="color:#404040">s </span>  <span style="color:#404040">anidadas</span>  <span style="color:#404040">\.</span>

<span style="color:#404040">Aun así\, debemos aplicar ?\. con cuidado\, solamente donde sea aceptable     que\, de acuerdo con nuestra lógica\, la parte izquierda no exista\. Esto es para que no nos oculte errores de programación\, si ocurren\.</span>

