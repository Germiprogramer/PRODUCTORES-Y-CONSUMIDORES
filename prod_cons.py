import threading

n = int(input("Introduce el numero de productos: "))

#procesos que faltan por producir
e = threading.Semaphore(n)
#procesos disponibles para consumir
f = threading.Semaphore(0)
#indica si el buffer está en uso
b = threading.Semaphore(1)

#semaforo = numero llamadas a acquire - numero llamadas a release + valor inicial // si es negativo, el hilo se bloquea

buffer = list()


class Producer(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self)
        self.nombre = nombre
    
    def producir(self): 
        while(True):
            dato = "a"
            e.acquire()
            b.acquire()
            print("{} Añadiendo dato al buffer en la posicion: ".format(self.nombre), len(buffer))
            buffer.append(dato)
            b.release()
            f.release()

class Consumer(threading.Thread):

    def __init__(self, nombre):
        threading.Thread.__init__(self)
        self.nombre = nombre
    
    def consumir(self):
        while(True):
            f.acquire()
            b.acquire()
            print("{} consumiendo dato del buffer en la posicion: ".format(self.nombre), len(buffer)-1)
            buffer.pop()
            b.release()
            e.release()

def main():
    p = Producer("Productor1")
    c = Consumer("Consumidor1")
    c2 = Consumer("Consumidor2")
    hilo1 = threading.Thread(target=p.producir)
    hilo2 = threading.Thread(target=c.consumir)
    hilo3 = threading.Thread(target=c2.consumir)
    hilo1.start()
    hilo2.start()
    hilo3.start()

main()