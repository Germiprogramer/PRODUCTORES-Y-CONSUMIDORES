# PRODUCTORES-Y-CONSUMIDORES

El link al repositorio es el siguiente: https://github.com/Germiprogramer/PRODUCTORES-Y-CONSUMIDORES.git

La tarea productores y consumidores consiste en crear unos elementos que produzcan un recurso, mientras haya otros que lo consuman. Para realizar el trabajo, he decidido basarme en la tarea del campus, siendo el producto un bollito. 

Partimos de un numero de bollos de pan base, que nuestro querido panadero ha horneado antes de el comienzo de la jornada laboral. Para ello, creamos una función para añadir bollos de pan a una queue, que será donde se almacenarán. A partir de ahí, los productores añadirán elementos a la queue, y los consumidores los consumirán. En nuestro ejemplo de aplicación hemos implementado un productor y dos consumidores. Los productores los hemos creado con la clase Thread, los consumidores con Timer, para que "lleguen a la tienda" en momentos distintos.

Para asegurarnos que cuando hay un único bollo los consumidores no lo consumen a la vez, se ha creado un semaforo cuyo contador se pondrá negativo cuando se trate de consumir mas bollos de los que hay, impidiendo dicha situación.

# EJEMPLO CON 5 BOLLOS



    PS C:\Users\Germán Llorente\Desktop\germiprogramer\PRODUCTORES-Y-CONSUMIDORES>  c:; cd 'c

    Introduce el numero de bollos: 5
    Los bollos iniciales son:  5

    Hay 5 bollos en el mostrador

    El consumidor- Wang está comiendo el bollo 2

    Maestro Zhang está produciendo el bollo 8

    El consumidor- Chen está comiendo el bollo 3

    Hay 4 bollos en el mostrador

    El consumidor- Wang está comiendo el bollo 4

    Maestro Zhang está produciendo el bollo 9

    Hay 4 bollos en el mostrador

    El consumidor- Chen está comiendo el bollo 6

    Maestro Zhang está produciendo el bollo 10

    Hay 4 bollos en el mostrador

    El consumidor- Wang está comiendo el bollo 7

    El consumidor- Chen está comiendo el bollo 8

    Maestro Zhang está produciendo el bollo 11

    Hay 3 bollos en el mostrador

    El consumidor- Wang está comiendo el bollo 9

    Maestro Zhang está produciendo el bollo 12

    Hay 3 bollos en el mostrador

    El consumidor- Chen está comiendo el bollo 10

    Maestro Zhang está produciendo el bollo 13

    Hay 3 bollos en el mostrador

    El consumidor- Wang está comiendo el bollo 11

    El consumidor- Chen está comiendo el bollo 12

    Maestro Zhang está produciendo el bollo 14

    Hay 2 bollos en el mostrador

    El consumidor- Wang está comiendo el bollo 13

    Maestro Zhang está produciendo el bollo 15

    Hay 2 bollos en el mostrador

    El consumidor- Chen está comiendo el bollo 14

    Maestro Zhang está produciendo el bollo 16

    Hay 2 bollos en el mostrador

    El consumidor- Wang está comiendo el bollo 15

    El consumidor- Chen está comiendo el bollo 16

    Maestro Zhang está produciendo el bollo 17

    Hay 1 bollos en el mostrador

    El consumidor- Wang está comiendo el bollo 17

    Maestro Zhang está produciendo el bollo 18

    Hay 1 bollos en el mostrador

    El consumidor- Chen está comiendo el bollo 18

    Maestro Zhang está produciendo el bollo 19

    Hay 1 bollos en el mostrador

    El consumidor- Wang está comiendo el bollo 19

    Maestro Zhang está produciendo el bollo 20
    El consumidor- Chen está comiendo el bollo 20


    Hay 0 bollos en el mostrador

    Maestro Zhang está produciendo el bollo 21
    El consumidor- Wang está comiendo el bollo 21


    Hay 0 bollos en el mostrador
