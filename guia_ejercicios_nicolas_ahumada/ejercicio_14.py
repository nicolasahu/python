#Permita  ingresar  un  grupo  de  notas  (el  usuario  escoge).
#Al  final  sacar  el  promedio general del curso

limite=input("ingrese numero de notas :")
cont=0
suma=0

while cont< limite :
    a=input("ingrese nota :")

    cont=cont+1
    suma =suma+ a

promedio=suma/limite

print "promedio del curso :",promedio
    
