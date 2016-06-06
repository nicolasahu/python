#Permita el ingreso de n numeros. 
#Al final muestre el promedio de ello

def pro(limite):
	cont=0
	suma=0
	while cont < limite :
		num=input("ingrese numero :")
		suma = suma + num
		cont+=1
	promedio=suma/limite
	print "el promedio es :",promedio
	
def main():
	limite=input("ingrese cantidad de numeros :")
	
	pro(limite)
	
main()
	
	
