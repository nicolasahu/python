# -*- coding: cp1252 -*-
#Permita  ingresar  n�meros  hasta  que  el  usuario  digite  el
#n�mero  de  la  suerte  (7).  El programa  debe  dar  pistas.
# Por  ejemplo,  si  el  usuario  ingresa  un  n�mero  mayor  a  7, 
#debe decir, �B�jate un poquito�. Si el usuario ingreso un n�mero
#menor a 7 debe decir �Sube un poquito�. Si el usuario ingresa
#el n�mero de la suerte (7), enviar un mensaje de felicidades.

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
