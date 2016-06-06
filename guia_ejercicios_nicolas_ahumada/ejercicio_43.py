# -*- coding: cp1252 -*-
#Permita  ingresar  números  hasta  que  el  usuario  digite  el
#número  de  la  suerte  (7).  El programa  debe  dar  pistas.
# Por  ejemplo,  si  el  usuario  ingresa  un  número  mayor  a  7, 
#debe decir, “Bájate un poquito”. Si el usuario ingreso un número
#menor a 7 debe decir “Sube un poquito”. Si el usuario ingresa
#el número de la suerte (7), enviar un mensaje de felicidades.

n=input("ingrese numero :")

while n != 7:
    if n > 7:
        print"bajate un poquito"
        print "------------------"
    elif n<7:
        print "sube un poquito"
        print "------------------"
    n=input("ingrese numero :")    
    
print "felicitaciones"
