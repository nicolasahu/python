# Permita pedir n nombres. Al final del ingreso muestre la
#suma de  caracteres de todos los nombres ingresados (con espacios)
limite=input("ingresar cantidad de nombres :")
cont=0
suma=0
while cont<limite:
    a=raw_input("ingrese nombre :")
    suma =suma + len (a)
    cont =cont + 1

print "los caracteres totales son :" , suma
