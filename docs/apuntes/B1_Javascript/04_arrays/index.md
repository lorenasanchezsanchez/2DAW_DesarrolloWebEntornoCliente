## INTRODUCCIÓN A ARRAYS EN JAVASCRIPT

# 1. ¿Qué son los arrays?

A menudo es necesario una colección ordenada, donde tenemos un 1ro, un 2do,  un  3er  elemento  y  así  sucesivamente.  Por  ejemplo, necesitamos almacenar una lista de algo: usuarios, bienes, elementos HTML, etc.

No es conveniente usar objetos aquí, porque no proveen métodos para manejar el orden de los elementos. No podemos insertar una nueva propiedad “entre” los existentes. Los objetos no  están hechos para eso. Existe una estructura llamada __Array__ (llamada en español arreglo o matriz/vector) para almacenar colecciones ordenadas.

Hay dos sintaxis para crear un __array__ vacío:

![](imagenes/UD24%20ARRAYS_0.png)

![](imagenes/UD24%20ARRAYS_1.png)

Casi siempre se usa la segunda. Podemos suministrar elementos iniciales entre Los corchetes

Un __array__ puede almacenar elementos de cualquier tipo. Por ejemplo:

![](imagenes/UD24%20ARRAYS_2.jpg)


---

Los  elementos  del  __array__  están  numerados  comenzando  desde  cero.  Podemos  obtener  un elemento por su número entre corchetes:

![](imagenes/UD24%20ARRAYS_3.png)

Podemos reemplazar un elemento:

![](imagenes/UD24%20ARRAYS_4.png)

…o agregar uno nuevo al __array__:

![](imagenes/UD24%20ARRAYS_5.png)

![](imagenes/UD24%20ARRAYS_6.png)

La cuenta total de elementos en el __array__ es su longitud __length__:

![](imagenes/UD24%20ARRAYS_7.png)

También podemos usar __alert__ para mostrar el __array__ completo.

---

### Obtener los últimos elementos con “at”

Digamos que queremos el último elemento de un __array__. Algunos lenguajes de programación permiten el uso de índices negativos para este propósito, como __fruits[-1]__.

Aunque en JavaScript esto no funcionará. El resultado será __undefined__, porque el índice de los corchetes es tratado literalmente. Podemos calcular explícitamente el último índice y luego acceder al elemento: __fruits[fruits.length - 1]__.

![](imagenes/UD24%20ARRAYS_8.png)

Un poco engorroso, ¿no es cierto? Necesitamos escribir el nombre de la variable dos veces. Afortunadamente, hay una sintaxis más corta: __fruits.at(-1)__:

![](imagenes/UD24%20ARRAYS_9.png)

En otras palabras, __arr.at(i)__:

es exactamente lo mismo que __arr[i]__, si i >= 0.

para valores negativos de i, salta hacia atrás desde el final del __array__.

---

### Métodos pop/push, shift/unshift

Una cola es uno de los usos más comunes de un __array__. En ciencias de la computación, significa una colección ordenada de elementos que soportan dos operaciones:

![](imagenes/UD24%20ARRAYS_10.png)

__push__  inserta un elemento al final.

__shift__  obtiene el elemento del principio, avanzando la cola, y así el segundo elemento se vuelve primero.


* Los __arrays__ soportan ambas operaciones.
* Por ejemplo, una cola de mensajes que necesitamos mostrar en pantalla. Hay otro caso de uso para los __arrays__ – la estructura de datos llamada pila. Ella soporta dos operaciones:
* __push__  agrega un elemento al final.
* __pop__  toma un elemento desde el final.
* Entonces los elementos nuevos son agregados o tomados siempre desde el “final”. Una pila es usualmente mostrada como un mazo de cartas, donde las nuevas cartas son agregadas al tope o tomadas desde el tope:

![](imagenes/UD24%20ARRAYS_11.jpg)


---

Para las pilas, la última introducida es la primera en ser recibida, en inglés esto es llamado principio LIFO (Last-In-First-Out, última en entrar primera en salir). Para las colas, tenemos FIFO (First-In-First-Out primera en entrar, primera en salir).

Los __arrays__ en JavaScript pueden trabajar como colas o pilas. Ellos permiten agregar/quitar elementos al/del principio o al/del final. Métodos que trabajan sobre el final del __array__:

* __Pop__ --> Extrae el último elemento del __array__ y lo devuelve:

![](imagenes/UD24%20ARRAYS_12.png)

Tanto __fruits.pop()__ como __fruits.at(-1)__ devuelven el último elemento del __array__, pero __fruits.pop()__ también modifica el __array__ eliminando tal elemento.

* __Push__ --> Agrega el elemento al final del __array__:

![](imagenes/UD24%20ARRAYS_13.png)

El  llamado a __fruits.push(...)__ es igual a __fruits[fruits.length]__ = .... Métodos que trabajan con el principio del __array__:

---

* __Shift__   -->  Extrae   el primer elemento del __array__ y lo devuelve:

![](imagenes/UD24%20ARRAYS_14.png)

* __Unshift__ -->  Agrega el elemento al principio del __array__:

![](imagenes/UD24%20ARRAYS_15.png)

Los  métodos __push__ y __unshift__ pueden agregar múltiples elementos de una vez:

![](imagenes/UD24%20ARRAYS_16.png)

---

Un __array__ es una  clase especial de objeto. Los corchetes usados para acceder a una propiedad __arr[0]__ vienen de la sintaxis de objeto. Son esencialmente lo mismo que __obj[key]__, donde __arr__ es el objeto mientras los números son usados como claves. Ellos extienden los objetos proveyendo métodos especiales para trabajar con colecciones ordenadas de datos y también la propiedad __length__. Pero en el corazón es aún un objeto.

Recuerde, solo hay ocho tipos de datos básicos en JavaScript (consulte el capítulo Tipos de datos para obtener más información). __Array__ es un objeto y, por tanto, se comporta como un objeto. Por ejemplo, es copiado por referencia :

![](imagenes/UD24%20ARRAYS_17.jpg)

… Pero lo que hace a los __array__ realmente especiales es su representación interna. El motor trata de almacenarlos en áreas de memoria contigua, uno tras otro, justo como muestra la ilustración en este capítulo. Hay otras optimizaciones también para hacer que los __arrays__ trabajen verdaderamente rápido.


---

Pero todo esto se puede malograr si dejamos de trabajarlos como __arrays__ de colecciones ordenadas y comenzamos a usarlos como si fueran objetos comunes. Por ejemplo, técnicamente podemos hacer esto:

![](imagenes/UD24%20ARRAYS_18.jpg)

Esto es posible porque los __arrays__ son objetos en su base. Podemos agregar cualquier propiedad en ellos. Pero el motor verá que estamos tratándolo como un objeto común. Las optimizaciones específicas no son aptas para tales casos y serán desechadas, y sus beneficios desaparecerán.

Las formas de malograr un __array__:

- Agregar una propiedad no numérica como __arr.test__ = 5.

- Generar agujeros como: agregar __arr[0]__ y luego __arr[1000]__ (y nada entre ellos).

- Llenar el __array__ en orden inverso, como __arr[1000]__, __arr[999]__ y así.

Piensa en los __arrays__ como estructuras especiales para trabajar con datos ordenados. Ellos proveen métodos especiales para ello. Los __arrays__ están cuidadosamente afinados dentro de los motores JavaScript para funcionar con datos ordenados contiguos, por favor úsalos de esa manera. Y si necesitas claves arbitrarias, hay altas chances de que en realidad necesites objetos comunes {}.
![](imagenes/UD24%20ARRAYS_19.png)

---

Los métodos __push__/__pop__ son rápidos, mientras que __shift__ /__unshift__ son  lentos.

¿Por qué es más rápido trabajar con el final del __array__ que con el principio? Veamos qué pasa durante la ejecución:

![](imagenes/UD24%20ARRAYS_20.png)

No es suficiente tomar y eliminar el elemento con el índice 0. Los demás elementos necesitan ser renumerados también. La operación __shift__ debe hacer 3 cosas:

1. Remover el elemento con índice 0.

2. Mover todos los elementos hacia la izquierda y renumerarlos: desde el índice 1 a 0, de 2 a 1 y así sucesivamente.

3. Actualizar la longitud: la propiedad __length__.

![](imagenes/UD24%20ARRAYS_21.png)

Cuanto más elemento haya en el __array__ ,más tiempo tomará moverlos, más operaciones en memoria. 


---
Algo similar ocurre con __unshift__: para agregar un elemento al principio del __array__, necesitamos primero mover todos los elementos hacia la derecha, incrementando sus índices. ¿Y qué pasa con __push__/__pop__? Ellos no necesitan mover nada. Para extraer un elemento del final, el método __pop__ limpia el índice y acorta __length__. Las acciones para la operación __pop__:

![](imagenes/UD24%20ARRAYS_22.png)

El método __pop__ no necesita mover nada, porque los demás elementos mantienen sus índices. Es por ello que es muy rápido. Algo similar ocurre con el método __push__.

Una de las formas más viejas de iterar los __items__ de un __array__ es el bucle __for__ sobre sus índices:

![](imagenes/UD24%20ARRAYS_23.png)

---


Pero para los __arrays__ también hay otra forma de  bucle,__for__..of:

![](imagenes/UD24%20ARRAYS_24.png)

__for__..of no da acceso al número del elemento en curso, solamente a su valor, pero en la mayoría de los casos eso es suficiente. Y es más corto. Técnicamente, y porque los __arrays__ son objetos, es también posible usar __for__..in:

Pero es una mala idea. Existen problemas potenciales con esto:

- El bucle __for__..in itera sobre todas las propiedades, no solo las numéricas.

- Existen objetos “simil-__array__” en el navegador y otros ambientes que parecen __arrays__. Esto es, tienen __length__ y propiedades indexadas, pero pueden también tener propiedades no numéricas y métodos que usualmente no necesitemos. Y el bucle __for__..in los listará. Entonces si necesitamos trabajar con objetos simil-__array__, estas propiedades “extras” pueden volverse un problema.
- El bucle __for__..in está optimizado para objetos genéricos, no para __arrays__, y es de 10 a 100 veces más lento. Por supuesto es aún muy rápido. Una optimización puede que solo sea importante en cuellos de botella, pero necesitamos ser concientes de la diferencia.

