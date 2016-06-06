# -*- coding: cp1252 -*-

import os
os.system("cls")
global Listausu
listausu=list()

class Usuarios:
	usuario=""
	clave=""
	
def Registrousu():
	u1=Usuarios()
	u2=Usuarios()
	u1.usuario="admin"
	u1.clave="admin"
	u2.usuario="admin2"
	u2.clave="admin2"
	
	listausu.append(u1)
	listausu.append(u2)


	
	
def Ingresousu():
	Registrousu()
	cont=0
	resta=4
	while resta !=0:
		print "ingrese datos de usuario"
		usu=raw_input("usuario :")
		con=raw_input("clave :")
		os.system("cls")
		resta-=1
		existe=False	
		for u in listausu:
			if u.usuario == usu and  u.clave == con:
				existe=True
		if existe == True:
			print ""
			print "----------------"
			print "acceso concedido"
			from total import menu
			menu()

			
			break
			
		else :
			print "datos erronios"
			print "quedan",resta,"intentos"

		
	
		
		
		
	
	
	
	
