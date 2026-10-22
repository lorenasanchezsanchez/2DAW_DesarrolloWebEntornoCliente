<span style="color:#595959"> _Desarrollo Web en Entorno Cliente_ </span>

<span style="color:#262626">Introducción: callbacks</span>

<span style="color:#404040">loadScript\(src\)\,</span>

![](imagenes/ud26_0.png)

<span style="color:#000000">Esto inserta en el documento una etiqueta nueva\, creada dinámicamente\, \<script src =" \.\.\. "> </span>

<span style="color:#000000">con el código src dado\. El navegador comienza a cargarlo automáticamente y lo ejecuta cuando </span>

<span style="color:#000000">la carga se completa\. Podemos usar esta función así: </span>

![](imagenes/ud26_1.png)

<span style="color:#000000">El script se ejecuta “asincrónicamente”\, ya que </span>

<span style="color:#000000">comienza a cargarse ahora\, pero se ejecuta más </span>

<span style="color:#000000">tarde\, cuando la función ya ha finalizado\. El código debajo de loadScript \(\.\.\.\)\, no espera que </span>

<span style="color:#000000">finalice la carga del script\. </span>

![](imagenes/ud26_2.png)

<span style="color:#000000">Digamos que necesitamos usar el nuevo script tan pronto como se cargue\. Este script declara </span>

<span style="color:#000000">nuevas funciones\, y las queremos ejecutar\. Si lo hacemos inmediatamente después de llamar a </span>

<span style="color:#000000">loadScript \(\.\.\.\)\, no funcionarán: </span>

![](imagenes/ud26_3.png)

<span style="color:#000000">Es natural\, porque el navegador no tuvo tiempo de cargar el script\. Hasta el momento\, la </span>

<span style="color:#000000">función loadScript no proporciona una forma de monitorear la finalización de la carga\. El script </span>

<span style="color:#000000">se carga y finalmente se ejecuta\, eso es todo\. Pero necesitamos saber cuándo sucede\, para </span>

<span style="color:#000000">poder usar las funciones y variables nuevas de dicho script\. </span>

<span style="color:#000000">Agreguemos a loadScript un segundo argumento: una función callback que se ejecuta cuando </span>

<span style="color:#000000">se completa la carga el script: </span>

![](imagenes/ud26_4.png)

<span style="color:#000000">básicamente ejecuta una función después de que el script fue cargado y ejecutado\. </span>

<span style="color:#000000">Ahora\, si queremos llamar las nuevas funciones desde el script\, lo hacemos dentro de la callback: </span>

![](imagenes/ud26_5.png)

<span style="color:#000000">Esa es la idea: el segundo argumento es una función \(generalmente anónima\) que se ejecuta </span>

<span style="color:#000000">cuando se completa la acción\. Aquí un ejemplo ejecutable con un script real: </span>

![](imagenes/ud26_6.png)

<span style="color:#000000">Eso se llama programación asincrónica “basado en callback”\. Una función que hace algo de </span>

<span style="color:#000000">forma asincrónica debería aceptar un argumento de callback donde ponemos la función por </span>

<span style="color:#000000">ejecutar después de que se complete\. Aquí lo hicimos en loadScript\, pero por supuesto es un </span>

<span style="color:#000000">enfoque general\. </span>

<span style="color:#000000"> _Callback en una callback _ </span>

<span style="color:#000000">¿Cómo podemos cargar dos scripts secuencialmente\, el segundo en cuanto haya terminado de </span>

<span style="color:#000000">cargarse el primero? La solución natural sería poner la segunda llamada loadScript dentro de la </span>

![](imagenes/ud26_7.png)

<span style="color:#000000">queremos un script más …?</span>

![](imagenes/ud26_8.png)

<span style="color:#000000">acciones\, pero no en todos los casos; así que pronto veremos otras variantes\. </span>

<span style="color:#000000"> _Manejo de errores _ </span>

<span style="color:#000000">En los ejemplos anteriores no consideramos los errores\. ¿Qué pasa si falla la carga del script? </span>

<span style="color:#000000">Nuestra callback debería poder reaccionar ante eso\. Aquí una versión mejorada de loadScript </span>

<span style="color:#000000">que monitorea los errores de carga: </span>

![](imagenes/ud26_9.png)

<span style="color:#000000">Para una carga exitosa llama a callback\(null\, script\) y de lo contrario a callback\(error\)\. El uso: </span>

![](imagenes/ud26_10.png)

<span style="color:#000000">conoce como “error first callback” \(callback con el error primero\)\.</span>

<span style="color:#000000"> La convención es: </span>

<span style="color:#000000">El primer argumento de la ‘callback’ está reservado para un error\, si este ocurre\. En tal </span>

<span style="color:#000000">caso se llama a callback\(err\)\. </span>

<span style="color:#000000">El segundo argumento \(y los siguientes si es necesario\) son para el resultado exitoso\. En </span>

<span style="color:#000000">este caso se llama a callback\(null\, result1\, result2 \.\.\.\)\. </span>

<span style="color:#000000">informar errores </span>

<span style="color:#000000"> _Pirámide infernal _ </span>

<span style="color:#000000">A primera vista\, es una forma viable de codificación asincrónica\. Y de hecho lo es\. Para una o </span>

<span style="color:#000000">quizás dos llamadas anidadas\, se ve bien\. Pero para múltiples acciones asincrónicas que van una </span>

<span style="color:#000000">tras otra\, tendremos un código como este: </span>

![](imagenes/ud26_11.png)

<span style="color:#000000">En el código de arriba: </span>

<span style="color:#000000">Cargamos 1\.js\, entonces si no hay error…</span>

<span style="color:#000000">Cargamos 2\.js\, entonc</span>

<span style="color:#000000">es si no hay error…</span>

<span style="color:#000000">Cargamos 3\.js\, entonces\, si no hay ningún error: haga otra cosa \(\*\)\. </span>

<span style="color:#000000">administrar\, especialmente si tenemos un código real en lugar de ‘…’ que puede i</span>

<span style="color:#000000">bucles\, declaraciones condicionales\, etc\. A esto se le llama “infierno de callbacks” o “pirámide </span>

<span style="color:#000000">infernal” \(“callback hell”\, “pyramid of doom”\)\.</span>

![](imagenes/ud26_12.png)

<span style="color:#000000">La “pirámide” de llamadas anidadas crece hacia la derecha con cada acción asincrónica\. Pronto </span>