En general, no deberíamos usar __for__..in en __arrays__.

---

### Acerca de “length”

La propiedad __length__ automáticamente se actualiza cuando se modifica el __array__. Para ser precisos, no es la cuenta de valores del __array__ sino el mayor índice más uno. Por ejemplo, un elemento simple con un índice grande da una longitud grande:

![](imagenes/UD24%20ARRAYS_25.png)

**Una cosa interesante acerca de la propiedad length es que se puede sobrescribir.**

Si la incrementamos manualmente, nada interesante ocurre. Pero si la decrementamos, el __array__ se trunca. El proceso es irreversible, aquí el ejemplo:

![](imagenes/UD24%20ARRAYS_26.jpg)

Entonces la forma más simple de limpiar un __array__ es: __arr.length__ = 0;.

Hay una sintaxis más para crear un __array__:

![](imagenes/UD24%20ARRAYS_27.png)


---

Es raramente usada porque con corchetes [] es más corto. También hay una característica peculiar con ella. Si __new__ __Array__ es llamado con un único argumento numérico, se crea un __array__ sin __items__, pero con la longitud “__length__” dada. Veamos cómo uno puede dispararse en el pie:

![](imagenes/UD24%20ARRAYS_28.png)

Para evitar sorpresas solemos usar corchetes, salvo que sepamos lo que estamos haciendo.

### _Arrays multidimensionales_

Los __arrays__ pueden tener __items__ que a su vez sean __arrays__. Podemos usarlos como __arrays__ multidimensionales, por ejemplo para almacenar matrices:

![](imagenes/UD24%20ARRAYS_29.png)

---

### _toString_

Los __arrays__ tienen su propia implementación del método toString que devuelve una lista de elementos separados por coma. Por ejemplo:

![](imagenes/UD24%20ARRAYS_30.png)

Probemos esto también:

![](imagenes/UD24%20ARRAYS_31.png)

Los __arrays__ no tienen __Symbol.toPrimitive__ ni un valueOf viable, ellos implementan la conversión toString solamente, así [] se vuelve una cadena vacía, [1] se vuelve "1" y [1,2] se vuelve "1,2".

Cuando el operador binario más "+" suma algo a una cadena, lo convierte a cadena también, entonces lo siguiente se ve así:

![](imagenes/UD24%20ARRAYS_32.png)

---

### _No compares arrays con ==_

Las __arrays__ en JavaScript, a diferencia de otros lenguajes de programación, no deben ser comparadas con el operador ==. Este operador no tiene un tratamiento especial para __arrays__, trabaja con ellas como con cualquier objeto. Recordemos las reglas:

- Dos objetos son iguales == solo si hacen referencia al mismo objeto.

- Si uno de los argumentos de == es un objeto y el otro es un primitivo, entonces el objeto se convierte en primitivo, como se explica en el capítulo Conversión de objeto a valor primitivo.

…Con la excepción de __null__ y __undefined__ que son iguales == entre sí y nada más.

La comparación estricta === es aún más simple, ya que no convierte tipos. Entonces, si comparamos __arrays__ con ==, nunca son iguales, a no ser que comparemos dos variables que hacen referencia exactamente a la misma __array__. Por ejemplo:

![](imagenes/UD24%20ARRAYS_33.png)

---

Estas __arrays__ son técnicamente objetos diferentes. Así que no son iguales. El operador == no hace comparaciones de elemento a elemento. Comparaciones con primitivos también pueden dar resultados aparentemente extraños:

![](imagenes/UD24%20ARRAYS_34.png)

Aquí, en ambos casos, comparamos un primitivo con un objeto __array__. Entonces la __array__ [] se convierte a primitivo para el propósito de comparar y se convierte en una string vacía ''. Luego el proceso de comparación continúa con los primitivos, como se describe en el capítulo Conversiones de Tipos:

![](imagenes/UD24%20ARRAYS_35.jpg)

Entonces, ¿cómo comparamos __arrays__? Simple: no utilices el operador ==. En lugar, compáralas elemento a elemento en un bucle o utilizando métodos de iteración explicados en el siguiente capítulo.

---
<!-- _class: small -->
<!-- _style: "section { font-size: 0.75em; }" -->
## RESUMEN

<img src="imagenes/UD24%20ARRAYS_36.png" alt="RESUMEN" width="300" align="right" />


Los     __arrays__     son     una     clase     especial     de     objeto,     adecuados     para     almacenar     y     manejar     __items__     de     datos     ordenados.   

La     declaración:
- El llamado a __new__ __Array(number)__ crea un __array__ con la longitud dada, pero sin   elementos  .
- La propiedad __length__ es la longitud del __array__ o, para ser preciso, el último índice numérico más uno. Se autoajusta al usar los métodos de __array__.
- Si acortamos __length__ manualmente, el __array__ se trunca.

Obtener   los   elementos  :
- Podemos obtener un elemento por su índice, como __arr[0]__
- También podemos usar el método __at(i)__, que permite índices negativos. Para valores negativos de i, cuenta hacia atrás desde el final del __array__. Cuando i >=    0, funciona igual que __arr[i]__.

Podemos usar un __array__ como una pila “deque” o “bicola” con las siguientes operaciones:
- __push(...items)__ agrega __items__ al final.
- __pop()__ remueve el elemento del final y lo   devuelve  .
- __shift()__ remueve el elemento del principio y lo   devuelve  .
- __unshift(...items)__ agrega __items__ al principio.

Para iterar sobre los elementos de un __array__:
- __for__ (__let__ i=0; i<__arr.length__; i++) – lo más rápido, compatible con viejos   navegadores  .
- __for__ (__let__ __item__ of __arr__) – la sintaxis moderna para __items__   solamente  .
- __for__ (__let__ i in __arr__) – nunca lo uses.

Para comparar __arrays__, no uses el operador == (como tampoco >, < y otros), ya que no tienen un tratamiento especial para __arrays__. Lo manejan   como cualquier objeto y no es lo que normalmente queremos. En su lugar puedes utilizar el bucle __for__..of para comparar __arrays__ elemento a elemento.



---

## TAREAS

### 1. _¿El array es copiado?_ 

¿Qué     va     a     mostrar     este     código?
```js
__let__ __fruits__ = ["Apples", "Pear", "Orange"];

// introduce un valor nuevo dentro de una copia
__let__ shoppingCart = __fruits__;
shoppingCart.__push__("Banana");

// ¿Qué hay en "__fruits__"?
alert( fruits.length ); // ¿?
```

??? info "Solución"

    Este código pretende demostrar cómo funcionan las referencias a los arrays en JavaScript.

    **1. ¿Qué ocurre paso a paso?**

    ```javascript
    let fruits = ["Apples", "Pear", "Orange"];
    let shoppingCart = fruits;
    shoppingCart.push("Banana");
    alert(fruits.length);
    ```

    * `fruits` contiene un array con 3 elementos.
    * `shoppingCart = fruits` no crea una copia, ambas apuntan al mismo array.
    * `shoppingCart.push("Banana")` añade el elemento al array compartido.
    * Por tanto, `fruits` refleja el cambio y ahora tiene 4 elementos.

    **2. ¿Qué mostrará?**
    Mostrará `4`. El array final es: `["Apples", "Pear", "Orange", "Banana"]`.

    **3. ¿Cómo se podría crear una copia real?**
    Utilizando el operador de propagación (`...`):

    ```javascript
    let fruits = ["Apples", "Pear", "Orange"];
    let shoppingCart = [...fruits]; // Copia real
    shoppingCart.push("Banana");

    alert(fruits.length);       // 3
    alert(shoppingCart.length);  // 4
    ```
    

### 2. LLamados en un contexto de array 

¿Cuál     es     el     resultado     y por     qué?

```js
__let__ __arr__ = ["a", "b"];

__arr__.__push__(__function__() {
  alert( this );
});

__arr__[2](); // ?
```
??? info "Solución"

    **Resultado**
    El código va a mostrar: **`a,b,function() { alert( this ); }`** (o una representación en cadena del array).

    **Explicación paso a paso**

    1. **Estructura inicial:**
       Se crea un array `arr` con dos elementos: `["a", "b"]`.

    2. **Añadir una función:**
       Se utiliza `.push()` para añadir una función anónima al final del array (en el índice `2`):
       ```javascript
       let arr = ["a", "b"];

       arr.push(function() {
         alert( this );
       });
       ```

    3. **Invocación:**
       Al ejecutar `arr[2]()`, estás llamando a la función que se encuentra en la posición `2` del array.

    4. **El contexto (`this`):**
       En JavaScript, cuando una función se invoca como método de un objeto (en este caso, el array `arr`), **`this` apunta al objeto que la llama**, es decir, el propio array.

    5. **Resultado del `alert`:**
       Al hacer `alert(this)`, JavaScript convierte el array a cadena mediante su método `.toString()`, mostrando todos sus elementos separados por comas junto con la definición de la función.

### 3.Operaciones en arrays.

Tratemos     5     operaciones     de     __array__.

1. Crear     un     __array__     styles     con     los     __items__     “Jazz”     y     “Blues”.   

2. Agregar     “Rock-n-  Roll”     al     final.

3. Reemplazar     el     valor     en     el     medio     por     “Classics”.     Tu     código     para     encontrar     el     valor   medio     debe     funcionar     con     cualquier     __array__     de     longitud     impar.

4. Quitar     el     primer     valor     del     __array__     y     mostrarlo.  

5. Anteponer     Rap     y     Reggae     al   __array__.

El     __array__     durante     el     proceso:
```text
Jazz, Blues
Jazz, Blues, Rock-n-Roll
Jazz, Classics, Rock-n-Roll
Classics, Rock-n-Roll
Rap, Reggae, Classics, Rock-n-Roll
```

