#permita pedir dos numeros y realisar las operaciones 
#basicas con ellas (suma-resta-multiplicaciony divicion)
def calculadora(num1,num2):
	suma = num1 + num2
	resta =num1 - num2
	multiplicacion = num1 * num2
	divicion= num1 / num2
	print "el resultado de la suma entre ",num1 ,"y",num2 ,"es :",suma
	print "el resultado de la resta entre ",num1 ,"y",num2 ,"es :",resta
	print "el resultado de la multiplicacion entre ",num1 ,"y",num2 ,"es :",multiplicacion
	print "el resultado de la divicion entre ",num1 ,"y",num2 ,"es :",divicion


def main():
	num1=input("ingrese primer numero :")
	num2=input("ingrese segundo numero :")
	calculadora(num1,num2)
	
main()
