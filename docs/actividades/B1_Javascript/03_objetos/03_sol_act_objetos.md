# SOLUCIÓN ACTIVIDAD 1: Objetos
## Enunciados y soluciones

Material de apoyo para el módulo de Desarrollo Web en Entorno Cliente — 2.º DAW.

---

# Ejercicio 1. Comprobar y añadir propiedades

## Enunciado
Crea un objeto `product` con estas propiedades:
- `name`: `"Portátil"`
- `price`: `1000`
- `stock`: `5`

Realiza las siguientes operaciones:
1. Comprueba si existe la propiedad `price` utilizando el operador `in`.
2. Comprueba si existe la propiedad `discount`.
3. Si `discount` no existe, añádela con el valor `0.1`.
4. Recorre todas las propiedades del objeto con `for...in` y muestra por consola el nombre y el valor de cada una.

## Solución
```javascript
let product = {
    name: "Portátil",
    price: 1000,
    stock: 5
};

console.log("¿Existe price?", "price" in product);
console.log("¿Existe discount?", "discount" in product);

if (!("discount" in product)) {
    product.discount = 0.1;
}

for (let property in product) {
    console.log(`${property}: ${product[property]}`);
}
```

---

# Ejercicio 2. Duplicar los valores numéricos

## Enunciado
Crea una función `doubleNumbers(obj)` que reciba un objeto y multiplique por dos únicamente los valores de sus propiedades que sean numéricos. La función debe devolver el objeto modificado.

Prueba la función con este objeto:
```javascript
let game = {
    title: "Zelda",
    year: 1998,
    score: 9.5,
    genre: "Adventure"
};
```

## Solución
```javascript
function doubleNumbers(obj) {
    for (let property in obj) {
        if (typeof obj[property] === "number") {
            obj[property] *= 2;
        }
    }

    return obj;
}

let game = {
    title: "Zelda",
    year: 1998,
    score: 9.5,
    genre: "Adventure"
};

console.log(doubleNumbers(game));
```

### Resultado esperado
```javascript
{
    title: "Zelda",
    year: 3996,
    score: 19,
    genre: "Adventure"
}
```

---

# Ejercicio 3. Contar las propiedades de un objeto

## Enunciado
Crea una función `countProperties(obj)` que:
1. Recorra las propiedades propias enumerables del objeto mediante `for...in`.
2. Muestre por consola el nombre de cada propiedad.
3. Devuelva el número total de propiedades.

Prueba la función con este objeto:
```javascript
let user = {
    name: "Laura",
    age: 22,
    city: "Madrid"
};
```

## Solución
```javascript
function countProperties(obj) {
    let count = 0;

    for (let property in obj) {
        if (Object.hasOwn(obj, property)) {
            console.log(property);
            count++;
        }
    }

    return count;
}

let user = {
    name: "Laura",
    age: 22,
    city: "Madrid"
};

console.log("Número de propiedades:", countProperties(user));
```

### Resultado esperado
```text
name
age
city
Número de propiedades: 3
```

---

# Ejercicio 4. Gestionar el inventario

## Enunciado
Crea un objeto `inventory` que almacene el número de unidades disponibles de varios productos. Incluye inicialmente:
- `keyboard`: 10
- `mouse`: 8
- `laptop`: 4

Después:
1. Recorre el inventario con `for...in` y muestra cada producto y su cantidad.
2. Crea una función `updateStock(item, quantity)` que actualice el inventario:
   - Si el producto ya existe, suma `quantity` a su stock.
   - Si no existe, crea una propiedad con ese nombre y le asigna `quantity`.
3. Prueba la función con `updateStock("mouse", -2)` y `updateStock("monitor", 4)`.
4. Muestra el inventario actualizado.

## Solución
```javascript
let inventory = {
    keyboard: 10,
    mouse: 8,
    laptop: 4
};

for (let item in inventory) {
    console.log(`${item}: ${inventory[item]} unidades`);
}

function updateStock(item, quantity) {
    if (item in inventory) {
        inventory[item] += quantity;
    } else {
        inventory[item] = quantity;
    }
}

updateStock("mouse", -2);
updateStock("monitor", 4);

console.log("Inventario actualizado:", inventory);
```

### Resultado esperado
```text
keyboard: 10 unidades
mouse: 8 unidades
laptop: 4 unidades
Inventario actualizado: {
    keyboard: 10,
    mouse: 6,
    laptop: 4,
    monitor: 4
}
```

---

## Conceptos trabajados
- Creación y modificación de objetos.
- Acceso a propiedades mediante `obj.propiedad` y `obj["propiedad"]`.
- Operador `in`.
- Bucle `for...in`.
- Operador `typeof`.
- Comprobación de propiedades propias con `Object.hasOwn()`.
- Funciones que reciben y modifican objetos.
