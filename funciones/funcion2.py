#cree una funcion que permitaentregar un parametr(numdia).
#segun el numero de dia entregado, escribir el dia corespondiente en pantalla.
def dia(numdia):
	if numdia==1:
		print "lunes"
		print "------------"
	elif numdia==2:
		print "martes"
		print "------------"
	elif numdia==3:
		print"miercoles"
		print "------------"
	elif numdia==4:
		print "jueves"
		print "------------"
	elif numdia==5:
		print "viernes"
		print "------------"
	elif numdia==6:
		print "sabado"
		print "------------"
	elif numdia==7:
		print "domingo"
		print "------------"
	else:
		print"numero erronio"

def mensaje():
	print "gracias por utilizar esta aplicacion"
	
def main():
	ciclo=True
	while ciclo:
		numdia=input("ingrese dia (1-7) :")
		dia(numdia)
		
		print"desea salir"
		print "1.-si"
		print "2.-no"
		salir=input("desea salir :")
		if salir == 1:
			ciclo= False
	
	mensaje()
	
main()
