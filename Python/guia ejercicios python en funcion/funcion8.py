#Permita estar ingresando numeros hasta
# que el usuario ingrese -100. En ese momento, 
#mostrar la cantidad de numeros ingresados.
def cantidad(num):
	cont=0
	while num != -100 :
		cont+=1
		num=input("ingrese numero :")
	print "cantidad de nuemros ingresados :",cont
	
def main():
	num=input("ingrese numero :")
	cantidad(num)
main()
	


