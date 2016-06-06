#Pedir un nombre completo y mostrar la cantidad de vocales que tiene

nombre=raw_input("ingresar nombre completo :")

cont=0
for letra in nombre:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        cont=cont+1

print "cantidades de vocales :",cont
print letra

