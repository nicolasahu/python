"""ingrese x notas de un alumno y calcule su promedio
(valide, las notas si estan fuera del rango las vuelve a pedir)"""

limite=input("ingrese n notas :")
cont=0
ciclo = True
suma=0
while cont < limite :
    nota=input("ingese nota :")
    while nota < 1 or nota >7:
        if nota >7 or nota <1:
            print"ingrese nota valida"
            nota=input("ingrese nota :")

        else:
            ciclo = False

    suma=suma+nota
    cont+=1

promedio=suma/limite
print "el promedio es :",promedio 
