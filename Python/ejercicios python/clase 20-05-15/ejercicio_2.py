#definicion de funciones
def pedirdatos():
	from time import sleep
	limite=input("cantidad de vueltas :")
	mensaje=raw_input("mensaje :")
	
	cont=0
	while cont< limite:
		print mensaje
		sleep(0.5)
		
		cont+=1
def mensaje():
	print "gracias por utilizar la aplicacion "
	
def principal():
	pedirdatos ()
	
	
	mensaje()
#definicion de funciones

print principal()
