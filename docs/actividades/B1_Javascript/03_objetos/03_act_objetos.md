Ejercicios de Objetos en JavaScript 

Ejercicio 1. Verificación y actualización de propiedades con in

Crea un objeto product con las propiedades:
let product = {
name: "Portßtil",
price: 1000,
stock: 5
};

1. Comprueba con el operador in si existen las propiedades "price" y "discount".
2. Si "discount" no existe, a±ade la propiedad con valor 0.1 (10%).
3. Recorre con for..in todas las propiedades y muÚstralas en consola.

Ejercicio 2. Duplicar valores numÚricos dinßmicamente

Escribe la funci¾n doubleNumbers(obj) que reciba un objeto y duplique ·nicamente sus
propiedades numÚricas.

Prueba con este objeto:
let game = {
title: "Zelda",
year: 1998,
score: 9.5,
genre: "Adventure"
};

Ejercicio 3. Contador de propiedades

Crea la funci¾n countProperties(obj) que:
1. Devuelva cußntas propiedades tiene un objeto.
2. Liste todas sus claves usando for..in.

Prueba con:
let user = {
name: "Laura",
age: 22,
city: "Madrid"
};

Ejercicio 4. Sistema de inventario

1. Crea un objeto inventory con varias propiedades, donde cada clave es un producto y el valor es
la cantidad en stock.
2. Recorre el objeto con for..in para mostrar el stock disponible de cada producto.
3. A±ade la funci¾n updateStock(item, quantity) que actualice el stock:
- Si el producto existe, sume la cantidad.
- Si no existe, cree la propiedad con ese valor.

Prueba con:
updateStock("mouse", -2);
updateStock("monitor", 4);


