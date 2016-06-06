# -*- coding: cp1252 -*-
#Permita  ingresa  n  edades.  El  programa  debe  decir  cuántas
#personas  son  mayor  de 
#edad y cuantas son menores de edad

limite=input("ingrese cantidad de edades :")

cont=0
mayor=0
menor=0
while cont<limite:
    edad=input("ingrese edad :")
    cont=cont +1
    if edad < 18:
        menor=menor+1

    else:
        mayor = mayor +1



print "numero de personas mayores de 18 años es :",mayor
print "numero de personas menor a 18 años es :",menor
    



