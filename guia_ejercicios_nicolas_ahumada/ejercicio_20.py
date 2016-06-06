#Permita  ingresar  una  palabra  y  muestre  sus  letras,  una  a
#una  hacia  abajo,  con  una pausa de 1 segundo
from time  import sleep
a=raw_input("ingrese palabra :")

for letra in a:
        
    print letra
    sleep(1)


