def elevado(a,b):
	
	cont=0
	acum=1
	while cont < b:
		acum=acum*a
		cont+=1
	
	print acum
	
def mensaje():
	print "gracias por utilizar esta aplicacion"
def main ():
	ciclo=True
	while ciclo:
		a=input("ingrese primer  numero :")
		b=input("ingrese segundo numero :")
		elevado(a,b)
		print "desea salir"
		print "1-si"
		print "2-no"
		salir =input("desea salir :")
		if salir == 1:
			ciclo=False
	mensaje()
	
main()	
	