??? info "Solución"
    ```javascript
    // 1. Crear un array styles con los items “Jazz” y “Blues”.
    let styles = ["Jazz", "Blues"];

    // 2. Agregar “Rock-n-Roll” al final.
    styles.push("Rock-n-Roll");

    // 3. Reemplazar el valor en el medio por “Classics”.
    // Math.floor(styles.length / 2) encuentra el índice central para cualquier array de longitud impar.
    let middleIndex = Math.floor(styles.length / 2);
    styles[middleIndex] = "Classics";

    // 4. Quitar el primer valor del array y mostrarlo.
    let removedFirst = styles.shift();
    alert(removedFirst); // Muestra "Jazz"

    // 5. Anteponer "Rap" y "Reggae" al array.
    styles.unshift("Rap", "Reggae");

    // El array final queda de la siguiente manera:
    console.log(styles); // ["Rap", "Reggae", "Classics", "Rock-n-Roll"]
    ```

    **Explicación paso a paso:**

    1. **`styles = ["Jazz", "Blues"]`**: Inicializa el array con dos elementos.
    2. **`styles.push("Rock-n-Roll")`**: Añade el elemento al final. El array pasa a ser `["Jazz", "Blues", "Rock-n-Roll"]`.
    3. **`styles[middleIndex] = "Classics"`**: Con una longitud de `3`, `Math.floor(3 / 2)` da `1`. El elemento en el índice `1` ("Blues") es reemplazado por "Classics".
    4. **`styles.shift()`**: Extrae y elimina el primer elemento del array ("Jazz"), permitiendo guardarlo en una variable si se desea mostrar.
    5. **`styles.unshift("Rap", "Reggae")`**: Inserta ambos elementos al comienzo del array en el orden especificado.

### 4. Suma de números ingresados 

Escribe     una     función     sumInput()     que:

- VPida     al     usuario     valores     usando     prompt     y     los     almacene     en     el     __array__.     Termine     de     pedirlos     cuando     el     usuario     ingrese     un     valor     no     numérico,   una   cadena     vacía,     o     presione     “Escape”.

- Calcule     y     devuelva     la     suma     de     los     __items__     del     __array__.

P.D.     Un     cero     0     es     un     número     válido,     por     favor     no     detengas     los     ingresos     con     el     cero.


??? info "Solución"

    ```javascript
    function sumInput() {
      let numbers = [];

      while (true) {
        let value = prompt("Introduce un número:", "");

        // ¿Cuándo debemos parar?
        // 1. Si el usuario cancela (devuelve null)
        // 2. Si deja la cadena vacía ("")
        // 3. Si no es un número válido (!isFinite(value))
        // Nota: isFinite("") da true en JS, por eso comprobamos value === "" primero.
        if (value === "" || value === null || !isFinite(value)) {
          break;
        }

        // Convertimos el valor a número y lo añadimos al array
        numbers.push(Number(value));
      }

      let sum = 0;
      for (let number of numbers) {
        sum += number;
      }

      return sum;
    }

    // Ejemplo de uso:
    // alert(sumInput());
    ```

    **Explicación paso a paso:**

    1. **Bucle `while (true)`:** Permite pedir datos de forma indefinida hasta que se cumpla la condición de salida.
    2. **Validación del `prompt` (`value === "" || value === null || !isFinite(value)`):**
      * `value === null`: Se activa si el usuario pulsa **Cancelar** o **Escape**.
      * `value === ""`: Se activa si el usuario pulsa aceptar sin escribir nada.
      * `!isFinite(value)`: Comprueba que el texto introducido sea un número válido. Ten en cuenta que el `0` (cero) pasa esta validación correctamente, por lo que no detendrá el bucle.
    3. **Almacenamiento:** Con `Number(value)` o el operador unario `+value`, transformamos el texto ingresado en un número real antes de guardarlo con `.push()`.
    4. **Suma final:** Recorremos el array con un bucle `for...of` para acumular todos los valores almacenados y devolver el total.



---

### 5. Subarray máximo  

La     entrada     es     un     __array__     de     números,     por     ejemplo     __arr__     =     [1,     -  2,     3,     4,     -  9,     6]  .
La     tarea     es: encuentra     el     subarray     contiguo     de     __items__     de     __arr__     con     la   suma   máxima.
Escribe     la     función   getMaxSubSum(__arr__)     que     devuelva     tal     sumo.   Por   ejemplo:

```js
getMaxSubSum([-1, 2, 3, -9]) == 5 // la suma de __items__ resaltados
getMaxSubSum([2, -1, 2, 3, -9]) == 6
getMaxSubSum([-1, 2, 3, -9, 11]) == 11
getMaxSubSum([-2, -1, 1, 2]) == 3
getMaxSubSum([100, -9, 2, -3, 5]) == 100
getMaxSubSum([1, 2, 3]) == 6 // toma todo
```

Si     todos     los     elementos     son     negativos,     significa     que     que     no     tomamos     ninguno   (el     subarray     está     vacío),     entonces     la     suma     es     cero:

```js
getMaxSubSum([-1, -2, -3]) = 0
```

Trata     de     pensar     un     solución     rápida:     O(n  2  )     o     incluso     O(n)     si     puedes.

??? info "Solución"
      **Código de la solución (Algoritmo de Kadane - O(n))**

      ```javascript
      function getMaxSubSum(arr) {
        let maxSum = 0;
        let currentSum = 0;

        for (let item of arr) {
          currentSum += item;
          if (currentSum > maxSum) {
            maxSum = currentSum;
          }
          if (currentSum < 0) {
            currentSum = 0;
          }
        }

        return maxSum;
      }
      ```

      **Explicación paso a paso:**

      1. **Enfoque eficiente (Algoritmo de Kadane):** En lugar de probar todas las combinaciones posibles con bucles anidados (lo que tomaría $O(n^2)$), podemos resolverlo en una sola pasada con complejidad **$O(n)$**.
      2. **Variables de control:**
        * `maxSum`: Almacena la suma máxima encontrada hasta el momento (inicializada a `0` para manejar el caso donde todos los números son negativos).
        * `currentSum`: Acumula la suma del subarray actual mientras avanzamos.
      3. **Funcionamiento del bucle:**
        * Sumamos cada elemento del array a `currentSum`.
        * Si `currentSum` supera a `maxSum`, actualizamos `maxSum`.
        * Si en algún momento `currentSum` cae por debajo de `0`, significa que ese tramo negativo resta más de lo que aporta, por lo que lo reiniciamos a `0` para empezar a contar un nuevo subarray.
      4. **Resultado:** Al finalizar el recorrido, `maxSum` contendrá la mayor suma de un subarray contiguo posible.




## 2. Métodos de Arrays

Los __arrays__ (también llamados arreglos o matrices) cuentan con muchos métodos. Para hacer las cosas más sencillas, en este capítulo se encuentran divididos en dos partes.

### _Agregar_    _/remover ítems_ 

Ya conocemos algunos métodos que agregan o extraen elementos del inicio o final de un __array__:

* __arr.push__  (...__items__) – agrega ítems al final,
* __arr.pop__  () – extrae un ítem del final,
* __arr.shift__  () – extrae un ítem del inicio,
* __arr.unshift__  (...__items__) – agrega ítems al principio.

¿Cómo podemos borrar un elemento de un __array__? Los __arrays__ son objetos, por lo que podemos intentar con  __delete__:

![](imagenes/UD24%20ARRAYS_37.png)

El elemento fue borrado, pero el __array__ todavía tiene 3 elementos; podemos ver que __arr.length__ == 3.

Es natural, porque __delete__ __obj.key__ borra el valor de __key__, pero es todo lo que hace. Esto está bien en los objetos, pero en general lo que buscamos en los __arrays__ es que el resto de los elementos se desplace y se ocupe el lugar libre. Lo que esperamos es un __array__ más corto. Por lo tanto, necesitamos utilizar métodos especiales.

---

El método __arr.splice__ funciona como una navaja suiza para __arrays__. Puede hacer todo: insertar, remover y remplazar elementos. La sintaxis es:

<img src="imagenes/UD24%20ARRAYS_38.png" width="300">

Esto modifica __arr__ comenzando en el índice __start__: remueve la cantidad deleteCount de elementos y luego inserta elem1, ..., elemN en su lugar. Lo que devuelve es un __array__ de los elementos removidos.

Este método es más fácil de entender con ejemplos. Empecemos removiendo elementos:

<img src="imagenes/UD24%20ARRAYS_39.jpg" width="300">

¿Fácil, no? Empezando desde el índice 1 removió 1 elemento. En el próximo ejemplo removemos 3 elementos y los reemplazamos con otros 2:

<img src="imagenes/UD24%20ARRAYS_40.jpg" width="300">

Aquí podemos ver que __splice__ devuelve un __array__ con los elementos removidos:

<img src="imagenes/UD24%20ARRAYS_41.jpg" width="300">

El método __splice__ también es capaz de insertar elementos sin remover ningún otro. Para eso necesitamos establecer __deleteCount__ en 0:

<img src="imagenes/UD24%20ARRAYS_42.jpg" width="400">

---


El método __arr.slice__ es mucho más simple que __arr.splice__. La sintaxis es:

<img src="imagenes/UD24%20ARRAYS_43.png" width="300">


Devuelve un nuevo __array__ copiando en el mismo todos los elementos desde principio hasta final (sin incluir final). principio y final pueden ser negativos, en cuyo caso se asume la posición desde el final del __array__.

Es similar al método para strings __str.slice__, pero en lugar de substrings genera subarrays. Por ejemplo:

<img src="imagenes/UD24%20ARRAYS_44.jpg" width="300">

También podemos invocarlo sin argumentos: __arr.slice()__ crea una copia de __arr__. Se utiliza a menudo para obtener una copia que se puede transformar sin afectar el __array__ original.

El método __arr.concat__ crea un nuevo __array__ que incluye los valores de otros __arrays__ y elementos adicionales. La sintaxis es:

<img src="imagenes/UD24%20ARRAYS_45.png" width="300">

Este acepta cualquier número de argumentos, tanto __arrays__ como valores.

El resultado es un nuevo __array__ conteniendo los elementos de __arr__, después arg1, arg2 etc. Si un argumento argN es un __array__, entonces todos sus elementos son copiados. De otro modo el argumento en sí es copiado. Por ejemplo:
<img src="imagenes/UD24%20ARRAYS_46.jpg" width="300">

---


Normalmente, solo copia elementos desde __arrays__. Otros objetos, incluso si parecen __arrays__, son agregados como un todo:

<img src="imagenes/UD24%20ARRAYS_47.png" width="300">

…Pero si un objeto similar a un __array__ tiene la propiedad especial __Symbol.isConcatSpreadable__, entonces __concat__ lo trata como un __array__ y en lugar de añadirlo como un todo, solo añade sus elementos.
<img src="imagenes/UD24%20ARRAYS_48.png" width="300">
### _Iteración: forEach_

