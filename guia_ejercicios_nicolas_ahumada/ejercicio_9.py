# -*- coding: cp1252 -*-
#Permita  estar  ingresando  números  hasta  que  el  usuario
#ingrese  -1000.  En  ese 
#momento, mostrar la cantidad de números igual a 100

a=input("ingrese numero :")
acumulador=0

while a!=-1000:
    if a == 100:
        acumulador=acumulador+1
    a=input("ingrese numero :")

    
print "la cantidad de numeros 100 es :",acumulador


        
    
    
