INTRODUCCION A
ERRORES HALDING EN
JAVASCRIPT
1
2║ DAW - Desarrollo Web en Entorno Cliente

Manejo de errores, "try...catch"
2
? No importa lo buenos que seamos en la programaci¾n, a veces nuestros
scripts tienen errores. Pueden ocurrir debido a nuestros descuidos, una
entrada inesperada del usuario, una respuesta err¾nea del servidor y por
otras razones mßs.
? Por lo general, un script ômuereö (se detiene inmediatamente) en caso de
error, imprimiÚndolo en la consola. Pero hay una construcci¾n sintßctica
try...catch que nos permite ôatraparö errores para que el script pueda, en
lugar de morir, hacer algo mßs razonable.

La sintaxis ôtryàcatchö
3
La construcci¾n try...catch tiene dos bloques principales: try, y luego catch:
Funciona asÝ:
1. Primero, se ejecuta el c¾digo en try {...}.
2. Si no hubo errores, se ignora catch (err): la ejecuci¾n llega al final de try y contin·a,
omitiendo catch.
3. Si se produce un error, la ejecuci¾n de try se detiene y el control fluye al comienzo de
catch (err). La variable err (podemos usar cualquier nombre para ella) contendrß un
objeto de error con detalles sobre lo que sucedi¾.

Entonces, un error dentro del bloque try {...} no mata el script; tenemos la oportunidad de
4
manejarlo en catch. Veamos algunos ejemplos.
Un ejemplo sin errores: muestra alert (1) y (2):
Un ejemplo con un error: muestra (1) y (3):
Nota: Para que try..catch funcione, el c¾digo debe ser ejecutable. En otras palabras, deberÝa
ser JavaScript vßlido. No funcionarß si el c¾digo es sintßcticamente incorrecto, por ejemplo, si
hay llaves sin cerrar

Objeto Error
5
Cuando se produce un error, JavaScript genera un objeto que contiene los detalles al respecto.
El objeto se pasa como argumento para catch:
Para todos los errores integrados, el objeto error tiene dos propiedades principales:
ò Name: Nombre de error. Por ejemplo, para una variable indefinida que es
"ReferenceError".
ò Message: Mensaje de texto sobre detalles del error.
Hay otras propiedades no estßndar disponibles en la mayorÝa de los entornos. Uno de los mßs
utilizados y compatibles es:
ò Stack: Pila de llamadas actual: una cadena con informaci¾n sobre la secuencia de
llamadas anidadas que condujeron al error. Utilizado para fines de depuraci¾n.
Por ejemplo:
Si no necesitamos detalles del error, catch puede omitirlo:

Usando ôtryàcatchö
6
Exploremos un caso de uso de la vida real de try...catch. Como ya sabemos, JavaScript admite el
mÚtodo JSON.parse(str) para leer valores codificados con JSON.
Por lo general, se utiliza para decodificar datos recibidos a travÚs de la red, desde el servidor u
otra fuente. Lo recibimos y llamamos a JSON.parse asÝ:
Puede encontrar informaci¾n mßs detallada sobre JSON en el capÝtulo MÚtodos JSON, toJSON.
Si json estß mal formado, JSON.parse genera un error, por lo que el script ômuereö.
┐DeberÝamos estar satisfechos con eso? íPor supuesto no!
De esta manera, si algo anda mal con los datos, el visitante nunca lo sabrß (a menos que abra la
consola del desarrollador). Y a la gente realmente no le gusta cuando algo ôsimplemente muereö
sin ning·n mensaje de error. Usemos try...catch para manejar el error:
AquÝ usamos el bloque catch solo para mostrar el mensaje, pero podemos hacer mucho mßs:
enviar una nueva solicitud de red, sugerir una alternativa al visitante, enviar informaci¾n sobre
el error a una instalaci¾n de registro, à. Todo mucho mejor que solo morir.

Lanzando nuestros propios errores
7
┐QuÚ sucede si json es sintßcticamente correcto, pero no tiene una propiedad requerida de
name? Como este:
AquÝ JSON.parse se ejecuta normalmente, pero la ausencia de name es en realidad un error
nuestro. Para unificar el manejo de errores, usaremos el operador throw.

El operador ôthrowö
8
El operador throw genera un error. La sintaxis es:
TÚcnicamente, podemos usar cualquier cosa como un objeto error. Eso puede ser incluso un
primitivo, como un n·mero o una cadena, pero es mejor usar objetos, preferiblemente con
propiedades name y message (para mantenerse algo compatible con los errores incorporados).
JavaScript tiene muchos constructores integrados para manejar errores estßndar: Error,
SyntaxError, ReferenceError, TypeError y otros. Podemos usarlos para crear objetos de error
tambiÚn. Su sintaxis es:
Para errores incorporados (no para cualquier objeto, solo para errores), la propiedad name es
exactamente el nombre del constructor. Y mensaje se toma del argumento. Por ejemplo:

