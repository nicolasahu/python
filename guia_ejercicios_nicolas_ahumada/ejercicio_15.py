# -*- coding: cp1252 -*-
#Permita ingresar un grupo de notas (el usuario escoge).
#Al final mostrar la nota más alta y la nota más baja
limite=input("ingrese numero de notas")
nota =0
cont=0
notaAlta = 0
notaBaja = 0


while cont < limite:
    a=input ("ingrese nota")
    if cont ==0:
        notaAlta = a
        notaBaja = a
    else:
        if(notaAlta < a):
            notaAlta = a
        if(notaBaja > a):
            notaBaja = a
    


    cont = cont + 1
print "La nota mas alta: ", notaAlta
print "La nota mas baja: ", notaBaja
            

        





