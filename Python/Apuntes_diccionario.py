diccionario={1:"enero", 2:"Febrero", 3:"Marzo"}
diccionario[1]="Abril"
print diccionario[1]

#Ver si se encuentra un valor en el diccionario
print "\nBuscando clave 1..."
print diccionario.has_key(1)

print "\nBuscando clave 3..."
print 3 in diccionario

#Buscando el valor de la clave
print "\nBuscando valor de la clave 5 en diccionario..."
print diccionario.get(5, "No se encontro el valor")

#Mostrando el diccionario en tuplas...
print "\nEl diccionario contiene (tuplas)..."
print diccionario.items()

#Devuelve una lista con las claves
print "\nEl diccionario contiene las siguientes claves."
print diccionario.keys()

#Devuelve una lista con los valores del diccionario
print "\nEl diccionario contiene los siguientes valores."
print diccionario.values()

#Borra la clave e imprime su valor (pop)
print "\nBorrando la clave 2..."
print diccionario.pop(2)
print "\nAhora el diccionario contiene: "
print diccionario
print "\nBorrando clave 4..."
print diccionario.pop(4, "No se encontro esta clave")

#Borrando la clave con del
print "\nBorrando clave 1..."
del diccionario[1]
print "\nAhora contiene: "
print diccionario

#Limpiando el diccionario
print "\nLimpiando diccionario..."
diccionario.clear()
print "Ahora el diccionario esta vacio...\n", diccionario

#Llenar el diccionario...
print "\nAhora llenaremos nuevamente el diccionario."
k=raw_input("Ingrese la clave: ")
v=raw_input("Ingrese el valor: ")
diccionario[k]=v
print "\nAhora el diccionario contiene lo siguiente: \n", diccionario
