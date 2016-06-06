# Permita ingresar edades. El programa debe
# estar pidiendo edades hasta que ingrese la 
#edad  -100.  Decir  cuantas  personas  son  
#de  la  tercera  edad  (mayor  a  50)  y  cuantas 
#edades se ingresaron

def edad (e):
	cont=0
	mayor=0
	while e != -100 :
		if e>= 50:
			mayor+=1
		cont+=1
		e=input("ingrese edad :")
	print "numero de personas mayores de edad :",mayor
	print "numero de edades ingresadas :",cont
		
def main():
	e=input("ingrese edad :")
	edad(e)
	
main()
	
		
		
	
	

