# Ingrese una frase. El programa debe permitir lo siguiente:
#Ingrese una frase: hola a todos
#Resultado: xxxx x xxxxx
a=raw_input("ingrese frase :")
cadena= ""
for letra in a:
    if letra != " ":
        cadena=cadena+"x"

    else:
        cadena=cadena+" "
print"resultado :",cadena
