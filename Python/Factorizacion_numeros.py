#Factorial de un numero digitado

import math

a=int(input("Inggrese un numero: "))
if a<0:
	print "Digite un numero positivo...."
else:
	a=math.factorial(a)
	print a
