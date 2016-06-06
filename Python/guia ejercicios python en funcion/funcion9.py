#Permita  estar  ingresando  numeros  hasta  que  
#el  usuario  ingrese  -1000.  En  ese 
#momento, mostrar la cantidad de numeros igual a 100
def cantidad (num):
	cont=0 
	while num!=-1000:
		if num == 100:
			cont+=1
		num=input("ingrese numero :")
			
	print "cantidad de veces ingresado 100 :",cont

def main():
	num=input("ingrese numero :")
	cantidad(num)
	
main()
			

