#ejercicio 4condicional if


correo = raw_input("correo :")
clave = raw_input("clave :")

if correo == "nicolas_ahumada@live.cl":
    if clave == "123456789":
        print "bienvenido"
    else :
        print "error en la clave"

else:
    print "error en el correo"
    
