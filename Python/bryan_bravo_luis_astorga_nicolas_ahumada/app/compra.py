from menucomida import listamenu
from time import sleep
import os
os.system("cls")

global listacompra
listacompra=list()

class Compra:
	nombre=""
	precio=0
	codigo=""
def compras(nombre,precio,codigo):
	
	c=Compra()
	
	c.nombre=nombre
	c.precio=precio
	c.codigo=codigo
	
	listacompra.append(c)

def registrarcompra():
	ciclo=True
	while ciclo:
		codigo=raw_input("ingrese codigo producto :")
		for m in listamenu:
			if m.codigo == codigo:
				compras(m.nombre,m.precio,m.codigo)
				print "agregado"
				sleep(0.5)
			
				
		os.system("cls")
		print "desea seguir agregando"
		print "1.-si"
		print "2.-no"
		salir=input("ingrese opcion :")
		os.system("cls")
		if salir ==2:
			break


			
		

def listacom():
	print "lista de compra"
	for c in listacompra:
		print "nombre :",c.nombre
		print "precio :",c.precio
		print "codigo :",c.codigo
		print "------------------"
	a=raw_input("precione enter ")
	os.system("cls")
	
def totalcompra():
	
	
	suma=0
	for c in listacompra:
		suma+=c.precio
		
	print "el total es :$",suma
	a=raw_input("precione enter")
	os.system("cls")
	
def imprimircompra():
	print "lista de compra"
	for c in listacompra:
		print "nombre :",c.nombre
		print "precio :",c.precio
		print "codigo :",c.codigo
		print "------------------"

	
	totalcompra()
	
		

	

