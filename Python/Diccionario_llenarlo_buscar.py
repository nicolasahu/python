
d={}
r=False
while r==False:
	cant=raw_input("Ingrese cantidad de valores: ")
	r=cant.isdigit()
	if r==False:
		print "Ingrese numeros..."
	else:
		cant=int(cant)
		r=True

for i in range(1, cant+1):
	k=raw_input("Ingrese clave %d: " %i)
	v=raw_input("Ingrese valor %d: " %i)
	d[k]=v

print "El diccionario contiene: \n", d
r=False
while r==False:
	buscar=raw_input("\n\nQue desea buscar?: ")
	print d.get(buscar, "No se encuentra esta clave.")
	resp=raw_input("Desea continuar buscando?: ")
	resp=resp.lower()
	if resp=='n':
		break
