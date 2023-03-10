from queue import Queue

import threading

from threading import Thread, Timer, Semaphore

import time

num_bollos_inicial = int(input("Introduce el numero de bollos: "))

# queue que simula el mostrador

q = Queue(maxsize=num_bollos_inicial)

# semaforo para que los consumidores no consuman el mismo bollo

e = Semaphore(num_bollos_inicial)

def bollos_iniciales(num_bollos_inicial):

    print("Los bollos iniciales son: ", num_bollos_inicial)

    for i in range(num_bollos_inicial-1):

        q.put(i+1)

bollos_iniciales(num_bollos_inicial)

def producer(name):

    """Productor"""

    count = 1 + num_bollos_inicial #mostrador

    while True:

        q.put(count)

        e.acquire()

        print(f"{name} está produciendo el bollo {count}" + "\n")

        count+=1

        print("Hay",q.qsize(),"bollos en el mostrador" + "\n")

        time.sleep(5)

def customer(name):

    """consumidor"""

    count = 1

    while True:

        baozi = q.get(block=True) # Si no hay bollos, no espera

        print(f"El consumidor- {name} está comiendo el bollo {baozi}" + "\n")

        e.release()

        count+=1

        # Envía una señal después de comer

        time.sleep(8)



if __name__ == '__main__':

    t1 = Thread(target=producer,args=("Maestro Zhang",))

    t2 = Timer(2,customer,args=("Chen",))
    
    t3 = Timer(5,customer,args=("Wang",))

    t1.start()

    t2.start()

    t3.start()

    

    

    