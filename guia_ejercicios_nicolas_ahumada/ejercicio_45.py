# -*- coding: cp1252 -*-
#Realizar el ejercicio anterior a�adiendo  lo siguiente. Al momento de
#adivinar, adem�s de mostrar el n�mero de intentos,
#preguntar si desea seguir participando, a lo que el 
#usuario puede escoger 1.-  Si, 2.-  No.
#El programa debe estar ejecut�ndose mientras la 
#respuesta sea si (opci�n 1). Adem�s el n�mero m�gico
#se debe generar aleatoriamente 
#(Investigar c�mo generar un n�mero random en python)


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
    
    