<span style="color:#000000">se sale de control\. </span>

<span style="color:#000000">Entonces esta forma de codificación no es tan buena\. Podemos tratar de aliviar el problema </span>

<span style="color:#000000">haciendo\, para cada acción\, una función independiente: </span>

![](imagenes/ud26_13.png)

<span style="color:#000000">¿Lo Ves? Hace lo mismo\, y ahora no hay anidamiento profundo porque convertimos cada acción </span>

<span style="color:#000000">en una función de nivel superior separada\. </span>

<span style="color:#000000">notado que hay que saltar de un lado a otro mientras lees\. Es un inconveniente\, especialmente </span>

<span style="color:#000000">si el lector no está familiarizado con el código y no sabe dónde dirigir la mirada\. Además\, las </span>

<span style="color:#000000">funciones llamadas step\* son de un solo uso\, existen únicamente para evitar la “Pirámide de </span>

<span style="color:#000000">abarrotados aquí\. </span>

![](imagenes/ud26_14.png)

<span style="color:#000000">Más adelante veremos cómo los “fanáticos” pueden suscribirse a estos cambios\.</span>

<span style="color:#000000">Aquí hay un ejemplo de un constructor de promesas y una función ejecutora simple con “código </span>

<span style="color:#000000">productor” que toma tiempo \(a través </span>

<span style="color:#000000">de setTimeout\): </span>

![](imagenes/ud26_15.png)

<span style="color:#000000">Podemos ver dos cosas al ejecutar el código anterior: </span>

<span style="color:#000000">Se llama al ejecutor de forma automática e inmediata \(por new Promise\)\. </span>

<span style="color:#000000">El ejecutor recibe dos argumentos: resolve y reject\. Estas funciones están predefinidas </span>

<span style="color:#000000">por el motor de JavaScript\, por lo que no necesitamos crearlas\. Solo debemos llamar a </span>

<span style="color:#000000">una de ellas cuando esté listo\. </span>

<span style="color:#000000">Después de un segundo de “procesamiento”\, el ejecutor llama a resolve\("hecho"\) para </span>

<span style="color:#000000">producir el resultado\. Esto cambia el estado del objeto promise: </span>

![](imagenes/ud26_16.png)

<span style="color:#000000">ejemplo de finalización exitosa de la tarea\, una “promesa cumplida”\. Y ahora un </span>

<span style="color:#000000">ejemplo del ejecutor rechazando la promesa con un error: </span>

![](imagenes/ud26_17.png)

<span style="color:#000000">La llamada a reject\(\.\.\.\) mueve el objeto promise al estado "rechazado": </span>

![](imagenes/ud26_18.png)

<span style="color:#000000">Para resumir\, el ejecutor debe realizar una tarea \(generalmente algo que toma tiempo\) y luego </span>

<span style="color:#000000">llamar a “resolve” o a “reject” para cambiar el estado del objeto promise correspondiente\.</span>

<span style="color:#000000">consideramos “establecida”\.</span>

<span style="color:#000000"> _Consumidores: then y catch _ </span>

<span style="color:#000000">Un objeto Promise sirve como enlace entre el ejecutor \(el “código productor” o el “cantante”\) y </span>

<span style="color:#000000">funciones de consumo pueden registrarse \(suscribirse\) utilizando los métodos </span>

<span style="color:#000000">El más importante y fundamental es “\.then”\. La sintaxis es:</span>

![](imagenes/ud26_19.png)

<span style="color:#000000">El primer argumento de “\.then” es una función que se ejecuta cuando se resuelve la promesa y </span>

<span style="color:#000000">recibe el resultado\. </span>

<span style="color:#000000">El segundo argumento d</span>

<span style="color:#000000">e “\.then” es una función que se ejecuta cuando se rechaza la promesa </span>

<span style="color:#000000">y recibe el error\. </span>

<span style="color:#000000">Por ejemplo\, aquí hay una reacción a una promesa resuelta con éxito: </span>

![](imagenes/ud26_20.png)

<span style="color:#000000">La primera función fue ejecutada\. Y en el caso de un rechazo\, el segundo: </span>

![](imagenes/ud26_21.png)

<span style="color:#000000">argumento de función para </span>

![](imagenes/ud26_22.png)

<span style="color:#000000">\.then\(null\, errorHandlingFunction\)</span>

<span style="color:#000000">\. O podemos usar </span>

<span style="color:#000000">\.catch\(errorHandlingFunction\)</span>

<span style="color:#000000">exactamente lo mismo: </span>

![](imagenes/ud26_23.png)

<span style="color:#000000"> __LIMPIEZA: FINALLY __ </span>

<span style="color:#000000">promesas\. La llamada </span>

<span style="color:#000000"> en el sentido de que f siempre se </span>

<span style="color:#000000">ejecuta cuando se resuelve la promesa: ya sea que se resuelva o rechace\. </span>

<span style="color:#000000">La idea de finally es establecer un manejador para realizar la limpieza y finalización después de </span>

<span style="color:#000000">que las operaciones se hubieran completado\. Por ejemplo\, detener indicadores de carga\, cerrar </span>

<span style="color:#000000">conexiones que ya no son necesarias\, etc\. </span>

<span style="color:#000000">Puedes pensarlo como el finalizador de la fiesta\. No importa si la fiesta fue buena o mala ni </span>

<span style="color:#000000">cuántos invitados hubo\, aún necesitamos \(o al menos deberíamos\) hacer la limpieza después\. El </span>

<span style="color:#000000">código puede verse como esto: </span>

![](imagenes/ud26_24.png)

