#Permita  ingresar  n  notas.  Al  momento  de  ingresar  todas
#las  notas  mostrar  el porcentaje de rojos y el porcentaje de azules

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
        notaazul= notaazul + a
        contalta= contalta + 1

    else :
        notaroja = notaroja + a
        contbaja = contbaja + 1
        
    

    cont=cont+1

sumacont=contalta+contbaja

porcentajeazul=(contalta*100/(sumacont))
porcentajerojo=(contbaja*100/(sumacont))
print "porcentaje notas azules : ",porcentajeazul
print "porcentaje notas rojas : ", porcentajerojo
            
