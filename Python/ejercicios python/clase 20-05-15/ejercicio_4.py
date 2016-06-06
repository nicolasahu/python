
def menu():
	ciclo=True
	while ciclo:
		print "1.- Sumar"
		print "2.- Restar"
		print "3.- Dividir"
		print "4.- Multiplicar"
		print "5.- Salir"
		n=input("ingrese opcion :")
		if n==5:
			break
		num1=input("ingrese numero 1 :")
		num2=input("ingrese numero 2 :")
		
		if n==1:
			
			suma = num1+num2
			print "respuesta :" ,suma
		elif n==2:
			resta= num1-num2
			print "respuesta :" ,resta
			
		elif n==3:
			dividir=num1/num2
			print "respuesta :",dividir
			
		elif n==4:
			multiplicar=num1*num2
			print "respuesta :" ,multiplicar


def mensaje ():
	print "Gracias por utilizar la aplicacion"
	
def main():
	
	menu()
	mensaje()
	
main()
	
	
			
		
	

