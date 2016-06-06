# -*- coding: cp1252 -*-
# Realice el ejercicio anterior  pero esta vez pida nombres hasta que
#el usuario ingrese el nombre  “terminar”.  Por  cada  nombre
#ingresado  debe  mostrar  la  información requerida
#(cantidad  de  caracteres  que  tiene  sin  espacios,  cantidad  de
#espacios  que tiene, cantidad de vocales que tiene,
#cantidad de consonantes que tiene)

a =raw_input("ingrese nombre :")

while a!= "terminar" :
    

    frase=a.replace(" ","")

    for letrs in a:
        b=a.replace ("a","")
        c=b.replace ("b","")
        d=c.replace("c","")
        e=d.replace("d","")
        f=e.replace("e","")
        g=f.replace("f","")
        h=g.replace("g","")
        i=h.replace("h","")
        j=i.replace("i","")
        k=j.replace("j","")
        l=k.replace("k","")
        m=l.replace("l","")
        n=m.replace("m","")
        o=n.replace("n","")
        p=o.replace("o","")
        q=p.replace("p","")
        r=q.replace("q","")
        s=r.replace("r","")
        t=s.replace("s","")
        u=t.replace("t","")
        v=u.replace("u","")
        w=v.replace("v","")
        x=w.replace("w","")
        y=x.replace("x","")
        z=y.replace("y","")
        aa=z.replace("z","")

    contb=0
    for letra in a:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            contb=contb+1
    conta=0
    for letra in a :
        b=a.replace("a","")
        c=b.replace("e","")
        d=c.replace("i","")
        e=d.replace("o","")
        n=e.replace("u","")
        f=n.replace(" ","")
        conta = conta +1


    print "numero de caracteres sin espacion",len(frase)
    print "numero de espacios", len (aa)
    print "cantidades de vocales :",contb
    print "cantidad de consonantes", len (f)
    a=raw_input("ingrese nombre :")


print "termino"


