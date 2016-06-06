
def hola(mensaje,cantidad):
    cont=0
    limite=cantidad
    while cont<limite:
        print mensaje
        cont=cont+1


    




    
def final():
    n=input("ingrese cuatas veses  de repiticion de (hola) :")
    v=input("ingrese cuatas veses  de repiticion de (chao) :")
    
    hola("hola",n)
    hola("chao",v)
    suma=n+v**9
    hola("seba",suma)

    


final()


