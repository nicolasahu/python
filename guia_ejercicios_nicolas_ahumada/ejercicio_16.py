#Permita ingresar una cierta cantidad de notas (n). Al momento
#de ingresar todas las notas mostrar el promedio de rojos y
#el promedio de azules


limite=input("ingrese numero de notas :")
nota =0
cont=0
notaazul = 0
notaroja = 0
contalta=0
contbaja=0

while cont < limite:
    a=input ("ingrese nota :")
    if a>4:
        notaazul= notaazul + a
        contalta= contalta + 1

    else :
        notaroja = notaroja + a
        contbaja = contbaja + 1
        
    

    cont=cont+1
promediorojos=notaroja/contbaja
promedioazules=notaazul/contalta

print "promedio notas azules : ",promedioazules
print "promedio notas rojas : ", promediorojos
            






