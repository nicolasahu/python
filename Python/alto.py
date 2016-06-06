global lista
lista=list()

class Sueldo:
	nombre=""
	sueldo=0

def Registrar():
	s=Sueldo()
	s.nombre=raw_input("ingrese nombre :")
	s.sueldo=input("ingrese sueldo :")
	lista.append(s)
	

			
def Mayor():
	mayorn=""
	mayors=0
	menorn=""
	menors=0
	cont=0
	for s in lista :
		if cont == 0:
			mayorn=s.nombre
			mayors=s.sueldo
			menorn=s.nombre
			menors=s.sueldo
		elif s.sueldo > mayors :
			
			mayorn=s.nombre
			mayors=s.sueldo
		elif s.sueldo < menors:
			menorn=s.nombre
			menors=s.sueldo
		cont+=1
	
	
	print "sueldo mayor"
	print ""
	print "nombre :",mayorn
	print "sueldo :",mayors
def Menor():
	mayorn=""
	mayors=0
	menorn=""
	menors=0
	cont=0
	for s in lista :
		if cont == 0:
			mayorn=s.nombre
			mayors=s.sueldo
			menorn=s.nombre
			menors=s.sueldo
		elif s.sueldo > mayors :
			
			mayorn=s.nombre
			mayors=s.sueldo
			print "mayor"
		elif s.sueldo < menors:
			menorn=s.nombre
			menors=s.sueldo
			print "menor"
		cont+=1

	
	print "sueldo menor"
	print ""
	print "nombre :",menorn
	print "sueldo :",menors
	
			


def  main():
	ciclo=True
	
	while ciclo:

		print "menu"
		print "1.-registrar"
		print "2.-ver sueldo mayor"
		print "3.-ver sueldo menor"
		print "4.-salir"
		op=raw_input("ingrese opcion :")
		if op == "1":
			Registrar()
		elif op == "2":
			Mayor()
		elif op == "3":
			Menor()
		elif op == "4":
			ciclo=False
			
main()
			