El método __arr.forEach__ permite ejecutar una función a cada elemento del __array__. La sintaxis:

<img src="imagenes/UD24%20ARRAYS_49.png" width="300">

Por ejemplo, el siguiente código muestra cada elemento del __array__:

<img src="imagenes/UD24%20ARRAYS_50.png" width="300">

Y este caso más detallado da la posición del elemento en el __array__:
<img src="imagenes/UD24%20ARRAYS_51.jpg" width="300">

El resultado de la función (si lo hay) se descarta y se ignora.


---

### _Buscar dentro de un array_

Ahora vamos a ver métodos que buscan elementos dentro de un __array__.
___indexOf__/__lastIndexOf__ e __includes___

Los métodos __arr.indexOf__ y __arr.includes__ tienen una sintaxis similar y hacen básicamente lo mismo que sus contrapartes de __strings__, pero operan sobre elementos en lugar de caracteres:

* __arr.indexOf(item, from)__ – busca __item__ comenzando desde el __index__ __from__, y devuelve el __index__ donde fue encontrado, de otro modo devuelve -1.

* __arr.includes(item, from)__ – busca __item__ comenzando desde el índice __from__, devuelve __true__ en caso de ser encontrado.

Usualmente estos métodos se usan con un solo argumento: el __item__ a buscar.

De manera predeterminada, la búsqueda es desde el principio. Por ejemplo:

<img src="imagenes/UD24%20ARRAYS_52.png" width="200">

Tener en cuenta que el método usa la comparación estricta (===). Por lo tanto, si buscamos __false__, encontrará exactamente __false__ y no cero. Si queremos comprobar si un elemento existe en el __array__, pero no necesitamos saber su ubicación exacta, es preferible usar __arr.includes__

El método __arr.lastIndexOf__ es lo mismo que __indexOf__, pero busca de derecha a izquierda.

<img src="imagenes/UD24%20ARRAYS_53.jpg" width="300">

---
### _find y findIndex / findLastIndex_

Imaginemos que tenemos un __array__ de objetos. ¿Cómo podríamos encontrar un objeto con una condición específica? Para este tipo de casos es útil el método __arr.find(fn)__. La sintaxis es:

<img src="imagenes/UD24%20ARRAYS_54.jpg" width="400">

La función es llamada para cada elemento del __array__, uno después del otro:

* __item__ es el elemento.
* __index__ es su índice.
* __array__ es el __array__ mismo.

Si devuelve __true__, la búsqueda se detiene y el __item__ es devuelto. Si no encuentra nada, entonces devuelve __undefined__. Por ejemplo, si tenemos un __array__ de usuarios, cada uno con los campos id y name. Encontremos el elemento con id == 1:

<img src="imagenes/UD24%20ARRAYS_55.png" width="300">

En la vida real los arrays de objetos son bastante comunes por lo que el método __find__ resulta muy útil. Tened en cuenta que en el ejemplo anterior le pasamos a __find__ la función __item__ => __item.id__ == 1 con un argumento. Esto es lo más común, otros argumentos son raramente usados en esta función.

---

El método __arr.findIndex__ tiene la misma sintaxis, pero devuelve el índice donde el elemento fue encontrado en lugar del elemento en sí. Devuelve -1 cuando no lo encuentra.

El método __arr.findLastIndex__ es como __findIndex__, pero busca de derecha a izquierda, similar a __lastIndexOf__.

Un ejemplo:

<img src="imagenes/UD24%20ARRAYS_56.jpg" width="300">

El método __find__ busca un único elemento (el primero) que haga a la función devolver __true__. Si existieran varios elementos que cumplen la condición, podemos usar __arr.filter(fn)__. La sintaxis es similar a __find__, pero __filter__ devuelve un __array__ con todos los elementos encontrados:

<img src="imagenes/UD24%20ARRAYS_57.jpg" width="300">

<img src="imagenes/UD24%20ARRAYS_58.png" width="300">


---

## 3. Transformar un array

Pasamos ahora a los métodos que transforman y reordenan un __array__.

### Map

El método __arr.map__ es uno de los métodos más comunes y ampliamente usados. Este método llama a la función para cada elemento del __array__ y devuelve un __array__ con los resultados. La sintaxis es:

<img src="imagenes/UD24%20ARRAYS_59.png" width="300">

Por ejemplo, acá transformamos cada elemento en el valor de su respectivo largo (__length__):

<img src="imagenes/UD24%20ARRAYS_60.jpg" width="300">

Cuando usamos __arr.sort()__, este ordena el propio __array__ cambiando el orden de los elementos. También devuelve un nuevo __array__ ordenado, pero este usualmente se descarta ya que __arr__ en sí mismo es modificado. Por ejemplo:

<img src="imagenes/UD24%20ARRAYS_61.png" width="300">

¿Notas algo extraño en los valores de salida? Los elementos fueron reordenados a 1, 15, 2. Pero

¿por qué pasa esto? Los elementos son ordenados como __strings__ (cadenas de caracteres) por defecto

Todos los elementos son literalmente convertidos a __string__ para ser comparados. En el caso de __strings__ se aplica el orden lexicográfico, por lo que efectivamente "2" > "15". Para usar nuestro propio criterio de reordenamiento, necesitamos proporcionar una función como argumento de __arr.sort()__.

---


La función debe comparar dos valores arbitrarios, y devolver:

<img src="imagenes/UD24%20ARRAYS_62.jpg" width="300">

Por ejemplo, para ordenar como números:

<img src="imagenes/UD24%20ARRAYS_63.png" width="300">

Ahora sí funciona como esperábamos.

Detengámonos un momento y pensemos qué es lo que está pasando. El __array__ __arr__ puede ser un __array__ de cualquier cosa, ¿no? Puede contener números, __strings__, objetos o lo que sea. Podemos decir que tenemos un conjunto de ciertos __items__. Para ordenarlos, necesitamos una función de ordenamiento que sepa cómo comparar los elementos. El orden por defecto es hacerlo como strings.

El  método  __arr.sort(fn)__  implementa  un  algoritmo  genérico  de  orden.  No  necesitamos preocuparnos de cómo funciona internamente (la mayoría de las veces es una forma optimizada del algoritmo quicksort o Timsort). Este método va a recorrer el __array__, comparar sus elementos usando la función dada y, finalmente, reordenarlos. Todo los que necesitamos hacer es proveer la __fn__ que realiza la comparación.

---

Por cierto, si queremos saber qué elementos son comparados, nada nos impide ejecutar __alert__() en ellos:

<img src="imagenes/UD24%20ARRAYS_64.png" width="300">

El algoritmo puede comparar un elemento con muchos otros en el proceso, pero trata de hacer la menor cantidad de comparaciones posible.

El método __arr.reverse__ revierte el orden de los elementos en __arr__. Por ejemplo:

<img src="imagenes/UD24%20ARRAYS_65.png" width="300">

También devuelve el __array__ __arr__ después de revertir el orden.

Analicemos una situación de la vida real. Estamos programando una app de mensajería y y el usuario ingresa una lista de receptores delimitada por comas: Celina, David, Federico. Pero para nosotros un __array__ sería mucho más práctico que una simple string. ¿Cómo podemos hacer para obtener un __array__?

El método __str.split(delim)__ hace precisamente eso. Separa la __string__ en elementos según el delimitante __delim__ dado y los devuelve como un __array__. En el ejemplo de abajo, separamos por “coma seguida de espacio”:

<img src="imagenes/UD24%20ARRAYS_66.jpg" width="300">

El método __split__ tiene un segundo argumento numérico opcional: un límite en la extensión del __array__. Si se provee este argumento, entonces el resto de los elementos son ignorados. Sin embargo en la práctica rara vez se utiliza:

<img src="imagenes/UD24%20ARRAYS_67.jpg" width="300">

---


__arr.join(glue)__ hace lo opuesto a __split__. Crea una __string__ de __arr__ elementos unidos con __glue__ (pegamento) entre ellos. Por ejemplo:

<img src="imagenes/UD24%20ARRAYS_68.jpg" width="300">

### _Reduce/reduceRight_

Cuando necesitamos iterar sobre un __array__ podemos usar __forEach__, __for__ o __for__..of. Cuando necesitamos iterar y devolver un valor por cada elemento podemos usar __map__.

Los métodos __arr.reduce__ y __arr.reduceRight__ también pertenecen a ese grupo de acciones, pero son un poco más complejos. Se los utiliza para calcular un único valor a partir del __array__. La sintaxis es la siguiente:

<img src="imagenes/UD24%20ARRAYS_69.jpg" width="300">

La función es aplicada a todos los elementos del __array__, uno tras de otro, y va arrastrando el resultado parcial al próximo llamado. Argumentos:

* __accumulator__ – es el resultado del llamado previo de la función, equivale a __initial__ la primera vez (si __initial__ es dado como argumento).
* __item__ – es el elemento actual del __array__.
* __index__ – es la posición.
* __array__ – es el __array__.

Mientras la función sea llamada, el resultado del llamado anterior se pasa al siguiente como primer argumento. Entonces, el primer argumento es el acumulador que almacena el resultado combinado de todas las veces anteriores en que se ejecutó, y al final se convierte en el resultado de __reduce__.

---

La forma más simple de entender algo es con un ejemplo.

AQUÍ tenemos la suma de un __array__ en una línea:
<img src="imagenes/UD24%20ARRAYS_70.jpg" width="300">

La función pasada a __reduce__ utiliza solo 2 argumentos, esto generalmente es suficiente.

Veamos los detalles de lo que está pasando.

1. En la primera pasada, __sum__ es el valor __initial__ (el último argumento de __reduce__), equivale a 	0, y __current__ es el primer elemento de __array__, equivale a 1. Entonces el resultado de la 	función es 1.
2. En la segunda pasada, __sum__ = 1, agregamos el segundo elemento del __array__ (2) y 	devolvemos el valor.
3. En la tercera pasada, __sum__ = 3 y le agregamos un elemento más, y así sucesivamente…

El flujo de cálculos:

<img src="imagenes/UD24%20ARRAYS_71.jpg" width="300">

O en la forma de una tabla, donde cada fila representa un llamado a una función en el próximo elemento del __array__:

<img src="imagenes/UD24%20ARRAYS_72.png" width="300">

Acá podemos ver claramente como el resultado del llamado anterior se convierte en el primer argumento del llamado siguiente. También podemos omitir el valor inicial:

