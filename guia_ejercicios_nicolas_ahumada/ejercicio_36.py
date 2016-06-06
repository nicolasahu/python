# -*- coding: cp1252 -*-
#Desarrolle  un  programa  que  simule  estar  hablando  con  el
#computador.  Pida  datos personales (Nombre y edad) y pregunte por
#el estado de ánimo del usuario. Según su estado de ánimo, de consejos.
#El software debe estar pidiendo estos datos hasta que 
#el usuario ingrese como nombre “salir”. Al momento de salir,
#dar las gracias por utilizar su aplicación.

nombre=raw_input("ingrese nombre :")
ciclo=True
while nombre != "salir" :
    
    
    edad=input("ingrese edad :")
    estado=raw_input("cual es su estado de animo (bien,mal o mas o menos) :")
    
    if estado == "bien":
        print "siga con esa energia .",nombre

    elif estado == "mal":
        print "trata de relajarte de ves en cuando sale a dar una vuelta al aire libre"

    elif estado == "mas o menos":
        print "sube el animo no todo se viene abajo tan rapido siempre ahi una pequena esperansa de estar mejor"
    
    nombre=raw_input("ingrese nombre :")    
                
        
    


print "gracias por usar esta aplicaccion"
    
