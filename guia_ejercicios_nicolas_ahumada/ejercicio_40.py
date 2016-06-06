#Permitir el ingreso de un monto y desplegar su detalle.
#Ej:   Ingrese un monto: 20772
#Detalle:
#1 de $20000
#0 de $10000
#0 de $5000
#0 de $1000
#1 de $500
#2 de $100
#1 de $50
#2 de $10
#2 de $1

a=input( "ingresar monto :")
veintemil=0
diezmil=0
cincomil=0
mil=0
quinientos=0
cien=0
cincuenta=0
diez=0
uno=0
b=0
while a!=0:
    if a >=20000 :
    
        veintemil=veintemil + 1
        a=a-20000

    elif a>=10000:
        diezmil=diezmil+1
        a=a-10000

    elif a>=5000:
        cincomil=cincomil+1
        a=a-5000

    elif a>=1000:
        mil=mil+1
        a=a-1000

    elif a>=500:
        quinientos =quinientos+1
        a=a-500

    elif a>=100:
        cien=cien +1
        a=a-100

    elif a>=50:
        cincuenta=cincuenta+1
        a=a-50

    elif a>=10:
        diez=diez+1
    
        a=a-10

    else:
        uno=uno+1
        a=a-1

print "el resultado es "
print "20.000 :",veintemil
print "10.000 :",diezmil
print "5.000 :",cincomil
print "1.000 :",mil
print "500 :",quinientos
print "100 :",cien
print "50 : ",cincuenta
print "10 :",diez
print "1 :",uno