<img src="imagenes/UD24%20ARRAYS_73.jpg" width="300">

El resultado es el mismo. Esto es porque en el caso de no haber valor inicial, __reduce__ toma el primer elemento del __array__ como valor inicial y comienza la iteración a partir del segundo elemento.

---

La tabla de cálculos es igual a la anterior menos la primer fila. Pero este tipo de uso requiere tener extremo cuidado. Si el __array__ está vacío, entonces el llamado a __reduce__ sin valor inicial devuelve error. Acá vemos un ejemplo:

<img src="imagenes/UD24%20ARRAYS_74.jpg" width="300">

Por lo tanto siempre se recomienda especificar un valor inicial. El método __arr.reduceRight__ realiza lo mismo, pero va de derecha a izquierda.

Los __arrays__ no conforman un tipo diferente. Están basados en objetos. Por eso __typeof__ no ayuda a distinguir un objeto común de un __array__:

<img src="imagenes/UD24%20ARRAYS_75.png" width="300">

…Pero los __arrays__ son utilizados tan a menudo que tienen un método especial para eso: __Array.isArray(value)__. Este devuelve __true__ si el valor es un __array__ y __false__ si no lo es.

<img src="imagenes/UD24%20ARRAYS_76.png" width="300">

## La mayoría de los métodos aceptan “thisArg”

Casi todos los métodos para __arrays__ que realizan llamados a funciones – como __find__, __filter__, __map__, con la notable excepción de __sort__– aceptan un parámetro opcional adicional thisArg.

Ese parámetro no está explicado en la sección anterior porque es raramente usado. Pero para ser exhaustivos necesitamos verlo. Esta es la sintaxis completa de estos métodos:

<img src="imagenes/UD24%20ARRAYS_77.png" width="300">

EL valor del parámetro __thisArg__ se convierte en __this__ para func. Por ejemplo, acá usamos un método del objeto __army__ como un filtro y __thisArg__ da el contexto:

<img src="imagenes/UD24%20ARRAYS_78.jpg" width="300">

Si en el ejemplo anterior usáramos __users.filter(army.canJoin)__, entonces __army.canJoin__ sería llamada como una función independiente con __this__=__undefined__, lo que llevaría a un error inmediato.

La llamada a __users__.filter(army.canJoin, army) puede ser reemplazada con __users__.filter(__user__ => army.canJoin(__user__)) que realiza lo mismo. Esta última se usa más a menudo ya que es un poco más fácil de entender.

---

## RESUMEN

Para agregar/remover elementos:

* __push(...items)__ – agrega ítems al final,
* __pop()__ – extrae un ítem del final,
* __shift()__ – extrae un ítem del inicio,
* __unshift(...items)__ – agrega ítems al inicio.
* __splice(pos, deleteCount, ...items)__ – desde el índice __pos__ borra __deleteCount__ elementos e inserta __items__.
* __slice(start, end)__ – crea un nuevo __array__ y copia elementos desde la posición __start__ hasta __end__ (no incluido) en el nuevo __array__.
* __concat__  (...__items__) – devuelve un nuevo __array__: copia todos los elementos del __array__ actual y le agrega __items__. Si alguno de los __items__ es un __array__, se toman sus elementos.

Para buscar entre elementos:

* __indexOf__  /__lastIndexOf(item, pos)__ – busca por __item__ comenzando desde la posición __pos__, devolviendo el índice o -1 si no se encuentra.
* __includes(value)__ – devuelve __true__ si el __array__ tiene __value__, si no __false__.
* __find__/__filter(func)__ – filtra elementos a través de la función, devuelve el primer/todos los valores que devuelven __true__.
* __findIndex__   es similar a __find__, pero devuelve el índice en lugar del valor.

Para   iterar sobre elementos:

* __forEach__  (__func__) – llama la __func__ para cada elemento, no devuelve nada.

Para transformar el __array__:

* __map(func)__ – crea un nuevo __array__ a partir de los resultados de llamar a la __func__ para cada elemento
* __sort(func)__ – ordena el __array__ y lo devuelve.
* __reverse()__ – ordena el __array__ de forma inversa y lo devuelve.
* __split/join__ – convierte una cadena en un __array__ y   viceversa  .
* __reduce/reduceRight(func, initial)__ – calcula un solo valor para todo el __array__, llamando a la __func__ para cada elemento, obteniendo un resultado parcial en cada llamada y   pasándolo a la siguiente.


---

Adicional:

* __Array.isArray__  (__value__) comprueba si __value__ es un __array__.

Por favor tener en cuenta que __sort__, __reverse__ y __splice__ modifican el propio __array__. Estos métodos son los más utilizados y cubren el 99% de los casos. Pero existen algunos más:

* __arr.some__  (__fn__)/__arr.every(fn)__ comprueba el __array__.

La función __fn__ es llamada para cada elemento del __array__ de manera similar a __map__. Si alguno/todos      los resultados son __true__, devuelve __true__, si no, __false__.

Estos   métodos se comportan con similitud a los operadores || y &&: si __fn__ devuelve un valor verdadero,   __arr.some()__ devuelve __true__ y detiene la iteración de inmediato; si __fn__ devuelve un valor falso, __arr.every()__ devuelve __false__ y detiene la iteración también.

Podemos usar __every__ para comparar __arrays__:

```js
function arraysEqual(arr1, arr2) {
  return arr1.length === arr2.length && arr1.every((value, index) => value === arr2[index]);
}

alert( arraysEqual([1, 2], [1, 2])); // true
```
* __arr.fill__  (__value__, __start__, __end__) – llena el __array__ repitiendo __value__ desde el índice __start__ hasta end.
* __arr.copyWithin__  (__target__, __start__, __end__) – copia sus elementos desde la posición __start__ hasta la posición __end__ en si mismo, a     la posición __target__ (reescribe lo existente).

__arr.flat__  (__depth__)/__arr.flatMap(fn)__ crea un nuevo __array__ plano desde un __array__ multidimensional.



A primera vista puede parecer que hay demasiados métodos para aprender y un tanto difíciles de    recordar. Pero con el tiempo se vuelve más fácil. Revisa el ayudamemoria para conocerlos. Después realiza las prácticas de este capítulo para ganar experiencia con los métodos para __arrays__.

Finalmente   si en algún momento necesitas hacer algo con un __array__ y no sabes cómo, vuelve a esta    página, mira el ayudamemoria y encuentra el método correcto. Los ejemplos te ayudarán a escribirlos correctamente y pronto los recordarás automáticamente y sin esfuerzo.


---

## TAREAS
### 6. Transforma border-left-width en borderLeftWidth

Escribe la función **`camelize(str)`** que convierta palabras separadas por guiones, como `"mi-cadena-corta"`, en palabras con mayúscula después de cada guion: `"miCadenaCorta"`.

Esto consiste en eliminar los guiones y hacer que cada palabra después de un guion comience con mayúscula.

Ejemplos:

```js
camelize("background-color"); // "backgroundColor"
camelize("list-style-image"); // "listStyleImage"
camelize("-webkit-transition"); // "WebkitTransition"
```

**Pista:** usa `split()` para dividir el string en un array, transfórmalo y vuelve a unirlo con `join()`.

??? success "Solución"

    ```js
    function camelize(str) {
      return str
        .split("-")
        .map((word, index) => {
          if (index === 0) return word;
          return word ? word[0].toUpperCase() + word.slice(1) : "";
        })
        .join("");
    }

    console.log(camelize("background-color")); // "backgroundColor"
    console.log(camelize("list-style-image")); // "listStyleImage"
    console.log(camelize("-webkit-transition")); // "WebkitTransition"
    ```

    **Explicación:**

    - `split("-")` divide la cadena por los guiones.
    - `map()` recorre las palabras resultantes.
    - La primera palabra se mantiene igual; en las siguientes, se convierte la primera letra en mayúscula y se conserva el resto.
    - La comprobación `word ? ... : ""` evita problemas con palabras vacías, como cuando la cadena comienza por un guion.
    - `join("")` une las palabras sin añadir guiones.

---

### 7. Filtrar un rango

Escribe una función `filterRange(arr, a, b)` que reciba un array `arr`, busque los elementos con valor mayor o igual que `a` y menor o igual que `b`, y devuelva un nuevo array con los resultados.

La función no debe modificar el array original.

```javascript
let arr = [5, 3, 8, 1];

let filtered = filterRange(arr, 1, 4);

console.log(filtered); // [3, 1]
console.log(arr);      // [5, 3, 8, 1] (el array original no cambia)
```

??? success "Solución"

    ```js
    function filterRange(arr, a, b) {
      return arr.filter(value => value >= a && value <= b);
    }

    let arr = [5, 3, 8, 1];
    let filtered = filterRange(arr, 1, 4);

    console.log(filtered); // [3, 1]
    console.log(arr);      // [5, 3, 8, 1]
    ```

    **Explicación:**

    - `filter()` crea un array nuevo con los elementos que cumplen la condición.
    - `value >= a && value <= b` comprueba que el valor esté dentro del rango, incluidos los extremos.
    - El array original no se modifica.

---

### 8. Filtrar un rango

Escribe una función `filterRangeInPlace(arr, a, b)` que elimine del propio array todos los valores excepto aquellos que estén entre `a` y `b`, ambos incluidos.

La función debe modificar el array original y no debe devolver nada.

```js
let arr = [5, 3, 8, 1];

filterRangeInPlace(arr, 1, 4);

console.log(arr); // [3, 1]
```

??? success "Solución"

    ```js
    function filterRangeInPlace(arr, a, b) {
      for (let i = arr.length - 1; i >= 0; i--) {
        if (arr[i] < a || arr[i] > b) {
          arr.splice(i, 1);
        }
      }
    }

    let arr = [5, 3, 8, 1];
    filterRangeInPlace(arr, 1, 4);

    console.log(arr); // [3, 1]
    ```

    **Explicación:**

    - Se recorre el array desde el final hacia el principio.
    - Si un elemento está fuera del rango, `splice(i, 1)` lo elimina.
    - Se recorre hacia atrás para que la eliminación de un elemento no desplace los índices que todavía hay que revisar.
    - La función modifica `arr` directamente y no necesita devolver un resultado.

---

### 9. Ordenar en orden decreciente

Ordena el array de mayor a menor.

