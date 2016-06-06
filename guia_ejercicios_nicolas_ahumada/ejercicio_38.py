# -*- coding: cp1252 -*-
#Realizar el mismo ejercicio anterior pero con la opción 5.- Salir. El programa debe estar 
#pidiendo  2  números  y  mostrando  el  resultado  de  la  operación  escogida  mientras  la 
#opción digitada sea distinta de salir (opción 5)



ciclo=True
a=1
b=2
c=3
d=4
e=5
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
            
    elif v==2 :
        resta=n1-n2
        print "resultado de la resta es :",resta
            
    elif v==3 :
        dividir=n1/n2
        print"resultado de la dividir es :",dividir
           
    elif v==4 :
        multiplicar=n1*n2
        print "resultado de la multiplicacion es :",multiplicar
           
    if v == 5:
        ciclo=False

   
