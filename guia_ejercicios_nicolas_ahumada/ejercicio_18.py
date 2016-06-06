#Permita  ingresar  n  notas.  Al  momento  de  ingresar  todas
#las  notas  debe  mostrar  la 
#cantidad de rojos y la cantidad de azules.

limite=input("ingrese numero de notas :")
nota =0
cont=0
notaazul = 0
notaroja = 0
contalta=0
contbaja=0

while cont < limite:
    a=input ("ingrese nota :")
    if a>4:
        
        contalta= contalta + 1

    else :
        
        contbaja = contbaja + 1
        
    

    cont=cont+1


print "numero de notas azules : ",contalta
print "numero de notas rojas : ", contbaja
            
