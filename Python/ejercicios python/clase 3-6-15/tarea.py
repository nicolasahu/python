# -*- coding: cp1252 -*-
global lista1
lista1=list()
global lista2
lista2=list()

#defino los atributos 
class trabajadores :
	nombre=""
	rut =""
	sueldo=0
	dias=0
	
class peliculas:
	nombre=""
	genero=""
	ano=0
	
def registrartrabajador():
	print "--registro de trabajadores--"
	a=trabajadores()
	a.nombre=raw_input("ingrese nombre :")
	a.rut=raw_input("ingrese rut :")
	a.sueldo=input("ingrese sueldo :")
	a.dias=input("ingrese dias trabajados :")
	lista1.append(a)
	print "------------------------------"

def registrarpeli():
	print "---registro de peliculas---"
	b=peliculas()
	b.nombre=raw_input("ingrese nombre pelicula :")
	b.genero=raw_input("ingrese genero pelicula :")
	b.ano=input("ingrese  año de estreno :")
	lista2.append(b)
	

def listatrabajador():
	print "---lista de trabajadores---"
	for a in lista1:
		print "nombre :", a.nombre
		print "rut :",a.rut
		print "sueldo :", a.sueldo
		print "dias trabajados :",a.dias
		print "----------------------"
	
def listapeli():
	print "---lista de peliculas---"
	for b in lista2:
		print "nombre :", b.nombre
		print "genero :",b.genero
		print "año de estreno :",b.ano
		print "----------------------"
		
		
		
def buscartrabajador():
	print "---busqueda de trabajador---"
	opcion=raw_input("ingrese opcion(nombre o rut) :")
	
	for a in lista1:
		
		if opcion == a.nombre or opcion== a.rut:
			
			print "datos del trabajador "
			print "nombre :", a.nombre
			print "rut :",a.rut
			print "sueldo :", a.sueldo
			print "dias trabajados :",a.dias
			print "----------------------"
			
def buscarpeli():
	print "---busqueda de peliculas---"
	opcion=raw_input("ingrese nombre de la pelicula :")
	for b in lista2:
		if b.nombre==opcion:
			
			print "nombre :", b.nombre
			print "genero :",b.genero
			print "año de estreno :",b.ano
			print "----------------------"
			
	

			
def salir():
	print "gracias por usar esta opcion"
	print "------------------------------"
	
def salirb():
	print  "gracias por utilizar esta aplicacion"		
	
def menutrabajadores ():
	ciclo=True
	while ciclo:
		
		
	
		print "---menu---"
		print "1.-registrar trabajadores"
		print "2.-lista de trabajadores"
		print "3.-buscar trabajador"
		print "4.-salir"
		t=input("ingrese opcion :")
		if t==1:
			registrartrabajador()
		elif t ==2:
			listatrabajador()
		elif t==3:
			buscartrabajador()
		elif t==4:
			salir()
			ciclo=False
		else:
			print "digito erronio"
	
	
def menupeliculas():
	ciclo=True
	while ciclo:
		
		print "---menu---"
		print "1.-registrar pelicula"
		print "2.-lista de peliculas"
		print "3.-buscar pelicula"
		print "4.-salir"
	
		peli=input("ingrese opcion :")
		if peli==1:
			registrarpeli()
		elif peli ==2:
			listapeli()
		elif peli==3:
			buscarpeli()
		elif peli==4:
			salir()
			ciclo=False
		else:
			print "digito erronio"
	
	
	

def menu():
	ciclo=True
	while ciclo:
		
		print "-------menu-------"
		print "1.-trabajadores"
		print "2.-peliculas"
		print "3.- salir "
		opcion=input("ingrese opcion :")
		if opcion ==1:
			menutrabajadores ()
		elif opcion==2:
			menupeliculas()
		elif opcion==3:
			salirb()
			ciclo=False
		else:
			print "digito erronio"
			
menu()
			
			
		

