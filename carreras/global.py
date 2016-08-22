from IPython.display import clear_output  # Se necesita para limpiar la salida del notebook


def actualizar(puntos):
	global pun_tot,pun_gra

	pun_tot += puntos

	clear_output()
	pun_gra = print(pun_tot)

	return

pun_tot = 0
pun_gra = print(pun_tot)

puntos = int(input("Puntos : "))
while puntos != -1:
	actualizar(puntos)
	puntos = int(input("Puntos : "))

