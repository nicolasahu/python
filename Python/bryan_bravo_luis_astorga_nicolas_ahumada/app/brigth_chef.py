import os
os.system("cls")
def main():
	ciclo=True
	while ciclo:
		print ""
		print ""
		print "bienvenido a  brigth chef"
		print ""
		print ""
		a=raw_input("precione enter para iniciar ")
		os.system("cls")
		print "-----menu-----"
		print "1.-ingresar"
		print "2.-salir"
		op=input("ingrese opcion :")
		os.system("cls")
		if op ==1:
			from usuarios import  Ingresousu
			Ingresousu()
		elif op ==2:
			print "gracias por utilizar esta aplicacion"
			ciclo=False

main()
