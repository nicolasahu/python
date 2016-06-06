# -*- coding: cp1252 -*-
#Permita el ingreso de n números. Al final muestre el promedio de ellos

limite=input("ingrese numero para sacar promedio :")
cont=0
suma=0
while cont< limite:
    a=input("ingrese numero :")
    cont = cont + 1
    suma = suma + a

promedio=suma/limite

print "el promedio de los numeros son :",promedio
