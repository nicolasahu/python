#Permita  ingresar  notas.  El  programa  debe  estar
#  pidiendo  notas  hasta  que  ingrese  la 
#nota -1. Decir cuantas notas azules hay, cuantas rojas.
def notas (num):
	rojo=0
	azul=0
	while num!=-1:
		
		if num >=4:
			azul+=1
		else:
			rojo+=1
		num=input("ingrese nota :")
	print "notas azules :",azul
	print "nota rojas :",rojo
	
def main():
	num=input("ingrese nota :")
	notas(num)

main()
		
		
		
		
		
		
	

