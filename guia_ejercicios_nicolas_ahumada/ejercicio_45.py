# -*- coding: cp1252 -*-
#Realizar el ejercicio anterior añadiendo  lo siguiente. Al momento de
#adivinar, además de mostrar el número de intentos,
#preguntar si desea seguir participando, a lo que el 
#usuario puede escoger 1.-  Si, 2.-  No.
#El programa debe estar ejecutándose mientras la 
#respuesta sea si (opción 1). Además el número mágico
#se debe generar aleatoriamente 
#(Investigar cómo generar un número random en python)


cont=0
import random
cpu = random.choice(range(10))
ciclo=True
while ciclo:
    n=input("ingrese numero :")
    if n != cpu:   
        if n > cpu:
            print"bajate un poquito"
            print "------------------"
            
        elif n<cpu:
            print "sube un poquito"
            print "------------------"
        
    if n != cpu:
        print "1- si"
        print "2- no"
        p=input ("quiere salir :")
        if p == 1 : 
            ciclo=False 
    if ciclo==False:
        ciclo=False
    
    cont=cont+1    
print "numero de intentos",cont
print "felicitaciones"
    
    