```js
let arr = [5, 2, 1, -10, 8];

// ... tu código para ordenar en orden decreciente

console.log(arr); // [8, 5, 2, 1, -10]
```

??? success "Solución"

    ```js
    let arr = [5, 2, 1, -10, 8];

    arr.sort((a, b) => b - a);

    console.log(arr); // [8, 5, 2, 1, -10]
    ```

    **Explicación:**

    - `sort()` ordena el array original.
    - La función comparadora `b - a` coloca primero los números mayores.
    - Si no se proporciona una función comparadora, `sort()` ordena los elementos como cadenas de texto, lo que puede dar resultados incorrectos con números.

---

### 12. Copia y ordena un array

Supongamos que tenemos un array `arr`. Nos gustaría obtener una copia ordenada del mismo, pero mantener `arr` sin modificar.

Crea una función `copySorted(arr)` que devuelva esa copia.

```js
let arr = ["HTML", "JavaScript", "CSS"];

let sorted = copySorted(arr);

console.log(sorted); // ["CSS", "HTML", "JavaScript"]
console.log(arr);    // ["HTML", "JavaScript", "CSS"] (sin cambios)
```

??? success "Solución"

    ```js
    function copySorted(arr) {
      return [...arr].sort();
    }

    let arr = ["HTML", "JavaScript", "CSS"];
    let sorted = copySorted(arr);

    console.log(sorted); // ["CSS", "HTML", "JavaScript"]
    console.log(arr);    // ["HTML", "JavaScript", "CSS"]
    ```

    **Explicación:**

    - `[...arr]` crea una copia superficial del array.
    - `sort()` ordena la copia.
    - El array original permanece sin cambios.
    - También se podría utilizar `arr.slice().sort()`.

---

### 10. Mapa a nombres

Tienes un array de objetos `user`, cada uno con la propiedad `name`. Escribe el código que lo convierta en un array de nombres.

```js
let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };

let users = [john, pete, mary];

let names = /* tu código */;

console.log(names); // ["John", "Pete", "Mary"]
```

??? success "Solución"

    ```js
    let john = { name: "John", age: 25 };
    let pete = { name: "Pete", age: 30 };
    let mary = { name: "Mary", age: 28 };

    let users = [john, pete, mary];

    let names = users.map(user => user.name);

    console.log(names); // ["John", "Pete", "Mary"]
    ```

    **Explicación:**

    - `map()` crea un nuevo array transformando cada elemento.
    - En cada iteración, `user` representa uno de los objetos.
    - `user.name` obtiene la propiedad `name`.
    - El array original `users` no se modifica.

---

### 11. Crea una calculadora extensible

Crea una función constructora o una clase `Calculator` que permita crear calculadoras extensibles.

La actividad tiene dos partes.

**Primera parte:** implementar el método `calculate(str)`, que recibe una cadena como `"1 + 2"` en el formato `NÚMERO operador NÚMERO` y devuelve el resultado. Inicialmente debe entender los operadores `+` y `-`.

Ejemplo de uso:

```js
let calc = new Calculator();

console.log(calc.calculate("3 + 7")); // 10
```

**Segunda parte:** agrega el método `addMethod(name, func)`, que permita incorporar una nueva operación. Recibe el nombre del operador y una función `func(a, b)` que implementa la operación.

Por ejemplo, para añadir multiplicación, división y potencia:

```js
let powerCalc = new Calculator();

powerCalc.addMethod("*", (a, b) => a * b);
powerCalc.addMethod("/", (a, b) => a / b);
powerCalc.addMethod("**", (a, b) => a ** b);

let result = powerCalc.calculate("2 ** 3");

console.log(result); // 8
```

- No se necesitan paréntesis ni expresiones complejas.
- Los números y el operador deben estar delimitados por exactamente un espacio.
- Se pueden añadir comprobaciones de errores.

??? success "Solución"

    ```js
    class Calculator {
      constructor() {
        this.methods = {
          "+": (a, b) => a + b,
          "-": (a, b) => a - b
        };
      }

      addMethod(name, func) {
        this.methods[name] = func;
      }

      calculate(str) {
        const [left, operator, right] = str.split(" ");

        const a = Number(left);
        const b = Number(right);
        const operation = this.methods[operator];

        if (!Number.isFinite(a) || !Number.isFinite(b)) {
          throw new Error("Los operandos deben ser números.");
        }

        if (!operation) {
          throw new Error(`Operador no reconocido: ${operator}`);
        }

        return operation(a, b);
      }
    }

    let calc = new Calculator();
    console.log(calc.calculate("3 + 7")); // 10

    let powerCalc = new Calculator();
    powerCalc.addMethod("*", (a, b) => a * b);
    powerCalc.addMethod("/", (a, b) => a / b);
    powerCalc.addMethod("**", (a, b) => a ** b);

    console.log(powerCalc.calculate("2 ** 3")); // 8
    ```

    **Explicación:**

    - El constructor crea el objeto `methods`, que relaciona cada operador con su función.
    - `addMethod()` guarda una nueva función asociada al operador indicado.
    - `split(" ")` divide la expresión en operando izquierdo, operador y operando derecho.
    - `Number()` convierte los operandos a números.
    - `calculate()` busca la función correspondiente y la ejecuta con `a` y `b`.
    - Las comprobaciones muestran un error si los operandos no son números válidos o si el operador no está definido.

    **Idea clave:** la calculadora se puede ampliar sin tener que modificar `calculate()` cada vez que se incorpora una operación.

---

### 15. Mapa a objetos

Tienes un array de usuarios, cada uno con las propiedades `name`, `surname` e `id`.

Crea otro array con objetos que tengan `id` y `fullName`, donde `fullName` se genere a partir de `name` y `surname`.

```js
let john = { name: "John", surname: "Smith", id: 1 };
let pete = { name: "Pete", surname: "Hunt", id: 2 };
let mary = { name: "Mary", surname: "Key", id: 3 };

let users = [john, pete, mary];

let usersMapped = /* tu código */;

// usersMapped debería ser:
// [
//   { fullName: "John Smith", id: 1 },
//   { fullName: "Pete Hunt", id: 2 },
//   { fullName: "Mary Key", id: 3 }
// ]

console.log(usersMapped[0].id);       // 1
console.log(usersMapped[0].fullName); // "John Smith"
```

Intenta utilizar una función flecha. Hay un pequeño detalle al devolver objetos.

??? success "Solución"

    ```js
    let john = { name: "John", surname: "Smith", id: 1 };
    let pete = { name: "Pete", surname: "Hunt", id: 2 };
    let mary = { name: "Mary", surname: "Key", id: 3 };

    let users = [john, pete, mary];

    let usersMapped = users.map(user => ({
      fullName: `${user.name} ${user.surname}`,
      id: user.id
    }));

    console.log(usersMapped[0].id);       // 1
    console.log(usersMapped[0].fullName); // "John Smith"
    ```

    **Explicación:**

    - `map()` transforma cada objeto del array original en un objeto nuevo.
    - La plantilla `${user.name} ${user.surname}` crea el nombre completo.
    - Se conservan las propiedades `id` y `fullName`; no se copian las demás propiedades.
    - Los paréntesis de `({ ... })` son necesarios para que JavaScript interprete las llaves como un objeto que devuelve la función flecha.
    - El array original y sus objetos no se modifican.

---

### 12. Ordena usuarios por edad

Escribe la función `sortByAge(users)` que ordene un array de objetos según la propiedad `age`, de menor a mayor.

```js
let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };

let arr = [pete, john, mary];

sortByAge(arr);

// Ahora el orden debe ser: [john, mary, pete]

console.log(arr[0].name); // "John"
console.log(arr[1].name); // "Mary"
console.log(arr[2].name); // "Pete"
```

??? success "Solución"

    ```js
    function sortByAge(users) {
      users.sort((a, b) => a.age - b.age);
    }

    let john = { name: "John", age: 25 };
    let pete = { name: "Pete", age: 30 };
    let mary = { name: "Mary", age: 28 };

    let arr = [pete, john, mary];

    sortByAge(arr);

    console.log(arr[0].name); // "John"
    console.log(arr[1].name); // "Mary"
    console.log(arr[2].name); // "Pete"
    ```

    **Explicación:**

    - `sort()` ordena el array original.
    - La función comparadora `a.age - b.age` coloca primero al usuario con menor edad.
    - No hace falta devolver el array porque se modifica directamente.
    - Para ordenar de mayor a menor, se podría utilizar `b.age - a.age`.

---

### 13. Obtener edad promedio

Escribe la función `getAverageAge(users)`, que reciba un array de objetos con la propiedad `age` y devuelva el promedio de las edades.

La fórmula es:

`(edad1 + edad2 + ... + edadN) / N`

```js
let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 29 };

let arr = [john, pete, mary];

console.log(getAverageAge(arr)); // 28
```

??? success "Solución"

    ```js
    function getAverageAge(users) {
      if (users.length === 0) return 0;

      const total = users.reduce(
        (sum, user) => sum + user.age,
        0
      );

      return total / users.length;
    }

    let john = { name: "John", age: 25 };
    let pete = { name: "Pete", age: 30 };
    let mary = { name: "Mary", age: 29 };

    let arr = [john, pete, mary];

    console.log(getAverageAge(arr)); // 28
    ```

    **Explicación:**

    - `reduce()` recorre el array y acumula la suma de las edades.
    - `sum` es el acumulador y `user` es el objeto que se está procesando.
    - El `0` es el valor inicial del acumulador.
    - La suma se divide entre el número de usuarios.
    - Si el array está vacío, esta implementación devuelve `0` para evitar dividir entre cero.

---

### 14. Barajar un array

Escribe la función `shuffle(array)` que baraje o reordene aleatoriamente los elementos del array.

Las distintas permutaciones deben tener la misma probabilidad.

```js
let arr = [1, 2, 3];

shuffle(arr);
console.log(arr); // Por ejemplo: [3, 2, 1]

shuffle(arr);
console.log(arr); // Puede aparecer otro orden
```

??? success "Solución"

    ```js
    function shuffle(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));

        [array[i], array[j]] = [array[j], array[i]];
      }
    }

    let arr = [1, 2, 3];

    shuffle(arr);
    console.log(arr); // El orden será aleatorio
    ```

    **Explicación:**

    - Se recorre el array desde el último índice hasta el segundo.
    - En cada paso se elige aleatoriamente un índice entre `0` e `i`, ambos incluidos.
    - La asignación múltiple intercambia los elementos de las posiciones `i` y `j`.
    - Este algoritmo se conoce como **Fisher–Yates** y, si la selección aleatoria es uniforme, genera permutaciones con la misma probabilidad.
    - La función modifica el array original.

