
def bisiesto(anno):
	if anno%4==0 or (anno%100!=0 and anno%400==0):
		return True

a=input("Ingrese el anno a comprobar: ")
r=bisiesto(a)
if r==True:
	print "Es bisiesto."
else:
	print "No es bisiesto"
