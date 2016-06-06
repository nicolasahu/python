#pida n npersonas , a cada persona deve pedir (nombre,edad y n notas ),las notas ingresadas
#por alumno deven ser promediadas y ver cuantos rojos y azules,
#mostrar promedio cuantos rojos y cuantos azules

limite=input("inrese n alumnos :")
cont =0
curso=0
while cont<limite:
    nombre=raw_input("ingrese nombre :")
    edad=input("ingrese edad :")
    notas=input("ingrese n notas :")
    contnota=0
    suma=0
    azul=0
    rojos=0
    
    while contnota<notas:
        nota=input ("ingrese nota :")
        suma=suma+nota
        if nota>= 4:
            azul+=1
        else :
            rojos+=1
        contnota=contnota +1


    promedio=suma/notas
    curso+=promedio
    cont+=1
    print "nombre :",nombre
    print "edad :",edad
    print "promedio :",promedio
    print "numero de notas rojas :",rojos
    print "numero de notas azules :",azul


total=curso/limite
print "promedio curso :",total

