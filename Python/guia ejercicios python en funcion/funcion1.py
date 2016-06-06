#permita pedir nombre y edad. muistre por ppantalla
def edad (nombre,edad):
	print "nombre :", nombre 
	print "edad :",edad

def principal():
	n=raw_input("ingrese el nombre :")
	e=input("ingrese edad :")
	edad(n,e)
	
principal()