---

### 15. Filtrar elementos únicos de un array

Partiendo de un array `arr`, crea una función `unique(arr)` que devuelva un array con los elementos que aparecen una sola vez en el resultado, eliminando los duplicados.

```js
function unique(arr) {
  /* tu código */
}

let strings = [
  "Hare", "Krishna", "Hare", "Krishna",
  "Krishna", "Krishna", "Hare", "Hare", ":-O"
];

console.log(unique(strings)); // ["Hare", "Krishna", ":-O"]
```

??? success "Solución"

    ```js
    function unique(arr) {
      return [...new Set(arr)];
    }

    let strings = [
      "Hare", "Krishna", "Hare", "Krishna",
      "Krishna", "Krishna", "Hare", "Hare", ":-O"
    ];

    console.log(unique(strings)); // ["Hare", "Krishna", ":-O"]
    ```

    **Explicación:**

    - `Set` almacena valores únicos y descarta los duplicados.
    - `new Set(arr)` crea una colección a partir de los valores del array.
    - `[...new Set(arr)]` convierte la colección en un nuevo array.
    - Se conserva el orden de la primera aparición de cada valor.
    - El array original no se modifica.

---

### 16. Crea un objeto a partir de un array

Supongamos que recibimos un array de usuarios con la forma `{ id: ..., name: ..., age: ... }`.

Crea una función `groupById(arr)` que construya un objeto donde cada clave sea el `id` y cada valor sea el objeto de usuario correspondiente.

```js
let users = [
  { id: "john", name: "John Smith", age: 20 },
  { id: "ann", name: "Ann Smith", age: 24 },
  { id: "pete", name: "Pete Peterson", age: 31 }
];

let usersById = groupById(users);

// El resultado tendrá esta estructura:
// {
//   john: { id: "john", name: "John Smith", age: 20 },
//   ann: { id: "ann", name: "Ann Smith", age: 24 },
//   pete: { id: "pete", name: "Pete Peterson", age: 31 }
// }
```

Para esta actividad, asumimos que cada `id` es único. Utiliza el método de array `reduce()`.

??? success "Solución"

    ```js
    function groupById(arr) {
      return arr.reduce((result, user) => {
        result[user.id] = user;
        return result;
      }, {});
    }

    let users = [
      { id: "john", name: "John Smith", age: 20 },
      { id: "ann", name: "Ann Smith", age: 24 },
      { id: "pete", name: "Pete Peterson", age: 31 }
    ];

    let usersById = groupById(users);

    console.log(usersById);
    ```

    **Explicación:**

    - `reduce()` recorre el array y construye un único resultado.
    - `{}` es el objeto inicial que actúa como acumulador.
    - `result[user.id] = user` guarda cada objeto usando su `id` como clave.
    - `return result` devuelve el acumulador para la siguiente iteración.
    - Al terminar, `reduce()` devuelve el objeto con los usuarios indexados por su identificador.

    **¿Para qué sirve?** Esta estructura permite localizar rápidamente un usuario mediante su `id`, algo habitual cuando trabajamos con datos recibidos de un servidor.

---
# 3. Iterables

Los objetos iterables son una   generalización   de __arrays__. Es un concepto que permite que cualquier objeto pueda ser utilizado en un bucle __for..of.__

Por supuesto, las matrices o __arrays__ son iterables. Pero hay muchos otros objetos integrados que también lo son. Por ejemplo, las cadenas o __strings__ son iterables también. Como veremos, muchos operadores y métodos se basan en la   iterabilidad  .

Si  un  objeto  no  es  técnicamente  una  matriz,  pero  representa una  colección (lista, conjunto) de algo, entonces el uso de la sintaxis __for__..of es una gran forma de recorrerlo. Veamos cómo funciona.

Por ejemplo: tenemos un objeto que no es un __array__, pero parece adecuado para __for__..of. Como un objeto range que representa un intervalo de números:

<img src="imagenes/UD24%20ARRAYS_79.jpg" width="250">

Para hacer que el objeto range sea iterable (y así permitir que __for__..of funcione) necesitamos agregarle un método llamado __Symbol.iterator__ (un símbolo incorporado especial usado solo para realizar esa función).

Cuando se inicia __for__..of, éste llama al método __Symbol.iterator__ una vez (o genera un error si no lo encuentra). El método debe devolver un iterador : un objeto con el método next().

En adelante, __for__..of trabaja solamente con ese objeto devuelto.

Cuando __for__..of quiere el siguiente valor, llama a next() en ese objeto.

El resultado de next() debe tener la forma {done: Boolean, __value__: any}, donde done=__true__ significa que el bucle ha finalizado; de lo contrario, el nuevo valor es __value__.

---

Aquí está la implementación completa de range:
<img src="imagenes/UD24%20ARRAYS_80.jpg" width="300">



Note una característica fundamental de los iterables: separación de conceptos.

* El __range__ en sí mismo no tiene el método next().
* En cambio, la llamada a range[__Symbol.iterator__]() crea un otro objeto llamado “iterador”, y su next() genera valores para la iteración.
* Por lo tanto, el objeto iterador está separado del objeto sobre el que itera. Técnicamente, podríamos fusionarlos y usar el range mismo como iterador para simplificar el código. 

---

De esta manera:

<img src="imagenes/UD24%20ARRAYS_81.jpg" width="300">

Ahora range[__Symbol.iterator__]() devuelve el objeto range en sí: tiene el método next() necesario y recuerda el progreso de iteración actual en __this.current__. ¿Más corto? Sí. Y a veces eso también está bien.

La desventaja es que ahora es imposible tener dos bucles __for__..of corriendo sobre el objeto simultáneamente: compartirán el estado de iteración, porque solo hay un iterador: el objeto en sí. Pero dos __for__-of paralelos es algo raro, incluso en escenarios asíncronos.

---

### String es iterable

Las matrices y cadenas son los iterables integrados más utilizados. En una cadena o __string__, el bucle __for__..of recorre sus caracteres:

<img src="imagenes/UD24%20ARRAYS_82.png" width="300">

¡Y trabaja correctamente con valores de pares sustitutos (codificación UTF-16)!

<img src="imagenes/UD24%20ARRAYS_83.png" width="300">

### _Llamar a un iterador explícitamente_

Para una comprensión más profunda, veamos cómo usar un iterador explícitamente. Vamos a iterar sobre una cadena exactamente de la misma manera que __for__..of, pero con llamadas directas. Este código crea un iterador de cadena y obtiene valores de él “manualmente”:

<img src="imagenes/UD24%20ARRAYS_84.jpg" width="300">


Rara vez se necesita esto, pero nos da más control sobre el proceso que __for__..of. Por ejemplo, podemos dividir el proceso de iteración: iterar un poco, luego parar, hacer otra cosa y luego continuar.

---

### _Iterables y simil-array (array-like)_

Los dos son términos oficiales que se parecen, pero son muy diferentes. Asegúrese de comprenderlos bien para evitar confusiones.

Iterables son objetos que implementan el método __Symbol.iterator__, como se describió anteriormente.

simil-__array__ son objetos que tienen índices y longitud o __length__, por lo que se “ven” como __arrays__.

Cuando usamos JavaScript para tareas prácticas en el navegador u otros entornos, podemos encontrar objetos que son iterables o __array__-like, o ambos. Por ejemplo, las cadenas son iterables (__for__..of funciona en ellas) y __array__-like (tienen índices numéricos y __length__).

Pero un iterable puede que no sea __array__-like. Y viceversa, un __array__-like puede no ser iterable. Por ejemplo, range en el ejemplo anterior es iterable, pero no es __array__-like porque no tiene propiedades indexadas ni __length__.

Y aquí el objeto tiene forma de matriz, pero no es iterable:

<img src="imagenes/UD24%20ARRAYS_85.jpg" width="300">

Tanto los iterables como los __array__-like generalmente no son __arrays__, no tienen “__push__”, “__pop__”, etc. Eso es bastante inconveniente si tenemos un objeto de este tipo y queremos trabajar con él como con una matriz. __P.ej__. nos gustaría trabajar con range utilizando métodos de matriz.

Existe un método universal __Array.from__ que toma un valor iterable o simil-__array__ y crea un __Array__

¨real¨ a partir de él. De esta manera podemos llamar y usar métodos que pertenecen a una matriz. Por ejemplo:

<img src="imagenes/UD24%20ARRAYS_86.png" width="300">

---


__Array.from__ en la línea (*) toma el objeto, y si es iterable o simil-__array__ crea un nuevo __array__ y copia allí todos los elementos. Lo mismo sucede para un iterable:

<img src="imagenes/UD24%20ARRAYS_87.jpg" width="300">

La sintaxis completa para __Array.from__ también nos permite proporcionar una función opcional de “mapeo”:

<img src="imagenes/UD24%20ARRAYS_88.png" width="300">

El segundo argumento opcional __mapFn__ puede ser una función que se aplicará a cada elemento antes de agregarlo a la matriz, y __thisArg__ permite establecer el __this__ para ello. Por ejemplo:

<img src="imagenes/UD24%20ARRAYS_89.png" width="300">

Aquí usamos __Array.from__ para convertir una cadena en una matriz de caracteres:

<img src="imagenes/UD24%20ARRAYS_90.png" width="300">

---


A diferencia de __str.split__, __Array.from__ se basa en la naturaleza iterable de la cadena y, por lo tanto, al igual que __for__..of, funciona correctamente con pares sustitutos. Técnicamente aquí hace lo mismo que:

<img src="imagenes/UD24%20ARRAYS_91.jpg" width="300">

… Pero es más corto. Incluso podemos construir un segmento o __slice__ compatible con sustitutos en él:

<img src="imagenes/UD24%20ARRAYS_92.jpg" width="300">


---

## RESUMEN

Los objetos que se pueden usar en __for__..of se denominan iterables.

Técnicamente  , los iterables deben implementar el método llamado __Symbol.iterator__.

El resultado de __obj__[__Symbol.iterator__]() se llama iterador. Maneja el proceso de iteración adicional.

