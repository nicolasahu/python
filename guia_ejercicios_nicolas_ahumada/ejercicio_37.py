# -*- coding: cp1252 -*-
#Realizar una calculadora. La calculadora debe pedir
#dos números y mostrar el siguiente 
#menú:
#1.- Sumar
#2.- Restar
#3.- Dividir
#4.- Multiplicar

n1=input("ingresar numero 1 :")
n2=input("ingresar numero 2 :")
ciclo=True
a=1
b=2
c=3
d=4

   
print "1.- suma"
print "2.- resta"
print "3.- dividir"
print "4.- multiplicar"
v=input("ingrese la opcion")
if v == 1 :
    suma=n1+n2
    print "resultado de la suma es :",suma

elif v==2 :
    resta=n1-n2
    print "resultado de la resta es :",
elif v==3 :
    dividir=n1/n2
    print"resultado de la dividir es :",dividir

elif v==4 :
    multiplicar=n1*n2
    print "resultado de la multiplicacion es :",multiplicar
        
    
