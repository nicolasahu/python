tupla=("from","print","else","del","while","if","elif")
print"este ejercicion muestra si una palabra esta en la lista tupla"
print tupla
print "---------------------" 
print "else"
print "else" in tupla
print "---------------------" 

print "python"
print "python" in tupla
print "---------------------" 
ciclo=True
while ciclo:
    a=raw_input("ingrese palabra para verificar si esta en la lista :")
    if a =="salir":
        ciclo = False
    else :
        print a in tupla
        print "---------------------"
    
