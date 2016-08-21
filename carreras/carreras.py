from IPython.display import clear_output  # Se necesita para limpiar la salida del notebook
import time  # Se necesita para dormir el programa
import random  # Se necesita para obtener la distancia aleatoria a avanzar
import os

participantes = ["Moto_de_agua","Monorriel"]  # Lista de los participantes de la carrera
distancia_de_meta = 0  # Tamaño de la pista de carreras en metros


class Vehiculo:
    tam_tanque = 0  # Tamaño del tanque de gasolina
    min_distancia = 0  # Cantidad máxima de metros que puede avanzar un carro en una iteración
    max_distancia = 0  # Cantidad mínima de metros que puede avanzar un carro en una iteración
    distancia_recorrida = 0  # Distancia recorrida por el vehículo

    def __init__(self):
        """Inicializa la clase padre del vehículo"""
        self.tanque = self.tam_tanque  # Llena el tanque del vehículo

    def avanzar(self):
        """
        Avanza el vehículo una cantidad aleatoria entre
        su distancia mínima y máxima reduciendo 1 unidad
        en su tanque de gasolina. Si este se encuentra vacio
        entonces el vehículo no avanza pero rellena su tanque.
        Si el vehículo ha llegado a la meta este ya no avanza.
        """
        pass

def imprime_carrera():
    """Imprime el estado de la carrera"""
    len_pista = 60  # Longitud en ascii del circuito de carreras
    pistas = ""
    for x in range(len(participantes)):  # Itera sobre los vehículos
        vehiculo = participantes[x]
        pista = "-" * len_pista
        posicion = (vehiculo.distancia_recorrida * len_pista) // distancia_de_meta
        posicion = min(len_pista, posicion)
        pista = pista[:posicion] + "*" + pista[posicion:]
        pistas += '\n{:2d} '.format(x) + pista
    clear_output(wait=True)
    print(pistas)

def avanza_carrera():
    """Avanza cada coche"""
    pass


def juego_terminado():
    """Indica si en el estado actual de la carrera hay al menos un ganador"""
    return True

def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu

    """
    os.system('clear')  # NOTA para windows tienes que cambiar clear por cls
    # clear_output(wait = True)
    print("      (---PARTICIPANTES---)")
    print("\t")
    print("\t1 - Moto de agua")
    print("\t2 - Monorriel")
    print("\t3 - Trailer")
    print("\t4 - Patines")
    print("\t5 - Helicoptero")
    print("\t")
    print("\t9 - salir")
    print("\t")

def entrada_menu():

    # Mostramos el menu
    menu()
    # solicituamos una opción al usuario
    opcionMenu = input("elegir vehiculo >> ")

    if (opcionMenu == "1"):
        print(" ")
        input("Moto de agua\npulsa una tecla para continuar")

    elif opcionMenu == "2":
        print("")
        input("Monorriel\npulsa una tecla para continuar")

    elif opcionMenu == "3":
        print("")
        input("Trailer\npulsa una tecla para continuar")

    elif opcionMenu == "4":
        print("")
        input("Patines\npulsa una tecla para continuar")

    elif opcionMenu == "5":
        print("")
        input("Helicoptero\npulsa una tecla para continuar")

    elif opcionMenu == "9":
        quit()

    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

def inicializa_participantes():
    """Le pregunta al usuario la cantidad y tipos de participantes
    que habrá en la carrera"""
    no_participantes = int(input("Número de participantes: "))
    entrada_menu()


def main():
    print("Juego comenzado.")
    # Aquí va su código
    while not juego_terminado():
        time.sleep(1)  # Se encarga de dormir el programa un segundo
    print("Juego terminado.")


class Moto_de_agua(Vehiculo):
    """
    self.tam_tanque = 3
    self.min_distancia = 1
    self.max_distancia = 4
    """

class Monorriel(Vehiculo):
    pass


class Trailer(Vehiculo):
    pass


class Patines(Vehiculo):
    pass


class Helicoptero(Vehiculo):
    pass

'''random.random()'''
inicializa_participantes()
imprime_carrera()

main()