<span style="color:#000000">Sin embargo\, note que finally\(f\) no es exactamente un alias dethen\(f\, f\)\`\. </span>

<span style="color:#000000">Hay diferencias importantes:  </span>

<span style="color:#000000">exitosa o no\. Eso está bien\, ya que usualmente nuestra tarea es realizar procedimientos </span>

<span style="color:#000000">de finalización “generales”\.</span>

<span style="color:#000000">argumentos\, y lo que sale de la promesa es manejado en el siguiente manejador\. </span>

<span style="color:#000000">Resultados y errores pasan “a través” del manejador de finally\. Estos pasan al siguiente </span>

<span style="color:#000000">manejador que se adecúe\. Por ejemplo\, aquí el resultado se pasa a través de finally al </span>

<span style="color:#000000">then que le sigue: </span>

![](imagenes/ud26_25.png)

<span style="color:#000000">Como puedes ver\, el “valor” devuelto por la primera promesa es pasado a través de </span>

<span style="color:#000000">finally al siguiente then\. </span>

<span style="color:#000000">Esto es muy conveniente\, porque finally no está destinado a procesar el resultado de </span>

<span style="color:#000000">una promesa\. Como dijimos antes\, es el lugar para hacer la limpieza general sin importar </span>

<span style="color:#000000">cuál haya sido el resultado\. Y aquí\, el ejemplo de un error\. Vemos cómo se pasa a través </span>

<span style="color:#000000">de finally a catch: </span>

![](imagenes/ud26_26.png)

<span style="color:#000000">ignorado silenciosamente\. </span>

<span style="color:#000000">La única excepción a esta regla se da cuando el manejador mismo de finally dispara un </span>

<span style="color:#000000">error\. En ese caso\, este error pasa al siguiente manejador de error en lugar del resultado </span>

<span style="color:#000000">previo al finally\. Para summarizar: </span>

<span style="color:#000000">Un manejador finally no obtiene lo que resultó del manejador previo \(no tiene </span>

<span style="color:#000000">argumentos\)\. Ese resultado es pasado a través de él al siguiente manejador\. </span>

<span style="color:#000000">Si el manejador de finally devuelve algo\, será ignorado\. </span>

<span style="color:#000000">Cuando es finally el que dispara el error\, la ejecución pasa al manejador de error </span>

<span style="color:#000000">Estas características son de ayuda y hacen que las cosas funcionen tal como corresponde si </span>

<span style="color:#000000">“finalizamos” con finally como se supone: con procedimientos d</span>

<span style="color:#000000">e limpieza genéricos\. </span>

<span style="color:#000000"> _Ejemplo: loadScript _ </span>

<span style="color:#000000">continuación\, veamos </span>

<span style="color:#000000">escribir código asincrónico\. Tomemos\, del capítulo anterior\, la función loadScript para cargar un </span>

<span style="color:#000000">script\. Esta es la variante basada callback\, solo para recordarnos: </span>

![](imagenes/ud26_27.png)

<span style="color:#000000">Reescribámoslo usando Promesas\. </span>

<span style="color:#000000">La nueva función loadScript no requerirá una callback\. En su lugar\, creará y devolverá un objeto </span>

<span style="color:#000000">manejadores \(funciones de suscripción\) usando \.then: </span>

![](imagenes/ud26_28.png)

![](imagenes/ud26_29.png)

<span style="color:#000000">Podemos ver inmediatamente algunos beneficios sobre el patrón basado en callback: </span>

![](imagenes/ud26_30.png)

<span style="color:#262626">Encadenamiento de Promesa</span>

<span style="color:#000000">encadenamiento de promesas\. Se ve así: </span>

![](imagenes/ud26_31.png)

<span style="color:#000000">La idea es que el resultado pase a través de la cadena de manejadores “\.then”\.</span>

<span style="color:#000000">Aquí el flujo es: </span>

<span style="color:#000000">La promesa inicial se resuelve en 1 segundo \(\*\)\, </span>

<span style="color:#000000">\(resuelta con el valor 2\)\. </span>

<span style="color:#000000">El siguiente \.then \(\*\*\*\) obtiene el resultado del anterior\, lo procesa \(duplica\) y lo pasa </span>

<span style="color:#000000">al siguiente manejador\. </span>

<span style="color:#000000">…y así sucesivamente\.</span>

<span style="color:#000000">A medida que el resultado se pasa a lo largo de la cadena de controladores\, podemos ver una </span>

<span style="color:#000000">secuencia de llamadas de alerta: 1 → 2 → 4\.</span>

![](imagenes/ud26_32.png)

<span style="color:#000000">Todo funciona\, porque cada llamada a promise\.then devuelve una nueva promesa\, para que </span>

<span style="color:#000000">siguiente “\.then” </span>

<span style="color:#000000">convierte en el resultado de esa promesa\, por lo que se llama al siguiente “\.then”\.</span>

<span style="color:#000000">Un error clásico de principiante: técnicamente también podemos agregar muchos ‘\.then’ a una </span>

<span style="color:#000000">sola promesa: eso no es encadenamiento\. Por ejemplo: </span>

![](imagenes/ud26_33.png)

<span style="color:#000000">Lo que hicimos aquí fue añadir varios controladores a una sola promesa\. No se pasan el resultado </span>

<span style="color:#000000">el uno al otro; en su lugar\, lo procesan de forma independiente\. Aquí está la imagen \(compárala </span>

<span style="color:#000000">con el encadenamiento anterior\): </span>

![](imagenes/ud26_34.png)

<span style="color:#000000">promesa\. Entonces\, en el código sobre todo alert muestra lo mismo: 1\. En la práctica\, rara vez </span>

<span style="color:#000000">necesitamos múltiples manejadores para una promesa\. El encadenamiento se usa mucho más a </span>

<span style="color:#000000"> _Devolviendo promesas _ </span>

<span style="color:#000000">Un controlador \(“handler”\)\, utilizado en “\.then\(handler\)”\, puede crear y devolver una promesa\. </span>

<span style="color:#000000">En ese caso\, otros manejadores esperan hasta que se estabilice \(resuelva o rechace\) y luego </span>

<span style="color:#000000">obtienen su resultado\. Por ejemplo: </span>

![](imagenes/ud26_35.png)

<span style="color:#000000">En este código e</span>

<span style="color:#000000">l primer “\.then” muestra 1 y devuelve new Promise\(\.\.\.\) en la línea \(\*\)\. Después </span>

<span style="color:#000000">de un segundo\, se resuelve\, y el resultado \(el argumento de resolve\, aquí es result \* 2\) se pasa </span>

<span style="color:#000000">al controlador del segundo “\.then”\. Ese controlador está en la línea \(\*\*\)\, mues</span>

<span style="color:#000000">tra 2 y hace lo </span>

<span style="color:#000000">Por lo tanto\, la salida es la misma que en el ejemplo anterior: 1 → 2 → 4\, pero ahora con 1 </span>

<span style="color:#000000">segundo de retraso entre las llamadas de alerta\. Devolver las promesas nos permite construir </span>

<span style="color:#000000">cadenas de acciones asincrónicas\. </span>

<span style="color:#000000"> _El ejemplo: loadScript _ </span>

<span style="color:#000000">Usemos esta función con el loadScript promisificado\, definido en el capítulo anterior\, para cargar </span>

<span style="color:#000000">los scripts uno por uno\, en secuencia: </span>

![](imagenes/ud26_36.png)

<span style="color:#000000">Este código se puede acortar un poco con las funciones de flecha: </span>

![](imagenes/ud26_37.png)

<span style="color:#000000">Aquí cada llamada a loadScript devuelve una promesa\, y el sig</span>

<span style="color:#000000">uiente “\.then” se ejecuta cuando </span>

<span style="color:#000000">se resuelve\. Luego inicia la carga del siguiente script\. Entonces los scripts se cargan uno tras otro\. </span>

<span style="color:#000000">Podemos agregar más acciones asincrónicas a la cadena\. Tenga en cuenta que el código sigue </span>

<span style="color:#000000">siendo “plano”: crece hacia abajo\, no a la derecha\. No hay signos de la “pirámide del destino”\. </span>

<span style="color:#000000">Técnicamente\, podríamos agregar “\.then” directamente a cada loadScript\, así:</span>

![](imagenes/ud26_38.png)

<span style="color:#000000">Este código hace lo mismo: carga 3 scripts en secuencia\. Pero “crece hacia la derecha”\. Entonces </span>

<span style="color:#000000">tenemos el mismo problema que con los callbacks\. Quienes comienzan a usar promesas pueden </span>

<span style="color:#000000">desconocer el encadenamiento\, y por ello escribirlo de esta manera\. En general\, se prefiere el </span>

<span style="color:#000000">encadenamiento\. </span>

<span style="color:#000000">A veces es aceptable escribir “\.then” directamente\, porque la funció</span>

<span style="color:#000000">n anidada tiene acceso al </span>

<span style="color:#000000">variables script1\, script2\, script3\. Pero eso es una excepción más que una regla\. </span>

<span style="color:#000000"> _Ejemplo más grande: fetch _ </span>

<span style="color:#000000">En la programación “frontend”\, l</span>

<span style="color:#000000">as promesas a menudo se usan para solicitudes de red\. Veamos </span>

<span style="color:#000000">un ejemplo extendido de esto\. </span>

<span style="color:#000000">remoto\. Tiene muchos parámetros opcionales cubiertos en capítulos separados\, pero la sintaxis </span>

<span style="color:#000000">básica es bastante simple: </span>

![](imagenes/ud26_39.png)

<span style="color:#000000">Esto hace una solicitud de red a la url y devuelve una promesa\. La promesa se resuelve con un </span>

<span style="color:#000000">objeto ‘response’ cuando el servidor remoto responde con encabezados\, pero antes de que se </span>

<span style="color:#000000">descargue la respuesta completa\.  </span>

<span style="color:#000000">response\.text\(\): </span>

<span style="color:#000000">promesa que se resuelve cuando se descarga el texto completo del servidor remoto\, con ese </span>

<span style="color:#000000">texto como resultado\. El siguiente código hace una solicitud a user\.json y carga su texto desde </span>

![](imagenes/ud26_40.png)

<span style="color:#000000">El objeto response devuelto por fetch también incluye el método response\.json\(\) que lee los </span>

<span style="color:#000000">datos remotos y los analiza como JSON\. En nuestro caso\, eso es aún más conveniente\, así que </span>

<span style="color:#000000">pasemos a ello\. También usaremos las funciones de flecha por brevedad: </span>

![](imagenes/ud26_41.png)

<span style="color:#000000">Ahora hagamos algo con el usuario cargado\. Por ejemplo\, podemos hacer una solicitud más a </span>

<span style="color:#000000">GitHub\, cargar el perfil de usuario y mostrar el avatar: </span>

![](imagenes/ud26_42.png)

<span style="color:#000000">El código funciona; ver comentarios sobre los detalles\. Sin embargo\, hay un problema potencial\, </span>

<span style="color:#000000">un error típico para aquellos que comienzan a usar promesas\. </span>

<span style="color:#000000">mostrarse y se elimine? Por ejemplo\, nos gustaría mostrar un formulario para editar ese usuario </span>

<span style="color:#000000">u otra cosa\. A partir de ahora\, no hay manera\. </span>

<span style="color:#000000">Para que la cadena sea extensible\, debemos devolver una promesa que se resuelva cuando el </span>

<span style="color:#000000">avatar termine de mostrarse\. Como esto: </span>

![](imagenes/ud26_43.png)

<span style="color:#000000">Es decir\, el controlador “\.then” en la línea \(\*\) ahor</span>

<span style="color:#000000">a devuelve new Promise\, que se resuelve solo </span>

<span style="color:#000000">resolve\(githubUser\) </span>

<span style="color:#000000">cadena esperará eso\. </span>

<span style="color:#000000">Como buena práctica\, una acción asincrónica siempre debe devolver una promesa\. Eso hace </span>

<span style="color:#000000">posible planificar acciones posteriores; incluso si no planeamos extender la cadena ahora\, es </span>

<span style="color:#000000">posible que la necesitemos más adelante\. Finalmente\, podemos dividir el código en funciones </span>

![](imagenes/ud26_44.png)

<span style="color:#404040">Si un controlador “\.</span>

<span style="color:#404040">finally\, no importa\) devuelve una </span>

<span style="color:#404040">promesa\, el resto de la cadena espera hasta que ésta quede establecida </span>

<span style="color:#404040">\(sea resuelta o rechazada\)\. Cuando lo hace\, su resultado \(o error\) pasa </span>

<span style="color:#404040">más allá\. Aquí hay una imagen completa:</span>

![](imagenes/ud26_45.jpg)

<span style="color:#262626">Manejo de errores con promesas</span>

<span style="color:#000000">Las promesas encadenadas son excelentes manejando los errores\. Cuando una promesa es </span>

<span style="color:#000000">rechazada\, el control salta al manejador de rechazos más cercano\. Esto es muy conveniente en </span>

<span style="color:#000000">Por ejemplo\, en el código de abajo\, la URL a la cual se le hace fetch es incorrecta \(no existe el </span>

<span style="color:#000000">sitio\) y al ser rechazada “\.catch” maneja el error:</span>

![](imagenes/ud26_46.png)

<span style="color:#000000">Como puedes ver\, el </span>

<span style="color:#000000"> no tiene que escribirse inmediatamente después de la promesa\. </span>

<span style="color:#000000">Este puede aparecer después de uno o quizás varios </span>

<span style="color:#000000">O\, puede ocurrir\, que todo en el sitio se encuentre bien\, pero la respuesta no es un JSON válido\. </span>

<span style="color:#000000">La forma más fácil de detectar todos los errores es agregando </span>

<span style="color:#000000"> al final de la cadena de </span>

![](imagenes/ud26_47.png)

<span style="color:#000000"> _try…catch implícito_ </span>

<span style="color:#000000">"try\.\.catch invisible"\. Si ocurre una excepción\, esta es atrapada y es tratada como un rechazo\. </span>

<span style="color:#000000">Por ejemplo\, este código: </span>

![](imagenes/ud26_48.png)

<span style="color:#000000">…Hace exactamente lo mismo que este:</span>

![](imagenes/ud26_49.png)

<span style="color:#000000">El "try\.\.catch invisible" embebido en el ejecutor detecta automáticamente el error y lo convierte </span>

<span style="color:#000000">en una promesa rechazada\. </span>

<span style="color:#000000">Esto sucede no solo en la función ejecutora\, sino también en sus manejadores\. Si hacemos throw </span>

<span style="color:#000000">dentro de una llamada a “\.then”\, esto devolverá una prom</span>

<span style="color:#000000">esa rechazada\, por lo que el control </span>

<span style="color:#000000">salta al manejador de errores más cercano\. Por ejemplo: </span>

![](imagenes/ud26_50.png)

<span style="color:#000000">Esto sucede con todos los errores\, no solo los causados por la sentencia de excepción throw\. Por </span>

<span style="color:#000000">ejemplo\, un error de programación: </span>

![](imagenes/ud26_51.png)

<span style="color:#000000"> del final no solo detecta rechazos explícitos\, sino también los errores accidentales en </span>

<span style="color:#000000">los manejadores anteriores\. </span>

<span style="color:#000000"> _Rethrowing \(relanzamiento de errores\) _ </span>

<span style="color:#000000">Como ya vimos\, el “\.catch” del final es similar a “try\.\.catch”\. Podemos tener tantos manejadores </span>

<span style="color:#000000">“\.then” como queram</span>

<span style="color:#000000">os\, y luego usar un solo \.catch al final para manejar los errores en todos </span>

<span style="color:#000000">ellos\. En un “try\.\.catch” normal\, podemos analizar el error y quizá volver a lanzarlo si no se puede </span>

<span style="color:#000000">manejar\. Lo mismo podemos hacer con las promesas\. </span>

<span style="color:#000000">Si hacemos throw dentro de “\.catch”\, el control pasa a otro manejador de errores más cercano\. </span>

<span style="color:#000000">Y\, si manejamos el error y terminamos de forma correcta\, entonces se continúa con el siguiente </span>

<span style="color:#000000">manejador “\.then” exitoso\. En el ejemplo de abajo\, el “\.catch” maneja el error de forma exitosa:</span>

![](imagenes/ud26_52.png)

<span style="color:#000000">Aquí el “\.catch” termina de forma correcta\. Entonces se ejecuta el siguiente manejador exitoso </span>

<span style="color:#000000">En el siguiente ejemplo podemos ver otra situación con “\.catch”\. El manejador \(\*\) detecta el </span>

<span style="color:#000000">error y simplemente no puede manejarlo \(en el ejemplo solo sabe qué hacer con un URIError\)\, </span>

<span style="color:#000000">por lo que lo lanza nuevamente: </span>

![](imagenes/ud26_53.png)

<span style="color:#000000">La ejecución salta del primer </span>

<span style="color:#000000"> \(\*\) al siguiente \(\*\*\) en la cadena\. </span>

<span style="color:#000000"> _Rechazos no manejados _ </span>

<span style="color:#000000">¿Qué sucede cuanto un error no es manejado? Por ejemplo\, si olvidamos agregar </span>

<span style="color:#000000">final de una cadena de promesas\, como aquí: </span>

![](imagenes/ud26_54.png)

<span style="color:#000000">En caso de que se genere un error\, la promesa se rechaza y la ejecución salta al manejador de </span>

<span style="color:#000000">rechazos más cercano\. Pero aquí no hay ninguno\. Entonces el error se “atasca”\, ya que no hay </span>

<span style="color:#000000">código para manejarlo\. En la práctica\, al igual que con los errores comunes no manejados en el </span>

<span style="color:#000000">código\, esto significa que algo ha salido terriblemente mal\. </span>

<span style="color:#000000">¿Qué sucede cuando ocurre un error regular y no es detectado por try\.\.catch? El script muere </span>

<span style="color:#000000">con un mensaje en la consola\. Algo similar sucede con los rechazos de promesas no manejadas\. </span>

<span style="color:#000000">En este caso\, el motor de JavaScript rastrea el rechazo y lo envía al ámbito global\. Puedes ver en </span>

<span style="color:#000000">consola el error generado si ejecutas el ejemplo anterior\. En el navegador podemos detectar </span>

<span style="color:#000000">tales errores usando el evento unhandledrejection: </span>

![](imagenes/ud26_55.png)

<span style="color:#000000">Si se produce un error\, y no hay un “\.catch”\, se dispara unhandledrejection\, y se obtiene el </span>

<span style="color:#000000">objeto event el cual contiene información sobre el error\, por lo que podemos hacer algo con el </span>

<span style="color:#000000">error \(manejar el error\)\. </span>

<span style="color:#000000">Usualmente estos errores no son recuperables\, por lo que la mejor salida es informar al usuario </span>

<span style="color:#000000">sobre el problema y probablemente reportar el incidente al servidor\. En entornos fuera del </span>

<span style="color:#000000">navegador como Node\.js existen otras formas de rastrear errores no manejados\. </span>

<span style="color:#404040">unhandledrejection</span>

<span style="color:#404040">Hay 6 métodos estáticos en la clase Promise\. Veremos sus casos de uso </span>

<span style="color:#000000">Digamos que queremos que muchas promesas se ejecuten en paralelo y esperar hasta que </span>

<span style="color:#000000">todas ellas estén listas\. </span>

<span style="color:#000000">Por ejemplo\, descargar varias URLs en paralelo y procesar su contenido en cuanto todas ellas </span>

<span style="color:#000000">finalicen\. Para ello es Promise\.all\. La sintaxis es: </span>

![](imagenes/ud26_56.png)

<span style="color:#000000">Promise\.all toma un iterable \(usualmente un array de promesas\) y devuelve una nueva </span>

<span style="color:#000000">Esta nueva promesa es resuelta en cuanto todas las promesas listadas se resuelven\, y el array </span>

<span style="color:#000000">de aquellos resultados se vuelve su resultado\. Por ejemplo\, el Promise\.all debajo se resuelve </span>

<span style="color:#000000">después de 3 segundos\, y su resultado es un array \[1\, 2\, 3\]: </span>

![](imagenes/ud26_57.png)

<span style="color:#000000">Ten en cuenta que el orden de los miembros del array es el mismo que el de las promesas que </span>

<span style="color:#000000">los originan\. Aunque la primera promesa es la que toma más tiempo en resolverse\, es aún la </span>

<span style="color:#000000">primera en el array de resultados\. </span>

<span style="color:#000000">podemos usar fetch en todos ellos así: </span>

![](imagenes/ud26_58.png)

<span style="color:#000000">Un mayor ejemplo con fetch: la búsqueda de información de usuario para un array de usuarios </span>

<span style="color:#000000">de GitHub por sus nombres \(o podríamos buscar un array de bienes por sus “id”\, la lógica es </span>

![](imagenes/ud26_59.png)

<span style="color:#000000">inmediatamente rechaza: “reject” con ese error\. Por ejemplo:</span>

![](imagenes/ud26_60.png)

<span style="color:#000000">Aquí la segunda promesa se rechaza en dos segundos\. Esto lleva a un rechazo inmediato de </span>

<span style="color:#000000">Promise\.all\, entonces </span>

<span style="color:#000000"> se ejecuta: el error del rechazo se vuelve la salida del Promise\.all </span>

<span style="color:#000000"> _2\. Promise\.allSettled _ </span>

<span style="color:#000000">Promise\.all rechaza como un todo si cualquiera de sus promesas es rechazada\. Esto es bueno </span>

<span style="color:#000000">para los casos de “todo o nada”\, cuando necesitamos que todos los resultados sean </span>

![](imagenes/ud26_61.png)

<span style="color:#000000">Promise\.allSettled solo espera que todas las promesas se resuelvan sin importar sus resultados\. </span>

<span style="color:#000000">El array resultante tiene: </span>

<span style="color:#000000">\{status:"fulfilled"\, value:result\} para respuestas exitosas\, </span>

<span style="color:#000000">\{status:"rejected"\, reason:error\} para errores\. </span>

<span style="color:#000000">Por ejemplo\, quisiéramos hacer “fetch” de la información de múltiples usuarios\. Incluso si uno </span>

<span style="color:#000000">falla\, aún estaremos interesados en los otros\. Usemos Promise\.allSettled: </span>

![](imagenes/ud26_62.png)

<span style="color:#000000">El results de la línea \(\*\) de arriba será: </span>

![](imagenes/ud26_63.png)

<span style="color:#000000">Entonces para cada promesa obtendremos su estado y value/error\. </span>

<span style="color:#000000">Si el browser no soporta Promise\.allSettled\, es fácil implementarlo: </span>

<span style="color:#000000">if \(\!Promise\.allSettled\) \{ </span>

<span style="color:#000000">  const rejectHandler = reason => \(\{ status: 'rejected'\, reason \}\); </span>

<span style="color:#000000">  const resolveHandler = value => \(\{ status: 'fulfilled'\, value \}\); </span>

<span style="color:#000000">  Promise\.allSettled = function \(promises\) \{ </span>

<span style="color:#000000">convertedPromises </span>

<span style="color:#000000">Promise\.resolve\(p\)\.then\(resolveHandler\, </span>

<span style="color:#000000">rejectHandler\)\); </span>

<span style="color:#000000">    return Promise\.all\(convertedPromises\); </span>

<span style="color:#000000">En este código\, promises\.map toma los valores de entrada\, los transforma en promesas \(por si </span>

<span style="color:#000000">no lo eran\) con p => Promise\.resolve\(p\)\, entonces agrega un manejador “\.then” a cada una\.</span>

<span style="color:#000000">Este manejador \(“handler”\) transforma un resultado exitoso value en \{status:'fulfilled'\, value\}\, y </span>

<span style="color:#000000">\{status:'rejected'\, </span>

<span style="color:#000000">Promise\.allSettled\. Ahora podemos usar Promise\.allSettled para obtener el resultado de todas </span>

<span style="color:#000000">las promesas dadas incluso si algunas son rechazadas\. </span>

<span style="color:#000000"> _4\. Promise\.race _ </span>

<span style="color:#000000">Similar a Promise\.all\, pero espera solamente por la primera respuesta y obtiene su resultado \(o </span>

<span style="color:#000000">error\)\. Su sintaxis es: </span>

![](imagenes/ud26_64.png)

<span style="color:#000000">Por ejemplo\, aquí el resultado será 1: </span>

![](imagenes/ud26_65.png)

<span style="color:#000000">La primera promesa fue la más rápida\, por lo que se vuelve resultado\. En cuanto una promesa </span>

<span style="color:#000000">responde\, “gana la carrera”</span>

<span style="color:#000000">\, y todos los resultados o errores posteriores son ignorados\. </span>

<span style="color:#000000">Es similar a Promise\.race\, pero espera solamente por la primera promesa cumplida y obtiene su </span>

<span style="color:#000000">rechazada con AggregateError\, un error especial que almacena los errores de todas las promesas </span>

<span style="color:#000000">en su propiedad errors\. La sintaxis es: </span>

![](imagenes/ud26_66.png)

<span style="color:#000000">Por ejemplo\, aquí el resultado será 1: </span>

![](imagenes/ud26_67.png)

<span style="color:#000000">La primera promesa fue la más rápida\, pero fue rechazada entonces devuelve el resultado de la </span>

<span style="color:#000000">promesa cumplida “gana </span>

<span style="color:#000000">serán ignorados\. Aquí hay un ejemplo donde todas las promesas fallan: </span>

![](imagenes/ud26_68.png)

<span style="color:#000000">propiedad errors del objeto AggregateError\. </span>

<span style="color:#000000"> _6\. Promise\.resolve/reject _ </span>

<span style="color:#000000">Los métodos Promise\.resolve y Promise\.reject son raramente necesitados en código moderno </span>

<span style="color:#000000">porque la sintaxis async/await \(que veremos luego\) las hace algo obsoletas\. </span>

<span style="color:#000000">Las tratamos aquí para completar la cobertura y por aquellos casos que por algún motivo no </span>

<span style="color:#000000">puedan usar async/await\. </span>

<span style="color:#000000"> _Promise\.resolve _ </span>

<span style="color:#000000">Promise\.resolve\(value\) crea una promesa resuelta con el resultado value\. Tal como: </span>

![](imagenes/ud26_69.png)

<span style="color:#000000">compatibilidad\, </span>

<span style="color:#000000">Por ejemplo\, la función loadCached abajo busca una URL y recuerda \(en caché\) su contenido\. </span>

<span style="color:#000000">Futuros llamados con la misma URL devolverá el contenido de caché\, pero usa Promise\.resolve </span>

<span style="color:#000000">para hacer una promesa de él y así el valor devuelto es siempre una promesa: </span>

![](imagenes/ud26_70.png)

<span style="color:#000000">loadCached\(url\)\.then\(…\) </span>

<span style="color:#000000">Promise\.resolve en la línea \(\*\)\. </span>

<span style="color:#000000">Promise\.reject\(error\) crea una promesa rechazada con error\. Tal como: </span>

![](imagenes/ud26_71.png)

<span style="color:#000000">En la práctica este método casi nunca es usado\. </span>

<span style="color:#404040">Existen 6 métodos estáticos de la clase Promise:</span>

<span style="color:#404040">Promise\.all\(promises\) </span>

<span style="color:#404040">espera que todas las promesas se resuelvan y devuelve un </span>

<span style="color:#404040">array de sus resultados\. Si cualquiera es rechazada se vuelve el error de Promise\.all</span>

<span style="color:#404040">los demás resultados son ignorados\.</span>

<span style="color:#404040">Promise\.allSettled\(promises\) \(método recientemente añadido\) </span>

<span style="color:#404040">espera que toda las </span>

<span style="color:#404040">promesas respondan y devuelve sus resultados como un array de objetos con:</span>

<span style="color:#404040">status: "fulfilled" o "rejected"</span>

<span style="color:#404040">fulfilled\) o reason \(si</span>

<span style="color:#404040">Promise\.race\(promises\) </span>

<span style="color:#404040">espera a la primera promesa que responda y aquel </span>

<span style="color:#404040">resultado o error se vuelve su resultado o error\.</span>

<span style="color:#404040">Promise\.any\(promises\) \(método recientemente añadido\) </span>

<span style="color:#404040">espera por la primera </span>

<span style="color:#404040">promesa que se cumpla y devuelve su resultado\. Si todas las promesas son </span>

<span style="color:#404040">rechazadas\, AggregateError</span>

<span style="color:#404040">se vuelve el error de Promise\.any\.</span>

<span style="color:#404040">Promise\.resolve\(value\) </span>

<span style="color:#404040">crea una promesa resuelta con el “</span>

<span style="color:#404040">Promise\.reject\(error\) </span>

<span style="color:#404040">crea una promesa rechazada con el “error” dado</span>

<span style="color:#404040">es probablemente el más común en la práctica\.</span>

<span style="color:#000000">“Promisificación” es una simple transformación\. Es la conversión de una funci</span>

<span style="color:#000000">ón que acepta un </span>

<span style="color:#000000">callback a una función que devuelve una promesa\. </span>

<span style="color:#000000">A menudo estas transformaciones son necesarias en la vida real ya que muchas funciones y </span>

<span style="color:#000000">librerías están basadas en callbacks\, pero las promesas son más convenientes así que tiene </span>

<span style="color:#000000">sentido promisificarlas\. Veamos un ejemplo\. Aquí tenemos loadScript\(src\, callback\) del artículo </span>

<span style="color:#000000">Introducción: callbacks\. </span>

![](imagenes/ud26_72.png)

<span style="color:#000000">La función carga un script con el src dado\, y llama a callback\(err\) en caso de error o callback\(null\, </span>

<span style="color:#000000">script\) en caso de carga exitosa\. Esto está ampliamente acordado en el uso de callbacks\, lo </span>

<span style="color:#000000">hemos visto antes\. Vamos a promisificarla\. </span>

<span style="color:#000000">Haremos una función nueva loadScriptPromise\(src\) que va a hacer lo mismo \(carga el script\)\, </span>

<span style="color:#000000">exitosa y rechaza con error en caso contrario\. Aquí está: </span>

![](imagenes/ud26_73.png)

<span style="color:#000000">Como podemos ver\, la nueva función es un “wrapper” \(una función contenedora\) que envuelv</span>

<span style="color:#000000">la función loadScript original\. La llama proveyendo su propio callback y la traduce a una promesa </span>

<span style="color:#000000">resolve/reject\. </span>

<span style="color:#000000">Ahora loadScriptPromise se adapta bien a un código basado en promesas\. Si nos gustan más las </span>

<span style="color:#000000">promesas que los callbacks \(y pronto veremos más motivos para ello\)\, la usaremos en su lugar\. </span>

<span style="color:#000000">En la práctica podemos necesitar promisificar más de una función\, así que tiene sentido usar un </span>

<span style="color:#000000">función contenedora \(wrapper\)\. </span>

![](imagenes/ud26_74.png)

<span style="color:#000000">El código puede verse complicado\, pero es esencialmente lo mismo que escribimos arriba al </span>

<span style="color:#000000">promisificar la función loadScript\. </span>

<span style="color:#000000">contenedor devuelve una promesa y redirige el llamado a la f original\, siguiendo el resultado en </span>

<span style="color:#000000">el callback personalizado \(\*\*\)\. Aquí promisify asume que la función original espera un callback </span>

<span style="color:#000000">con dos argumentos \(err\, result\)\. Eso es lo que usualmente encontramos\. Entonces nuestro </span>

<span style="color:#000000">callback personalizado está exactamente en el formato correcto\, y promisify funciona muy bien </span>

<span style="color:#000000">¿Y si la f original espera un callback con más argumentos callback\(err\, res1\, res2\)? Podemos </span>

<span style="color:#000000">mejorar el ayudante\. Hagamos una versión de promisify más avanzada\. </span>

<span style="color:#000000">Cuando la llamamos como promisify\(f\)\, debe funcionar igual que en la versión previa\. </span>

<span style="color:#000000">Cuando la llamamos como promisify\(f\, true\)\, debe devolver una promesa que resuelve </span>

<span style="color:#000000">con el array de resultados del callback\. Esto es para callbacks con muchos argumentos\. </span>

![](imagenes/ud26_75.png)

<span style="color:#000000">Como puedes ver es esencialmente lo mismo de antes\, pero resolve es llamado con solo uno o </span>

<span style="color:#000000">con todos los argumentos dependiendo del valor de manyArgs\. Para formatos más exóticos de </span>

<span style="color:#000000">callback\(result\)\, </span>

<span style="color:#000000">promisificarlos </span>

<span style="color:#000000">manualmente sin usar el ayudante\. </span>

<span style="color:#000000">Existe una sintaxis especial para trabajar con promesas de una forma más confortable\, llamada </span>

<span style="color:#000000">“async/await”\. Es sorprendentemente fácil de entender y usar\.</span>

<span style="color:#000000"> _Funciones async _ </span>

<span style="color:#000000">Comencemos con la palabra clave async\. Puede ser ubicada delante de una función como aquí: </span>

![](imagenes/ud26_76.png)

<span style="color:#000000">automáticamente\. Por ejemplo\, esta función devuelve una promesa resuelta con el resultado </span>

<span style="color:#000000">de 1; Probémosla: </span>

![](imagenes/ud26_77.png)

<span style="color:#000000">…Podríamos explícitamente devolver una promesa\, lo cual sería lo mismo:</span>

![](imagenes/ud26_78.png)

<span style="color:#000000">Entonces\, async se asegura de que la función devuelva una promesa\, o envuelve las no promesas </span>

<span style="color:#000000">y las transforma en una\. Bastante simple\, ¿correcto? Pero no solo eso\. Hay otra palabra\, await\, </span>

<span style="color:#000000">que solo trabaja dentro de funciones async y es muy interesante\. </span>

![](imagenes/ud26_79.png)

<span style="color:#000000">await hace que JavaScript espere hasta que la promesa responda y devuelve su resultado\. Aquí </span>

<span style="color:#000000">hay un ejemplo con una promesa que resuelve en 1 segundo: </span>

![](imagenes/ud26_80.png)

<span style="color:#000000">La ejecución de la función es pausada en la línea \(\*\) y se reanuda cuando la promesa responde\, </span>

<span style="color:#000000"> literalmente suspende la ejecución de la función hasta que se establezca la </span>

<span style="color:#000000">promesa\, y luego la reanuda con el resultado de la promesa\. Eso no cuesta ningún recurso de </span>

<span style="color:#000000">CPU\, porque el motor de JavaScript puede hacer otros trabajos mientras tanto: ejecutar otros </span>

<span style="color:#000000">scripts\, manejar eventos\, etc\. Es simplemente una sintaxis más elegante para tener el resultado </span>

<span style="color:#000000">de una promesa que “promise\.then”\, es más fácil de leer y de escribir\.</span>

<span style="color:#000000"> __Nota: “await” solo funciona den__ </span>

<span style="color:#000000"> __tro de una función async\. __ </span>

<span style="color:#000000">Tomemos el ejemplo showAvatar\(\) del capítulo Encadenamiento de promesas y rescribámoslo </span>

<span style="color:#000000">usando async/await: </span>

<span style="color:#000000">Necesitaremos reemplazar los llamados “\.then” con await\.</span>

<span style="color:#000000">También debemos hacer que la función sea async para que aquellos funcionen\. </span>

![](imagenes/ud26_81.png)

<span style="color:#000000">Bien limpio y fácil de leer\, ¿no es cierto? Mucho mejor que antes\. </span>

<span style="color:#000000">Métodos de clase Async: Para declarar un método de clase async\, simplemente se le antepone </span>

![](imagenes/ud26_82.png)

<span style="color:#000000"> _Manejo de Error _ </span>

<span style="color:#000000">Si una promesa se resuelve normalmente\, entonces await promise devuelve el resultado\. Pero </span>

<span style="color:#000000">en caso de rechazo\, dispara un error\, tal como si hubiera una instrucción throw en aquella línea\. </span>

![](imagenes/ud26_83.png)

<span style="color:#000000">…es lo mismo que esto:</span>

![](imagenes/ud26_84.png)

<span style="color:#000000">En situaciones reales\, la promesa tomará algún tiempo antes del rechazo\. En tal caso habrá un </span>

<span style="color:#000000">retardo antes de que await dispare un error\. Podemos atrapar tal error usando try\.\.catch\, de la </span>

<span style="color:#000000">misma manera que con un throw normal: </span>

![](imagenes/ud26_85.png)

<span style="color:#000000">En el caso de un error\, el control salta al bloque catch\. Podemos también envolver múltiples </span>

![](imagenes/ud26_86.png)

<span style="color:#000000">Si no tenemos try\.\.catch\, entonces la promesa generada por el llamado de la función async f\(\) </span>

<span style="color:#000000">se vuelve rechazada\. Podemos añadir </span>

<span style="color:#000000"> para manejarlo: </span>

![](imagenes/ud26_87.png)

<span style="color:#000000">Si olvidamos añadir </span>

<span style="color:#000000"> allí\, obtendremos un error de promesa no manejado \(visible en </span>

<span style="color:#000000">unhandledrejection\. </span>

<span style="color:#404040">El comando async</span>

<span style="color:#404040">antes de una función tiene dos efectos:</span>

<span style="color:#404040">Hace que siempre devuelva una promesa\.</span>

<span style="color:#404040">Permite que sea usado await</span>

<span style="color:#404040">El comando await</span>

<span style="color:#404040">antes de una promesa hace que JavaScript espere hasta </span>

<span style="color:#404040">que la promesa responda\. Entonces:</span>

<span style="color:#404040">Si es un error\, la excepción es generada </span>

<span style="color:#404040">lo mismo que si throw</span>

<span style="color:#404040">error fuera llamado </span>

<span style="color:#404040">en ese mismo lugar\.</span>

<span style="color:#404040">De otro modo\, devuelve el resultado\.</span>

<span style="color:#404040">Juntos proveen un excelente marco para escribir código asincrónico que es </span>

<span style="color:#404040">fácil de leer y escribir\.</span>

<span style="color:#404040">raramente necesitamos escribir promise\.then/catch\, pero </span>

<span style="color:#404040">aún no deberíamos olvidar que están basados en promesas porque a veces </span>

<span style="color:#404040">\(ej\. como en el nivel superior de código\) tenemos que usar esos métodos\. </span>

<span style="color:#404040">También Promise\.all</span>

<span style="color:#404040">es adecuado cuando esperamos por varias tareas </span>

