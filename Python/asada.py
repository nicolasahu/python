#Permita  ingresa  n  edades.  El  programa  debe  decir
#cuántas  personas  son  mayor  de 
#edad y cuantas son menores de edad.

edad = input("Ingrese cant edades:2")
mayor=0
menor=0
CONT = 0

while CONT < edad:
    E1= input("iNGRESE SU EDAD")
    if E1>= 18:
        mayor=mayor+1
    else:
        menor +1
    CONT=CONT+1
print "moyores" , mayor
print "menores" , menor
