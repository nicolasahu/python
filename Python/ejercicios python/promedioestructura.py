print "programa para sacar promedio en  estructura de programacion"
print "notas catedra"
n1=input("inrese nota 1 :")
n2=input ("ingrese nota 2 :")
n3=input("ingrese nota 3:")
n4=input("ingrese nota 4 :")
nota1=n1*0.15
nota2=n2*0.20
nota3=n3*0.25
nota4=n4*0.45
promedio=nota1+nota2+nota3+nota4
print "-----------------------------------"
print "promedio catedra",promedio
print "-----------------------------------"
print "nota practica"
p1=input ("ingrese nota 1 :")
p2=input("ingrese nota 2 :")
p3=input("ingrese nota 3 :")
notap1=p1*0.25
notap2=p2*0.25
notap3=p3*0.50
sumapr=notap1+notap2+notap3
print "-----------------------------------"

print "nota practica :",sumapr
print "-----------------------------------"
print "-----------------------------------"
p1=promedio*0.7
p2=sumapr*0.3
sumatotal=p1+p2
print "nota final :",sumatotal
