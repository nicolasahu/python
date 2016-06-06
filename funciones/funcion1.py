##cree una lista que permita entregar 2 parametros(a,b),
# mustre el resultado de a elevado a "b" en dicha funcion
def numeros(a,b):
	elevado=a**b
	print "el resultado de",a,"elevado a ",b,"es :",elevado

def mensaje():
	print "gracias por usar esta aplicacion"

def main():
	ciclo=True
	while ciclo:
		a=input("ingrese primer numero :")
		b=input("ingrese segundo numero :")
		
		numeros(a,b)
		print "desea salir "
		print "1.-si"
		print "2.-no"
		salir=input("desea salir :")
		if salir==1:
			ciclo=False
	mensaje()
		
main()
