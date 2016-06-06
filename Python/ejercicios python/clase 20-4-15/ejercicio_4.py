#permita el ingreso de venta de una farmacia. el programa debe
#permitir el ingreso de n productos. almomento de 
#igresarlos datos, muestre el total de venta y el promedio


limite=input("ingrese numero de ventas :")
cont=0
suma=0


while cont<limite:
    venta=input("ingrese valor :")
    suma = suma + venta
    
    cont = cont + 1

 promedio = suma/limite
print "total de ventas",suma
print "total de promedio",  promedio
