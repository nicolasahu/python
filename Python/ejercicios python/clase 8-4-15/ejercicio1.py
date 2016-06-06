#pedir por pantalla 3 edades e identificar
#cuantas personas son mayor o menor de edad

e1=input("primera edad :")
e2=input("segunda edad :")
e3=input("tercer edad :")

contmene=0#contador para las edades menor a 18
contmaye=0#contador para las edades mayores de 18

if e1 >= 18:
    # mayor de edad
    contmaye=contmaye+1
else:
    #menor de edad
    contmene=contmene+1

if e2 >= 18:
    # mayor de edad
    contmaye=contmaye+1
else:
    #menor de edad
    contmene=contmene+1

if e3 >= 18:
    # mayor de edad
    contmaye=contmaye+1
else:
    #menor de edad
    contmene=contmene+1

print "cantidad menores :",contmene
print ""
print "contidad de mayores :",contmaye
