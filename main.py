from prod_cons import *

if __name__ == "__main__":
    num_bollos_inicial = int(input("Introduce el número de bollos inicial: "))
    num_consumidores = int(input("Introduce el número de consumidores: "))
    num_productores = int(input("Introduce el número de productores: "))

    # Queue que simula el mostrador
    q = Queue(maxsize=num_bollos_inicial)

    # Semaphore para controlar el acceso a los bollos
    e = Semaphore(num_bollos_inicial)
    bollos_iniciales(num_bollos_inicial)

    crear_productores(num_productores)
    crear_consumidores(num_consumidores)