limite=input("ingrese n trabajadores :")
cont=0
sueldoalto=0
sueldobajo=0

while cont< limite :
    sueldo=input("ingrese sueldo :")
    afp=sueldo*0.13
    salud=sueldo*0.07
    liquido=sueldo-afp-salud
    if cont==0:
        sueldoalto=liquido
        sueldobajo=liquido
    else:
        if liquido >sueldoalto:
            sueldoalto=liquido

        elif liquido <sueldobajo:
            sueldobajo=liquido
    cont+=1


print "el sueldo mas alto es :",sueldoalto
