#Permita  ingresa  n  edades.  El  programa 
# debe  decir  cuantas  personas  son  mayor  de 
#edad y cuantas son menores de edad. 

def edades(limite):
	cont=0
	mayor=0
	menor=0
	while cont < limite:
		edad=input("ingrese edad :")
		if edad >=18:
			mayor+=1
		else :
			menor+=1
		cont+=1
			
	print "personas mayores de edad :",mayor
	print "personas menores de edad :",menor
def main():
	limite=input("ingrese cantidad de edades :")
	edades(limite)
	
main()

