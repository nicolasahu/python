#Permita pedir una frase. Muestre la misma frase pero
#que reemplace todas las letras a 
#por 4, las letras e por 3, las letras i por 1,
#las letras o por 0 y las letras u por v

frase=raw_input("ingrese una frase")

for letra in frase  :
    a=frase.replace("a","4")
    b=a.replace("e","3")
    c=b.replace ("i","1")
    d=c.replace("o","0")
    e=d.replace("u","v")

print "la frase es :",e
