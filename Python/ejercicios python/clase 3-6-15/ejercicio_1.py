global lista
lista=list()
#defino los atributos 
class alumno :
	rut =""
	nombre=""
	edad=0
	
def registraralumno():
	print "registro de alumno"
	a=alumno()
	
	a.rut=raw_input("ingrese rut :")
	a.nombre=raw_input("ingrese nombre :")
	a.edad=input("ingrese edad :")
	lista.append(a)
	print "----------"
def listaalumno():
	print "lista de alumnos"
	print "-----------------"
	for a in lista:
		print "rut :",a.rut
		print "nombre :", a.nombre
		print "edad:", a.edad
		print "----------"
def buscaralumno():
	print "busqueda de alumno"
	datos=raw_input("ingrese rut alumno :")
	#recorer la lista
	for a in lista:
		if a.rut ==datos or a.nombre ==datos:
			print "rut :",a.rut
			print "nombre :", a.nombre
			print "edad:", a.edad
			print
		
			
	print "----------"
def salir ():
	print "salir"
	print "----------"
	
def menu():
	op = 0
	
	while op !=4:
		#mostrar el menu
		print "menu"
		print "1.- registrar alumnos"
		print "2.-lista alumnos"
		print "3.-buscar alumno"
		print "4.-salir"
		op=input( "dgite opcion :")
		
		if op ==1:
			registraralumno()
		elif op==2:
			listaalumno()
		elif op ==3:
			buscaralumno()
		elif op==4:
			salir()
			


menu()