Veamos quÚ tipo de error genera JSON.parse:
9
Como podemos ver, ese es un SyntaxError. Y en nuestro caso, la ausencia de name es un error,
ya que los usuarios deben tener un name. AsÝ que vamos a lanzarlo:
En la lÝnea (*), el operador throw genera un SyntaxError con el message dado, de la misma
manera que JavaScript lo generarÝa Úl mismo. La ejecuci¾n de try se detiene inmediatamente y
el flujo de control salta a catch.
Ahora catch se convirti¾ en un lugar ·nico para todo el manejo de errores: tanto para JSON.parse
como para otros casos.

Relanzando (rethrowing)
10
En el ejemplo anterior usamos try...catch para manejar datos incorrectos. Pero, ┐es posible que
ocurra otro error inesperado dentro del bloque try{...}? Como un error de programaci¾n (la
variable no estß definida) o algo mßs, no solo ôdatos incorrectosö. Por ejemplo:
íPor supuesto, todo es posible! Los programadores cometen errores. Incluso en las utilidades de
c¾digo abierto utilizadas por millones durante dÚcadas, de repente se puede descubrir un error
que conduce a hacks terribles.
En nuestro caso, try...catch estß destinado a detectar errores de ôdatos incorrectosö. Pero por
su naturaleza, catch obtiene todos los errores de try. AquÝ recibe un error inesperado, pero a·n
muestra el mismo mensaje de ôError en JSONö. Eso estß mal y tambiÚn hace que el c¾digo sea
mßs difÝcil de depurar.
Para evitar tales problemas, podemos emplear la tÚcnica de ôrethrowingö. La regla es simple:
Catch solo debe procesar los errores que conoce y ôvolver a lanzarö (rethrow) a todos los demßs.
La tÚcnica de ôrethrowingö puede explicarse con mßs detalle:
ò Catch captura todos los errores.
ò En el bloque catch (err) {...} analizamos el objeto error err.
ò Si no sabemos c¾mo manejarlo, hacemos 'throw err`.

Por lo general, podemos verificar el tipo de error usando el operador instanceof:
11
TambiÚn podemos obtener el nombre de la clase error con la propiedad err.name. Todos los
errores nativos lo tienen. Otra opci¾n es leer err.constructor.name. En el siguiente c¾digo,
usamos el rethrowing para que catch solo maneje SyntaxError:
El error lanzado en la lÝnea (*) desde el interior del bloque catch cae desde try...catch y puede
ser atrapado por una construcci¾n externa try...catch (si existe), o mata al script.
Por lo tanto, el bloque catch en realidad maneja solo los errores con los que sabe c¾mo lidiar y
ôomiteö todos los demßs. El siguiente ejemplo demuestra c¾mo dichos errores pueden ser
detectados por un nivel mßs de try...catch:

tryàcatchàfinally
12
Espera, eso no es todo. La construcci¾n try...catch puede tener una clßusula de c¾digo mßs:
finally.
Si existe, se ejecuta en todos los casos:
ò despuÚs de try, si no hubo errores,
ò despuÚs de catch, si hubo errores.
La sintaxis extendida se ve asÝ:
Intenta ejecutar este c¾digo:

El c¾digo tiene dos formas de ejecuci¾n:
13
ò Si responde ôSÝö a ô┐Cometer un error?ö, Entonces try -> catch -> finally.
ò Si dice ôNoö, entonces try -> finally.
La clßusula finally a menudo se usa cuando comenzamos a hacer algo y queremos finalizarlo en
cualquier resultado. Por ejemplo, queremos medir el tiempo que tarda una funci¾n de n·meros
de Fibonacci fib(n). Naturalmente, podemos comenzar a medir antes de que se ejecute y
terminar despuÚs. ┐Pero quÚ pasa si hay un error durante la llamada a la funci¾n? En particular,
la implementaci¾n de fib(n) en el c¾digo siguiente devuelve un error para n·meros negativos o
no enteros.
La clßusula finally es un excelente lugar para terminar las mediciones, pase lo que pase. AquÝ
finally garantiza que el tiempo se medirß correctamente en ambas situaciones, en caso de una
ejecuci¾n exitosa de fib y en caso de error:
Puede verificar ejecutando el c¾digo e ingresando 35 en prompt; se ejecuta normalmente, finally
despuÚs de try. Y luego ingrese -1 û habrß un error inmediato, y la ejecuci¾n tomarß 0ms. Ambas
mediciones se realizan correctamente.

