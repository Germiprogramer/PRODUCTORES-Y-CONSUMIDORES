from classes import *
from queue import Queue
from threading import Semaphore

def bollos_iniciales(num_bollos_inicial):
    print("Los bollos iniciales son:", num_bollos_inicial)
    for i in range(num_bollos_inicial):
        q.put(i+1)

def crear_productores(n):
    if n > 0:
        productor = Productor(f"Productor {n}", num_bollos_inicial, q, e)
        productor.start()
        crear_productores(n - 1)

def crear_consumidores(n):
    if n > 0:
        consumidor = Consumidor(f"Consumidor {n}", q, e)
        consumidor.start()
        crear_consumidores(n - 1)


    
