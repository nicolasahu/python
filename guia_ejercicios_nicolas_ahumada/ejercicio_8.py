# -*- coding: cp1252 -*-
#Permita estar ingresando n�meros hasta que el usuario ingrese -100.
#En ese momento, mostrar la cantidad de n�meros ingresados

a=input("ingrese numero :")
cont=0
while a != -100:
    cont=cont+1
    a=input("ingrese numero :")

print "numero de intentos :",cont




