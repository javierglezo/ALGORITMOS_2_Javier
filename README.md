# JAVIER GONZÁLEZ ORTEGA
***Segundo examen parcial de algoritmia***
Este repositorio contiene cada uno de los ejercicios del examen:
## Ejercicio 1: Ejercicio POO

### Descripción
Este ejercicio consiste en elaborar un programa que devuelve los elementos propios de una canción.
Está compuesto por dos archivos:

### Archivos
- Archivos: `genre.py` y `song.py`

## Ejercicio 2: Ejercicio de Recursividad: Cálculo del Factorial

### Descripción detallada en formato de PSEUDOCÓDIGO
***Hipótesis:*** Este algoritmo permite calcular el factorial de un número utilizando el método de recursividad.

***Precondición:*** El número ingresado debe ser un entero positivo, en caso de que sea igual a 0, su factorial se define como 1.

***Entrada:*** Se ingresa el número del cual se desea calcular el factorial.

***Tratamiento de datos:*** Si el número es 0, se devuelve 1 y finalizará el programa.
Si el número es distinto de 0, calcula el factorial del número multiplicándolo por el factorial del número anterior de forma recursiva "(n-1)". Una vez llega a 0,(caso 1), termina la recursividad.

***Poscondición***: El resultado debe ser un número positivo ya que no multiplica por ningún número negativo.

***Salida:*** Se obtiene el valor del factorial del número ingresado.


### Archivo
- Archivo: `Factorial.py`

## Ejercicio 3: Ejercicio de Ordenación
- BUBBLE SORT:
    El método bubble sort es un tipo de función que a través de un algoritmo de iteración, es capaz de ordenar una lista de elementos de forma sencilla.  
    **¿Cómo funciona?:** Lo que hace este algoritmo es, uno a uno, comparar con el elemento adyacente según el parámetro que le pases (normalmente al querer ordenar una lista en orden ascendente, compararía con el elemento de la derecha y en caso de ser menor **itera** con él).
    Pongamos un *ejemplo*: Dada una lista "[34, 7, 23, 32, 5]" el método actuaría de la siguiente forma:
        En el ***primer bucle***, compara el primer elemento con su adyacente 34>7 entonces permuta (**7, 34**, 23, 32, 5), pasa al siguiente elemento 34>23 entonces permuta (7, **23, 34**, 32, 5) volvería a permutar con el siguiente y así hasta que acaba el primer bucle y quedaría: (**7, 23, 32, 5, 34**)
        En el ***segundo bucle***, el 7 no permutaría y seguiría con el siguiente. Operaciones... **(7,23,5,32,34)**
        En el bucle final ya quedarían ordenados los elementos de menor a mayor.
    **Efectividad y debilidad**: Es efectiva cuando son listas pequeñas y no importa demasiado el rendimiento del programa, en cambio en listas grandes no sería el mejor método en términos de **optimización**.


Ejercicio Functools: Implementar una clase SimpleOperations que contenga métodos para calcular descuentos y tasas de impuestos. Posteriormente, utilizar functools.partial para crear versiones especializadas de estas funciones que se comporten de manera específica.
## Archivo SimpleOperations.py con functools
