#Ingrese n sueldos. Muestre el mayor de ello
limite=input("ingrese limite de sueldo :")
cont=0
sueldoalto=0
sueldobajo=0

while cont<limite:
    a=input("ingrese sueldo")
    if cont ==0:
        sueldoalto = a
        sueldobaja = a
    else:
        if(sueldoalto < a):
            sueldoalto = a
        if(sueldobajo > a):
            sueldobajo = a

    cont =cont+1

print "el sueldo mayor es :",sueldoalto
