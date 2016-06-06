# -*- coding: cp1252 -*-
# Ingrese n nombres de trabajadores con su sueldo.
#Imprima el nombre del trabajador con el sueldo más alto.

limite=input("ingrese numero de trabajadores  :")
cont=0
sueldoalto=0
sueldobajo=0
nombrealto=0
nombrebajo=0
while cont<limite:
    b=raw_input("ingrese nombre :")
    
            
    a=input("ingrese sueldo :")

    if cont ==0:
        sueldoalto = a
        sueldobajo = a
    else:
        if(sueldoalto < a):
            sueldoalto = a
        if(sueldobajo > a):
            sueldobajo = a

    

    if a >= sueldoalto :
        nombrealto =  b
    elif a <= sueldobajo: 
        nombrebajo=b
    

    
    
    cont =cont+1
    





print "nombre del trabajador con mayor sueldo"
print "nombre trabajador :",nombrealto
print "suelto trabajador :",sueldoalto
    
    
