# -*- coding: cp1252 -*-
#  Hacer el mismo ejercicio anterior añadiendo un contador que
#muestre la cantidad de veces que el usuario  intentó adivinar el número.
#La cantidad de veces de intento se 
#debe mostrar en el momento que el usuario adivino el número de la suerte. 

n=input("ingrese numero :")
cont=0
while n != 7:
    if n > 7:
        print"bajate un poquito"
        print "------------------"
    elif n<7:
        print "sube un poquito"
        print "------------------"
    cont=cont+1
    
    n=input("ingrese numero :")


print "numero de intentos",cont
print "felicitaciones"
