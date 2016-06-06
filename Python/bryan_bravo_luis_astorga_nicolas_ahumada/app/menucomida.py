import os
os.system("cls")
global listamenu
listamenu=list()
class men:
	nombre=""
	precio=0
	codigo=""
	

def Registroalimentos ():
	
	m1=men()
	m2=men()
	m3=men()
	m4=men()
	m5=men()
	m6=men()
	m7=men()
	m8=men()
	m9=men()
	m10=men()
	m11=men()
	m12=men()
	m13=men()
	m14=men()
	m15=men()
	m1.nombre="te"
	m1.precio=400
	m1.codigo="001"
	m2.nombre="cafe"
	m2.precio=400
	m2.codigo="002"
	m3.nombre="milo"
	m3.precio=400
	m3.codigo="003"
	m4.nombre="leche"
	m4.precio=400
	m4.codigo="004"
	m5.nombre="sandiwch lomo"
	m5.precio=1300
	m5.codigo="005"
	m6.nombre="sandiwch potito"
	m6.precio=1300
	m6.codigo="006"
	m7.nombre="sandiwch churrasco"
	m7.precio=1500
	m7.codigo="007"
	m8.nombre="sandiwch de pernil"
	m8.precio=1250
	m8.codigo="008"
	m9.nombre="sandiwch de pollo"
	m9.precio=1250
	m9.codigo="009"
	m10.nombre="bebida express"
	m10.precio=450
	m10.codigo="010"
	m11.nombre="empanada de pino"
	m11.precio=800
	m11.codigo="011"
	m12.nombre="empanada de queso"
	m12.precio=750
	m12.codigo="012"
	m13.nombre="empanada de poll y queso"
	m13.precio=850
	m13.codigo="013"
	m14.nombre="aliados (lomo y potito)"
	m14.precio=1800
	m14.codigo="014"
	m15.nombre="aliados (queso y jamon)"
	m15.precio=600
	m15.codigo="015"
	listamenu.append(m1)
	listamenu.append(m2)
	listamenu.append(m3)
	listamenu.append(m4)
	listamenu.append(m5)
	listamenu.append(m6)
	listamenu.append(m7)
	listamenu.append(m8)
	listamenu.append(m9)
	listamenu.append(m10)
	listamenu.append(m11)
	listamenu.append(m12)	
	listamenu.append(m13)
	listamenu.append(m14)
	listamenu.append(m15)

	

Registroalimentos ()
def listacomida():
	cont=1
	print "----lista de comidas-----"
	for m in listamenu:
		print "----comida numero ",cont,"-----"
		print "nombre :",m.nombre
		print "precio :",m.precio
		print "codigo :",m.codigo
		print "--------------------" 
		cont+=1
	a=raw_input("precione enter : ")
	os.system("cls")

