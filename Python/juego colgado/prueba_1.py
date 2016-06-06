import os
os.system("cls")


ciclo=True
letras = ""
prueba=""
juego=""
juego1=""
while ciclo:
    while ciclo:
        palabra=raw_input("ingrese palabra :")
        os.system("cls")
        for letra in palabra:
            if letra != " ":
                letras =letras+"_"+" "
                prueba=prueba+letra
            else:
                letras = letras+"   "
                prueba=prueba+letra
        while ciclo:
            
            print "         ",letras
            print""
            print""
            a=raw_input("            ingrese letra :")
            os.system("cls")           
            while ciclo :
                letras=""
                
                
                    
                for letra in palabra:
                    if letra ==a:
                        letras=letra.replace("_",letra)
                    else:
                        letras+="_"
                           
                         
                        print "                      ",letras
                        print" ----------- "
                        print"   |        | "
                        print"            | "
                        print"            | "
                        print"            | "
                        print"            | "
                        print"            | "
                        print"   -----------"
                        a=raw_input("            ingrese letra :")
                        os.system("cls")
            
                
                                   
                        print"              ",letras
                        print" ----------- "
                        print"   |        | "
                        print"   0       | "
                        print"            | "
                        print"            | "
                        print"            | "
                        print"            | "
                        print"   -----------"
                        print" le quedan 5 intentos"
                        a=raw_input("            ingrese letra :")
                        os.system("cls")
                       
            
            

                
                
                    
                    
            
    print "desea salir"
    print "1.- si"
    print "2.- no"
    salir=input("salir :")
    if salir !=1:
        
        letras =""

    else :
        ciclo=False


print "gracias por jugar el colgado"

            