Un iterador debe tener el método llamado next() que devuelve un objeto {done: Boolean, __value__: any}, donde done: __true__ marca el fin de la iteración; de lo contrario, __value__ es el siguiente valor.

El método __Symbol.iterator__ se llama automáticamente por __for__..of, pero también podemos llamarlo directamente.

Los iterables integrados, como cadenas o matrices, también implementan __Symbol.iterator__.

El iterador de cadena es capaz de manejar los pares sustitutos.

Los objetos que tienen propiedades indexadas y longitud o __length__ se llaman __array__-like. Dichos objetos también pueden tener otras propiedades y métodos, pero carecen de los métodos integrados de las matrices.

S  i   miramos dentro de la especificación, veremos que la mayoría de los métodos incorporados suponen   que funcionan con iterables o __array__-likes en lugar de matrices “reales”, porque eso es más abstracto.

__Array.from__   (__obj__[, __mapFn__, __thisArg__]) crea un verdadero __Array__ de un __obj__ iterable o __array__-like, y luego podemos usar métodos de matriz en él. Los argumentos opcionales __mapFn__ y __thisArg__ nos permiten aplicar una función a cada elemento.

---

## Asignación desestructurante

Las dos estructuras de datos más usadas en JavaScript son Object y __Array__.
Los objetos nos permiten crear una simple entidad que almacena __items__ con una clave cada uno.
Los __arrays__ nos permiten reunir __items__ en una lista ordenada.
Pero cuando los pasamos a una función, tal vez no necesitemos un objeto o __array__ como un conjunto sino en piezas individuales.
La asignación desestructurante es una sintaxis especial que nos permite “desempaquetar” __arrays__ u objetos en varias variables, porque a veces es más conveniente.
La desestructuración también funciona bien con funciones complejas que tienen muchos argumentos, valores por defecto, etcétera.

### _Desestructuración de Arrays_

Un ejemplo de cómo el __array__ es desestructurado en variables:

<img src="imagenes/UD24%20ARRAYS_93.png" width="250">

Ahora podemos trabajar con variables en lugar de miembros de __array__. Se ve genial cuando se combina con __split__ u otro método que devuelva un __array__:

<img src="imagenes/UD24%20ARRAYS_94.png" width="300">



Como puedes ver, la sintaxis es simple. Aunque hay varios detalles peculiares. Veamos más ejemplos para entenderlo mejor.

En general, si el __array__ es mayor que la lista de la izquierda, los ítems extras son omitidos. Por ejemplo, aquí solo dos __items__ son tomados, el resto simplemente es ignorado:

<img src="imagenes/UD24%20ARRAYS_95.jpg" width="300">

---


si queremos también obtener todo lo que sigue, podemos agregarle un parámetro que obtiene “el resto” usando puntos suspensivos “…”`:

<img src="imagenes/UD24%20ARRAYS_96.jpg" width="300">

El valor de rest es un __array__ con los elementos restantes del __array__ original. Podemos usar cualquier otro nombre de variable en lugar de rest, sólo hay que asegurar que tenga tres puntos que lo antecedan y que esté último en la asignación desestructurante.

<img src="imagenes/UD24%20ARRAYS_97.jpg" width="300">

## Valores predeterminados

Si el __array__ es más corto que la lista de variables a la izquierda, no habrá errores. Los valores ausentes son considerados __undefined__:

<img src="imagenes/UD24%20ARRAYS_98.png" width="300">

Si  queremos  un  valor  “predeterminado”  para  reemplazar  el  valor  faltante,  podemos proporcionarlo utilizando =:

<img src="imagenes/UD24%20ARRAYS_99.jpg" width="300">

Los  valores  predeterminados  pueden  ser  expresiones  más  complejas  e  incluso  llamadas  a función, que serán evaluadas sólo si el valor no ha sido proporcionado. Por ejemplo, aquí utilizamos la función prompt para dos valores predeterminados.

<img src="imagenes/UD24%20ARRAYS_100.jpg" width="300">

Observa que el prompt se ejecuta solamente para el valor faltante (surname).


---

## _Desestructuración de objetos_

La asignación desestructurante también funciona con objetos. La sintaxis básica es:

<img src="imagenes/UD24%20ARRAYS_101.png" width="300">

Debemos tener un símil-objeto en el lado derecho, el que queremos separar en variables. El lado izquierdo contiene un símil-objeto “pattern” para sus propiedades correspondientes. En el caso más simple, es la lista de nombres de variables en {...}. Por ejemplo:

<img src="imagenes/UD24%20ARRAYS_102.png" width="300">


Las propiedades __options.title__, __options.width__ y __options.height__ son asignadas a las variables correspondientes. No importa el orden sino los nombres. Esto también funciona:

<img src="imagenes/UD24%20ARRAYS_103.jpg" width="400">

---

El patrón de la izquierda puede ser más complejo y especificar el mapeo entre propiedades y variables. Si queremos asignar una propiedad a una variable con otro nombre, por ejemplo que __options.width__ vaya en la variable llamada w, lo podemos establecer usando dos puntos:

<img src="imagenes/UD24%20ARRAYS_104.png" width="300">

Los dos puntos muestran “qué : va dónde”. En el ejemplo de arriba la propiedad width va a w, height va a h, y title es asignado al mismo nombre. Para propiedades potencialmente faltantes podemos establecer valores predeterminados utilizando "=", de esta manera:

<img src="imagenes/UD24%20ARRAYS_105.png" width="300">

---

### _Desestructuración anidada_

Si un objeto o __array__ contiene objetos y __arrays__ anidados, podemos utilizar patrones del lado izquierdo más complejos para extraer porciones más profundas.

En el código de abajo options tiene otro objeto en la propiedad size y un __array__ en la propiedad __items__. El patrón en el lado izquierdo de la asignación tiene la misma estructura para extraer valores de ellos:

<img src="imagenes/UD24%20ARRAYS_106.jpg" width="300">

Todas las propiedades del objeto options con excepción de extra que no está en el lado izquierda, son asignadas a las variables correspondientes:

<img src="imagenes/UD24%20ARRAYS_107.jpg" width="300">

Por último tenemos width, height, item1, item2 y title desde el valor predeterminado. Tenga en cuenta que no hay variables para size e __items__, ya que tomamos su contenido en su lugar.

---

## _Argumentos de función inteligentes_

Hay momentos en que una función tiene muchos argumentos, la mayoría de los cuales son opcionales. Eso es especialmente cierto para las interfaces de usuario. Imagine una función que crea un menú. Puede tener ancho, altura, título, elementos de lista, etcétera. Aquí hay una forma errónea de escribir tal función:

<img src="imagenes/UD24%20ARRAYS_108.jpg" width="300">

En la vida real, el problema es cómo recordar el orden de los argumentos. Normalmente los IDEs (Entorno de desarrollo integrado) intentan ayudarnos, especialmente si el código está bien documentado, pero aún así… Otro problema es cómo llamar a una función si queremos que use sus valores predeterminados en la mayoría de los argumentos. ¿Así?

<img src="imagenes/UD24%20ARRAYS_109.jpg" width="300">

Esto no es nada grato. Y se torna ilegible cuando tratamos con muchos argumentos.

¡La desestructuración llega al rescate! Podemos pasar los argumentos como un objeto, y la función inmediatamente los desestructura en variables:

<img src="imagenes/UD24%20ARRAYS_110.jpg" width="300">

También podemos usar desestructuración más compleja con objetos anidados y mapeo de dos puntos:

<img src="imagenes/UD24%20ARRAYS_111.jpg" width="300">

---

La sintaxis completa es la misma que para una asignación desestructurante:

<img src="imagenes/UD24%20ARRAYS_112.jpg" width="300">

Entonces, para un objeto de parámetros, habrá una variable varName para la propiedad incomingProperty, con defaultValue por defecto. Por favor observe que tal desestructuración supone que showMenu() tiene un argumento. Si queremos todos los valores predeterminados, debemos especificar un objeto vacío:

<img src="imagenes/UD24%20ARRAYS_113.jpg" width="300">

Podemos solucionar esto, poniendo {} como valor predeterminado para todo el objeto de argumentos:

<img src="imagenes/UD24%20ARRAYS_114.jpg" width="300">

En el código de arriba, todo el objeto de argumentos es {} por defecto, por lo tanto siempre hay algo para desestructurar.

---

## RESUMEN

La asignación desestructurante permite mapear instantáneamente un objeto o __array__ en varias    variables.

* La sintaxis completa para objeto:

<img src="imagenes/UD24%20ARRAYS_115.png" width="300">

Esto significa que la propiedad prop se asigna a la variable varName; pero si no existe tal    propiedad, se usa el valor default. Las propiedades de objeto que no fueron mapeadas son copiadas al objeto rest.  	

* La sintaxis completa para __array__:

<img src="imagenes/UD24%20ARRAYS_116.png" width="300">

El primer __item__ va a item1, el segundo a item2, todos los ítems restantes crean el __array__ resto.

Es posible extraer información desde __arrays__/objetos anidados, para esto el lado izquierdo debe    tener la misma estructura que el lado derecho.

---

## TAREAS

### 21. Asignación desestructurante

Tenemos     un     objeto:

```js
 let user = {
  name: "John",
  years: 30
};
```

Escriba     la     asignación     desestructurante     que     asigne     las     propiedades:

__name__     en     la     variable     name  .   years     en     la     variable     age  .
__isAdmin__     en     la   variable   isAdmin     (__false__,     si     no     existe     tal   propiedad)

Este     es     un     ejemplo     de     los     valores     después     de     su     asignación:

```js
 let user  = { name: "John", years: 30 };

// tu código al lado izquierdo:
// ... = __user__

alert( name ); // John
alert( age ); // 30

alert( isAdmin ); // false
```

---

### 22. El Salario máximo



Hay     un     objeto     salaries  :

```js
 let salaries = {
  "John": 100,
  "Pete": 300,
  "Mary": 250
};
```

Crear la     función     topSalary(salaries)     que   devuelva     el nombre     de     la     persona   mejor     pagada.

* Si     salaries     es     vacío,     debe     devolver     __null__  .

* Si     hay     varias     personas     con     la     mejor     paga,     devolver     cualquiera     de     ellas.

PD:     Utilice     __Object.entries__     y     desestructuración   para iterar     sobre     pares     de   claves/valores.
