from IPython.display import clear_output  # Se necesita para limpiar la salida del notebook
import time  # Se necesita para dormir el programa
import random  # Se necesita para obtener la distancia aleatoria a avanzar
import os


participantes = []  # Lista de los participantes de la carrera
distancia_de_meta = 10  # Tamaño de la pista de carreras en metros
no_participantes = 0
posicion = 0

#CLASE VEHICULO (1)

class Vehiculo:
    '''
    tam_tanque = 2  # Tamaño del tanque de gasolina
    min_distancia = 2  # Cantidad máxima de metros que puede avanzar un carro en una iteración
    max_distancia = 2  # Cantidad mínima de metros que puede avanzar un carro en una iteración
    distancia_recorrida = 0  # Distancia recorrida por el vehículo
    '''
    def __init__(self):
        """Inicializa la clase padre del vehículo"""
        self.tanque = 2
        self.tam_tanque = 3
        self.min_distancia = 3
        self.max_distancia = 5
        self.distancia_recorrida = 0
        self.tanque = self.tam_tanque  # Llena el tanque del vehículo

        
    def avanzar(self):
        """
        Avanza el vehículo una cantidad aleatoria entre
        su distancia mínima y máxima reduciendo 1 unidad
        en su tanque de gasolina. Si este se encuentra vacio
        entonces el vehículo no avanza pero rellena su tanque.
        Si el vehículo ha llegado a la meta este ya no avanza.
        """
        self.tanque -= 1
        self.distancia_recorrida = self.distancia_recorrida + random.randint(self.min_distancia,self.max_distancia)

#PARTICIPANTES DE LA CARRERA (2)


class Moto_de_agua(Vehiculo):
    tanque = 0
    def _init_(self):
        super._init_()
        self.tanque = 2
        self.tam_tanque = 3
        self.min_distancia = 0
        self.max_distancia = 1
        self.distancia_recorrida = 0
  
class Monorriel(Vehiculo):
    def _init_(self):
        super._init_()
        self.tanque = 1
        self.tam_tanque = 5
        self.min_distancia = 0
        self.max_distancia = 2
        self.distancia_recorrida = 0


class Trailer(Vehiculo):
    def _init_(self):
        super._init_()
        self.tanque = 2
        self.tam_tanque = 2
        self.min_distancia = 0
        self.max_distancia = 1
        self.distancia_recorrida = 0


class Patines(Vehiculo):
    def _init_(self):
        super._init_()
        self.tanque = 1
        self.tam_tanque = 2
        self.min_distancia = 2
        self.max_distancia = 3
        self.distancia_recorrida = 0


class Helicoptero(Vehiculo):
    def _init_(self):
        super._init_()
        self.tanque = 2
        self.tam_tanque = 2
        self.min_distancia = 1
        self.max_distancia = 3
        self.distancia_recorrida = 0


moto_de_agua = Moto_de_agua()
monorriel = Monorriel()
trailer = Trailer()
patines = Patines()
helicoptero = Helicoptero()



#IMPRIME CARRERA (3)

def imprime_carrera():
    """Imprime el estado de la carrera"""
    len_pista = 60 # Longitud en ascii del circuito de carreras
    pistas = ""
    global posicion
    for x in range(len(participantes)):  # Itera sobre los vehículos
        vehiculo = participantes[x]
        pista = "-" * len_pista
        posicion = (vehiculo.distancia_recorrida * len_pista) // distancia_de_meta
        posicion = min(len_pista, posicion)
        pista = pista[:posicion] + "*" + pista[posicion:]
        pistas += '\n{:2d} '.format(x) + pista
    clear_output(wait=True)
    print(pistas)

#AVANZA CARRERA (4)

def avanza_carrera():
    """Avanza cada coche"""
    moto_de_agua.avanzar()
    monorriel.avanzar()
    trailer.avanzar()
    patines.avanzar()
    helicoptero.avanzar()



def juego_terminado():
    """Indica si en el estado actual de la carrera hay al menos un ganador"""
    global posicion
    if (posicion < 60):
        return True 

    else:
        return False



#MI MENU (5)


def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    #os.system('clear') 
    clear_output(wait = True)
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

#ELECCION MENU (6)

def entrada_menu():

    # Mostramos el menu
    menu()
    # solicituamos una opción al usuario
    opcionMenu = input("elegir vehiculo >> ")
    global participantes
    global moto_de_agua
    global monorriel
    global trailer
    global patines 
    global helicoptero

    if (opcionMenu == "1"):
        participantes.append(moto_de_agua)

    elif opcionMenu == "2":
        participantes.append(monorriel)

    elif opcionMenu == "3":
        participantes.append(trailer)

    elif opcionMenu == "4":
        participantes.append(patines)

    elif opcionMenu == "5":
        participantes.append(helicoptero)

    elif opcionMenu == "9":
        quit()

    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

def inicializa_participantes():
    """Le pregunta al usuario la cantidad y tipos de participantes
    que habrá en la carrera"""
    global no_participantes
    no_participantes = int(input("Número de participantes: "))
    while (no_participantes > 0):
        entrada_menu()
        no_participantes -= 1


def main():
    global posicion
    print("Juego comenzado.")
    # Aquí va su código
    inicializa_participantes()
    while juego_terminado():
        clear_output(True)
        os.system("clear")
        imprime_carrera()
        avanza_carrera()
        time.sleep(2)  # Se encarga de dormir el programa un segundo

    print("Juego terminado.")

main()