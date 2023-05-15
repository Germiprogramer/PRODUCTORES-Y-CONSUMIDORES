from queue import Queue
from threading import Thread, Timer, Semaphore
import time

num_bollos_inicial = int(input("Introduce el número de bollos: "))

# Queue que simula el mostrador
q = Queue(maxsize=num_bollos_inicial)

# Semaphore para controlar el acceso a los bollos
e = Semaphore(num_bollos_inicial)

def bollos_iniciales(num_bollos_inicial):
    print("Los bollos iniciales son:", num_bollos_inicial)
    for i in range(num_bollos_inicial):
        q.put(i+1)

bollos_iniciales(num_bollos_inicial)

def producer(name):
    """Productor"""
    count = num_bollos_inicial + 1  # Contador de bollos
    while True:
        q.put(count)
        e.acquire()
        print(f"{name} está produciendo el bollo {count}")
        count += 1
        print(f"Hay {q.qsize()} bollos en el mostrador")
        time.sleep(4)

def customer(name):
    """Consumidor"""
    while True:
        baozi = q.get(block=True)  # Si no hay bollos, espera
        print(f"El consumidor {name} está comiendo el bollo {baozi}")
        e.release()
        # Envía una señal después de comer
        time.sleep(6)

if __name__ == '__main__':
    t1 = Thread(target=producer, args=("Maestro Zhang",))
    t2 = Thread(target=customer, args=("Chen",))
    t3 = Thread(target=customer, args=("Wang",))

    t1.start()
    t2.start()
    t3.start()


    

    

    