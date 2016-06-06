#definicion de funcion

#parametros(las variables que le entrege  a la  funcion )
#esta funcion sumara 2 numeros entregados por para metro
#y mostrar el resultadoo
def sumar(n1,n2):
        suma=n1+n2
        print "la suma es :",suma
	
def principal():
        print "------------"
        print "bienvenido a mi software"
        print "------------------------"
        n1=input("ingrese numero 1 :")
        n2=input("ingrese numero 2 :")
        sumar(n1,n2)
        print "------------------------"
        print suma
# definicion de funcion

principal()
