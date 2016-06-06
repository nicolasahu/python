# -*- coding: cp1252 -*-
#Permita estar ingresando números hasta que el usuario ingrese -100.
#En ese momento, mostrar la cantidad de números ingresados

a=input("ingrese numero :")
cont=0
while a != -100:
    cont=cont+1
    a=input("ingrese numero :")

print "numero de intentos :",cont




