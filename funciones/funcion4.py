# cree una funcion que permita entregarle 1 parametro (contnotas)
# la funcion debe pedir las notas necesarias al usuario al final 
#del ingreso mostrar el promedio del curs. en la funcion principal 
#se debe pedir cuantas notas  desea ingresar y entregarselas como
# parametro a la funcion.
def nota(cantnota):
	cont=0
	suma=0
	while cont < cantnota:
		nota=input("ingrese nota:")
		suma=suma+nota
		cont+=1
	promedio=suma/cantnota
	print "el promedio es :",promedio
	
def mensaje():
	print "gracias por utilizar esta aplicacion"
	
def main():
	ciclo=True
	while ciclo:
		cantnota=input("ingrese cantidad de notas :")
		nota(cantnota)
		
		
		print"desea salir"
		print "1.-si"
		print "2.-no"
		salir=input("desea salir :")
		if salir == 1:
			ciclo= False
	
	mensaje()
main()
		

