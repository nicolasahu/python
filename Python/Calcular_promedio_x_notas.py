import os
def clear():
		if os.name == "posix":
			os.system ("clear")
		elif os.name == ("ce", "nt", "dos"):
			os.system ("cls")

suma=0
r=False
while r==False:
	cant=raw_input("Ingrese cantidad de notas: ")
	r=cant.isdigit()
	if r==False:
		print "Solo puede ingresar numeros..."
	else:
		cant=int(cant)
		r=True
clear()
for i in range(1, cant+1):
	nota=float(input("Ingrese nota %d: " %i))
	suma+=nota
prom=suma/cant
clear()
print "El promedio es: %1.1f" %prom
