
def dia(numDia):
	if numDia== 1:
		print "Lunes"
	elif numDia== 2:
		print "Martes"
	elif numDia== 3:
		print "Miercoles"
	elif numDia== 4:
		print "Jueves"
	elif numDia== 5:
		print "viernes"
	elif numDia== 6:
		print "Sabado"
	elif numDia== 7:
		print "domingo"
	else:
		print" numero erroneo :"
		
def mensaje():
	print"Gracias"
	
def principal():
	ciclo= True
	
	while ciclo:
		numDia= input("Ingrese dia (1-7 :")
		dia (numDia)
		
		print "Desea salir"
		print "1-si"
		print "2-no"
		
		salir = input("Desea salir:")
		if salir == 1:
			break
	mensaje ()
principal ()
	
