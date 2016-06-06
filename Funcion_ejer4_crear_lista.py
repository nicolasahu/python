
lista=[]
def lista_funcion():
	r1=True
	while r1==True:
		a=raw_input("Ingrese cantidad de palabras: ")
		z=a.isdigit()
		if z==False:
			print "Ingrese numeros, no letras..."
		else:
			a=int(a)
			r1=False
	for i in range(a):
		j=i+1
		r2=True
		while r2==True:
			b=raw_input("Ingrese palabra %d: " %j)
			z=b.isdigit()
			if z==True:
				print "Debe contener solo letras..."
			else:
				r2=False
		lista.append(b)
	return lista

lista1=lista_funcion()
print "\n\nla lista creada es: \n", lista1
