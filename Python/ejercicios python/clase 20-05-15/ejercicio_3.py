#funciones con parametros
def ciclo(mensaje,vueltas):
	cont=0
	while cont<vueltas:
		print mensaje	
		cont+=1
def pedirdatos():
	v=input("ingrese vueltas :")
	m=raw_input("ingrese mensaje  :")
	
	ciclo(m,v)
def main():
	pedirdatos()
	
print main()
	
