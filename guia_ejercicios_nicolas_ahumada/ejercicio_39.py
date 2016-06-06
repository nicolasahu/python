# -*- coding: cp1252 -*-
#Realizar  el  mismo  ejercicio  anterior  pero  añadiendo  un  contador
#por  operación (contSuma,  contResta,  contMult,  contDivi).
#Cuando  el  usuario  quiera  salir  del 
#programa,  mostrar  la  cantidad  de  operaciones  por  operando.
#(Cantidad  de  sumas, cantidad de restas… etc.)

ciclo=True
a=1
b=2
c=3
d=4
e=5
contsuma=0
contresta=0
contmult=0
contdivi=0
while  ciclo:
    n1=input("ingresar numero 1 :")
    n2=input("ingresar numero 2 :")
    print "1.- suma"
    print "2.- resta"
    print "3.- dividir"
    print "4.- multiplicar"
    print "5.- salir"
    v=input("ingrese la opcion :")
    
    if v == 1 :
        suma=n1+n2
        print "resultado de la suma es :",suma
        contsuma = contsuma + 1   
    elif v==2 :
        resta=n1-n2
        print "resultado de la resta es :",resta
        contresta=contresta +1    
    elif v==3 :
        dividir=n1/n2
        print"resultado de la dividir es :",dividir
        contdivi=contdivi+1   
    elif v==4 :
        multiplicar=n1*n2
        print "resultado de la multiplicacion es :",multiplicar
        contmult=contmult+1   
    if v == 5:
        ciclo=False

print "cantidad de sumas :",contsuma
print "cantidad de restas :",contresta
print "cantidad de multiplicar :",contmult
print "cantidad de division :",contdivi
