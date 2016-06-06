#Permita el ingreso de n numeros. Al final muestre 
#la suma de ellos
def suma(limite):
	cont=0
	suma=0
	pru=1
	while cont<limite:
		num=input("ingrese numero :")
		suma=suma+ num
		cont+=1
		pru+=1
	
	print "la suma de los nmeros es :",suma
	
def main():
	limite=input("ingrese n numeros :")
	suma(limite)
	
main()
	

