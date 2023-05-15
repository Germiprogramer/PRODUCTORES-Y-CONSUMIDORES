from threading import Thread
import time

class Productor(Thread):

    def __init__(self, name, num_bollos_inicial, q, e):
        Thread.__init__(self)
        self.name = name
        self.num_bollos_inicial = num_bollos_inicial
        self.q = q
        self.e = e


    def run(self):
        count = self.num_bollos_inicial + 1  # Contador de bollos
        while True:
            self.q.put(count)
            self.e.acquire()
            print(f"{self.name} está produciendo el bollo {count}")
            count += 1
            print(f"Hay {self.q.qsize()} bollos en el mostrador")
            time.sleep(4)

class Consumidor(Thread):

    def __init__(self, name, q, e):
        Thread.__init__(self)
        self.name = name
        self.q = q
        self.e = e


    def run(self):
        while True:
            baozi = q.get(block=True)  # Si no hay bollos, espera
            print(f"El consumidor {self.name} está comiendo el bollo {baozi}")
            e.release()
            # Envía una señal después de comer
            time.sleep(6)