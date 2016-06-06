# -*- coding: cp1252 -*-
#Permita pedir nombres hasta que el usuario ingrese el nombre “terminar”.
#Al final del ingreso muestre la suma de caracteres de todos los
#nombres ingresados (sin espacios), 
#y la cantidad de nombres ingresado

a=raw_input("ingrese nombre :")
cont = 0
suma=0
while a != "terminar" :
    for letra in a :
        letra=a.replace(" ","")
    suma = suma + len (letra)
    cont = cont + 1

    a=raw_input("ingrese nombre :")
    
print "caracteres totales :",suma
print "cantidad de nombres ingresados :",cont
