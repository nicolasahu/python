#Ingrese n sueldos. Muestre el menor de ellos
limite=input("ingrese limite de sueldo :")
cont=0
sueldoalto=0
sueldobajo=0

while cont<limite:
    a=input("ingrese sueldo")
    if cont ==0:
        sueldoalto = a
        sueldobajo = a
    else:
        if(sueldoalto < a):
            sueldoalto = a
        if(sueldobajo > a):
            sueldobajo = a

    cont =cont+1

print "el sueldo menor es :",sueldobajo
    
