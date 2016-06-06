#Realice un programa que permita el ingreso de una 
#edad. Diga si es menor o mayor de 
#edad.
def edad(n):
	if n >= 18:
		print "eres mayor de edad "
	else :
		print "eres menor de edad"
def main():
	n=input("ingrese edad :")
	edad(n)
	
main()
