#  La ANFP  necesita un sistema para poder registrar la venta de entradas de
#la final de la copa. El sistema debe estar pidiendo el precio de entradas
#hasta que el usuario ingrese un valor  -1. Al final de ingreso se debe
#mostrar el monto de entradas recaudado  (La suma total).

venta=input("ingrese veta :")
suma=0
while venta != -1 :
    suma=suma +venta

    venta=input("ingrese veta :")


print "monto de entradas recaudadas :",suma
