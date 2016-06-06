#Meses del ano <- cmd xd...
import os
re=True
r=True
mes=["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
while r==True:
	meses=raw_input("Ingrese numero del mes (1 al 12): ")
	re=meses.isdigit()
	if re==True:
		meses=int(meses)
		if meses in range(1, 13):
			print mes[meses]
		else:
			print "Please digite un valor correcto, no sea un ricardo....."
	else:
		print "Please digite un valor correcto, no sea un ricardo....."
	com=True
	while com==True:
		salir=raw_input("Desea continuar? (S/N): ")
		salir=salir.upper()
		if salir=='S' or salir=='N':
			com=False
		else:
			print "Digite una respuesta correcta..."
	if salir=='N':
		os.system('cls')
		print "Muchas gracias por utilizar el programa..."
		break
	os.system('cls')
