#Permita el ingreso de n numeros.
# Al final muestre la suma y la cantidad de numeros 
#ingresados
def suma (limite):
	cont=0
	suma=0
	while cont <limite:
		num=input("ingrese numero :")
		suma=suma+num
		cont+=1
		
	print "la suma de los numeros es :",suma
	print "la cantidad de numeros ingresados es :",limite
	
def main():
	limite=input("ingrese cantidad de numeros :")
	suma(limite)
	
main()
