# -*- coding: cp1252 -*-
#Permita estar ingresando números hasta que el usuario ingrese  -1.
#En ese momento, mostrar la suma y promedio.


a=input("ingrese numero :")
cont=0
suma=0
while a!=-1:
    
    cont=cont+1
    suma=suma+a
    a=input("ingrese numero :")
promedio=suma/cont
print "el resutado de la suma :",suma
print "el promedio es :",promedio
    


