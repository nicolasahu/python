#Ingrese precios hasta que el precio sea -1. Al final mostrar el promedio
#de precios.

precio=input("ingrese precio :")
cont=0
suma=0
while precio != -1 :
    suma = suma+ precio
    cont = cont +1
    precio=input("ingrese precio :")

promedio=suma/cont

print "promedio de los precios",promedio
    
