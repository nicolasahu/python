tupla=("lista","metallica","outlast","python","geany")
print "mostrar palabras  de la tupla"
print tupla
print "-------------------"
print tupla [3]
print "-------------------"
print tupla [-1]
print "-------------------"
print tupla [1:4]
print "-------------------"
ciclo=True
while ciclo:
    
    t=input("ingrese numero para ver si existe en la  tupla :")
    if t==-100:
        ciclo=False
    elif t !=-100:
        print tupla [t]
        print "-------------------"
    else:
        print"la palabra no esta"
print "-------------------"
print"se pueden juntar tuplas"
print "EJEMPLO :"
d=("luis","alvaro")
print tupla
print d
print "-------------------"
print tupla+d
