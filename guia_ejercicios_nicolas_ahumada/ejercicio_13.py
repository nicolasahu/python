# -*- coding: cp1252 -*-
#Permita  ingresar  notas.  El  programa  debe  estar  pidiendo
#notas  hasta  que  ingrese  la 
#nota -800. Decir cuántos sietes y cuántos unos hay
print"ingrese nota con decimal"
a=input("ingrese nota:")
cont=0
siete=0
uno=0
while a!= -800:
    cont=cont+1
    if a==7:
        siete=siete+1

    elif a==1:
        uno=uno+1
    a=input("ingrese nota :")

print "numero de notas 7 es :",siete

print "numero de notas 1 es :",uno
    

