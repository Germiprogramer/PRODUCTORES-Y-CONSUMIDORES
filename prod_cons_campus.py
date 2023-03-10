from queue import Queue

from threading import Thread

import threading

import time

# Crear cola

num_bollos_inicial = int(input("Introduce el numero de bollos: "))

q = Queue(maxsize=num_bollos_inicial)

e = threading.Semaphore(num_bollos_inicial)

def bollos_iniciales(num_bollos_inicial):

    print("Los bollos iniciales son: ", num_bollos_inicial)

    for i in range(num_bollos_inicial-1):

        q.put(i+1)

    print(q.queue)

bollos_iniciales(num_bollos_inicial)

def producer(name):

    """Productor"""

    count = 1 + num_bollos_inicial #mostrador

    while True:

        # Espera a task_done () para enviar una señal

        q.put(count)

        e.acquire()

        print(f"{name} está produciendo el bollo {count}" + "\n")

        count+=1

        #printear una queue

        print("Hay",q.qsize(),"bollos en el mostrador" + "\n")

        time.sleep(2)

def customer(name):

    """consumidor"""

    count = 1

    while True:

        baozi = q.get(block=True) # Si no hay bollos, no espera

        print(f"El consumidor- {name} está comiendo el bollo {baozi}" + "\n")

        e.release()

        count+=1

        # Envía una señal después de comer

        time.sleep(2)



if __name__ == '__main__':

    t1 = Thread(target=producer,args=("Maestro Zhang",))

    t2 = Thread(target=customer,args=("Chen",))
    
    t3 = Thread(target=customer,args=("Wang",))

    t1.start()

    t2.start()

    t3.start()

    

    

    