Captura global
14
Imaginemos que tenemos un error fatal fuera de try...catch, y el script muri¾. Como un error de
programaci¾n o alguna otra cosa terrible.
┐Hay alguna manera de reaccionar ante tales ocurrencias? Es posible que queramos registrar el
error, mostrarle algo al usuario (normalmente no ve mensajes de error), etc.
No hay ninguna en la especificaci¾n, pero los entornos generalmente lo proporcionan, porque
es realmente ·til. Por ejemplo, Node.js tiene process.on("uncaughtException") para eso. Y en el
| navegador  | podemos  | asignar  una  | funci¾n  | a  la  propiedad  | especial window.onerror,  | que  se  |
| ---------- | -------- | ------------- | -------- | ----------------- | ------------------------- | -------- |
ejecutarß en caso de un error no detectado. La sintaxis:

ò
Message: Mensaje de error.
| ò   | Url: URL del script donde ocurri¾ el error.                    |     |     |     |     |     |
| --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- |
| ò   | Line, col: N·meros de lÝnea y columna donde ocurri¾ el error.  |     |     |     |     |     |
| ò   | Error: El objeto error.                                        |     |     |     |     |     |

Por ejemplo:
15

El rol del controlador global window.onerror generalmente no es recuperar la ejecuci¾n del
script, probablemente sea imposible en caso de errores de programaci¾n, pero sÝ enviar el
mensaje de error a los desarrolladores.
| TambiÚn  | hay  servicios  | web  que  | proporcionan  | registro  | de  errores  para  | tales  casos,  | como  |
| -------- | --------------- | --------- | ------------- | --------- | ------------------ | -------------- | ----- |
https://errorception.com o https://www.muscula.com. Estos servicios funcionan asÝ:
| 1.  | Nos registramos en el servicio y obtenemos un fragmento de JS (o la URL de un script)  |     |     |     |     |     |     |
| --- | -------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
para insertar en las pßginas.
| 2.  | Ese script JS establece una funci¾n personalizada window.onerror.                      |     |     |     |     |     |     |
| --- | -------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| 3.  | Cuando se produce un error, se envÝa una solicitud de red al servicio.                 |     |     |     |     |     |     |
| 4.  | Podemos iniciar sesi¾n en la interfaz web del servicio y ver los errores registrados.  |     |     |     |     |     |     |

RESUMEN
16
? La construcci¾n try...catch permite manejar errores de tiempo de ejecuci¾n. Literalmente permite ôintentar (try)ö ejecutar
el c¾digo y ôatrapar (catch)ö errores que pueden ocurrir en Úl. La sintaxis es:
? Puede que no haya una secci¾n catch o finally, por lo que las construcciones mßs cortas try...catch y try...finallytambiÚn
son vßlidas.
? Los objetos Error tienen las siguientes propiedades:
? messageûel mensaje de error legible por humanos.
? nameûla cadena con el nombre del error (nombre del constructor de error).
? stack(No estßndar, pero bien soportado) ûla pila en el momento de la creaci¾n del error.
? Si no se necesita un objeto error, podemos omitirlo usando catch { en lugar de catch (err) {.
? TambiÚn podemos generar nuestros propios errores utilizando el operador throw. TÚcnicamente, el argumento de throw
puede ser cualquier cosa, pero generalmente es un objeto error heredado de la clase incorporada Error. Mßs sobre la
extensi¾n de errores en el pr¾ximo capÝtulo.
? Relanzado (rethrowing)es un patr¾n muy importante de manejo de errores: un bloque catch generalmente espera y sabe
c¾mo manejar el tipo de error en particular, por lo que deberÝa relanzar errores que no conoce.
? Incluso si no tenemos try...catch, la mayorÝa de los entornos nos permiten configurar un controlador de errores ôglobalö
para detectar los errores que caigan. En el navegador, eso es window.onerror.

TAREAS
17
Finally o solo el c¾digo?
Compara los dos fragmentos de c¾digo.
El primero usa finally para ejecutar el c¾digo despuÚs de try..catch:
El segundo fragmento coloca la limpieza justo despuÚs de try..catch:
Definitivamente necesitamos la limpieza despuÚs del trabajo, no importa si
hubo un error o no.
┐Hay alguna ventaja aquÝ en usar finally o ambos fragmentos de c¾digo son iguales?
Si existe tal ventaja, entonces da un ejemplo cuando sea importante.
