# -*- coding: cp1252 -*-
#Permita  ingresar  notas.  El  programa  debe  estar  pidiendo
#notas  hasta  que  ingrese  la 
#nota -1. Decir cuántas notas azules hay, cuantas rojas

print "ingresar notas con decimal"
a=input("ingrese nota :")
rojos = 0
azules =0
cont=0
while a != -1:
    cont=cont+1
    if a>= 4:
        azules=azules+1

    else :
        rojos=rojos+1




    a=input("ingrese nota :")


print "el resultado de los rojos son :",rojos
print "el resultado de los azules son :",azules

    
        
