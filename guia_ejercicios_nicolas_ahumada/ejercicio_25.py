#Pedir un nombre completo y mostrar la cantidad de consonantes que tiene.

nombre=raw_input("ingrese nombre :")
cont =0
for letra in nombre :
    b=nombre.replace("a","")
    c=b.replace("e","")
    d=c.replace("i","")
    e=d.replace("o","")
    n=e.replace("u","")
    f=n.replace(" ","")
    cont = cont +1
print len (f)

