def actualizar(puntos):
	global pun_tot,pun_gra

	pun_tot += puntos

	erase(pun_gra)
	pun_gra = create_text(500,500,pun_tot,16,"CENTER")

	return

pun_tot = 0
pun_gra = create_text(500,500,pun_tot,16,"CENTER")

puntos = int(input("Puntos : "))
while puntos != -1:
	actualizar(puntos)
	puntos = int(input("Puntos : "))

