#Permita estar ingresando numeros hasta que
# el usuario ingrese  -1. En ese momento, 
#mostrar la suma y promedio
def pro(num):
	suma=0
	cont=0
	while num != -1 :
		suma=suma+num
		cont+=1
		num=input("ingrese numero :")
	promedio=suma/cont
	print "la suma de los numeros es :",suma
	print "el promedio de los numeros es :",promedio
	
		
def main():
	num=input("ingrese numero :")
	pro(num)
	
main()
		
	
