# -*- coding: cp1252 -*-
#Permita ingresar edades. El programa debe estar pidiendo edades hasta
#que ingrese la edad  -100.  Decir  cuántas  personas  son
#de  la  tercera  edad  (mayor  a  50)  y  cuantas 
#edades se ingresaron


a=input("ingrese edad :")
cont=0
mayores=0
menores =0

while a!=-100:
    cont=cont+1

    if a>50:
        mayores = mayores +1

    else :
        menores = menores+1


    a=input("ingrese edad :")
print "numero de edades mayor a 50 son :",mayores
print "numero de edades ingresadas son :",cont
