#creee una funcion que permita entregarle 1perimetro
#(nummes).segun el numero de mes
#entregado, escribir el mes correspondiente en palabras 
def mes(numMes):
	if numMes ==1:
		print "enero"
	elif numMes == 2:
		print "febrero"
	elif numMes == 3:
		print "marzo"
	elif numMes ==4:
		print "abril"
	elif numMes==5:
		print "mayo"
	elif numMes==6:
		print "junio"
	elif numMes==7:
		print "julio"
	elif numMes ==8:
		print "agosto"
	elif numMes==9:
		print "septiembre"
	elif numMes==10:
		print "octubre"
	elif numMes==11:
		print "noviembre"
	elif numMes==12:
		print "diciembre"
	else :
		print"numero erronio"
def mensaje():
	print "gracias por utilizar esta aplicacion"
	
def main():
	ciclo=True
	while ciclo:
		numMes=input("ingrese numero de mes (1-12):")
		mes(numMes)
		
		print"desea salir"
		print "1.-si"
		print "2.-no"
		salir=input("desea salir :")
		if salir == 1:
			ciclo= False
	mensaje()
main()
			
	
