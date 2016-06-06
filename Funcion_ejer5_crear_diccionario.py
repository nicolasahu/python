
def diccionario():
	dic={}
	j=0
	a=input("Ingrese cantidad de datos: ")
	for i in range(a):
		j=i+1
		z=raw_input("Ingrese clave %d: " %j)
		x=raw_input("Ingrese valor %d: " %j)
		dic[z]=x
	return dic
r=True
while r==True:
	dicci=diccionario()
	print "\n\nEl diccionario quedo asi: \n", dicci
	resp=raw_input("Desea continuar ingresando (s/n)?: ")
	resp=resp.upper()
	if resp=='N':
		r=False
