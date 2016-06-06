#cree una funcion que segun la una edad entregada por parametro
#diga si es menor o mayorde edad
def edad(e):
	if e>=18:
		print "eres mayor de edad"
	else:
		print "eres menor de edad"
	
def mensaje():
	print "gracias por utilizar la aplicacion"
def main():
	ciclo=True
	while ciclo:
		e=input("ingrese edad :")
		edad(e)
		
		print"desea salir"
		print "1.-si"
		print "2.-no"
		salir=input("desea salir :")
		if salir == 1:
			ciclo= False
	mensaje()
	
main()
	

