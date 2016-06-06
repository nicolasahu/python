# -*- coding: cp1252 -*-

global Listausu
Listausu=list()
global Listaplatos
Listaplatos=list()
global Listacompra
Listacompra=list()
class Usuario:
	usuario=""
	clave=""

class Plato:
	dia=""
	turno=""
	nombre=""
	ingrediente1=""
	ingresiente2=""
	ingresiente3=""
	ingresiente4=""
	ingresiente5=""
	precio=0
class Liscompra :
	nombre=""
	precio=0
	descuento=0
	
	
def Registrarusu():
	u=Usuario()
	u.usuario="admin"
	u.clave="admin"
	Listausu.append(u)

def Registrar_platos_dias_especiales():
	p1=Plato()
	p2=Plato()
	p3=Plato()
	p4=Plato()
	p5=Plato()
	p6=Plato()
	p7=Plato()
	p8=Plato()
	p9=Plato()
	p10=Plato()
	p11=Plato()
	p12=Plato()
	p13=Plato()
	p14=Plato()
	p15=Plato()
	p16=Plato()
	p17=Plato()
	p18=Plato()
	p19=Plato()
	p20=Plato()
	p21=Plato()
	
	
	
	p1.dia="lunes"
	p1.turno="desayuno"
	p1.nombre="te con huevos rancheros"
	p1.precio=2500
	p1.ingrediente1="1 jitomate"
	p1.ingrediente2="2 chiles gueros"
	p1.ingrediente3="1 diente de ajo"
	p1.ingrediente4="tortilla de maiz"
	p1.ingrediente5="6 huevos"
	
	p2.dia="lunes"
	p2.turno="almuerzo"
	p2.nombre="chile en nogada"
	p2.precio=3500
	p2.ingrediente1="6 chiles poblanos"
	p2.ingrediente2="2 tazas de leche entera"
	p2.ingrediente3="1 taza de queso crema "
	p2.ingrediente4="2 tomates romapicados en cuadritos"
	p2.ingrediente5="6 huevos grandes"
	
	p3.dia="lunes"
	p3.turno="cena"
	p3.nombre="fajitas de pollo al chipotle"
	p3.precio=3400
	p3.ingrediente1="1 o 2 cucharadas de aceite vegetal"
	p3.ingrediente2="1 kilo de fajitas de pechuga o muslo de pollo "
	p3.ingrediente3="1/8 cucharada de ajo en polvo "
	p3.ingrediente4="3 chiles chipotles adobado"
	p3.ingrediente5="250gramos de crema entera de leche "
	
	p4.dia="miercoles"
	p4.turno="desayuno"
	p4.nombre="chacarero chileno con te"
	p4.precio=2500
	p4.ingrediente1="1 sirloin steak"
	p4.ingrediente2="1 bolsa de porotos verdes"
	p4.ingrediente3="panes suaves redondos"
	p4.ingrediente4="tomate"
	p4.ingrediente5="te"
	
	p5.dia="miercoles"
	p5.turno="almuerzo"
	p5.nombre="porotos con riendas"
	p5.precio=450
	p5.ingrediente1="2 tazas de frijoles pinto"
	p5.ingrediente2="2 chorizos tipo españal rebanado"
	p5.ingrediente3="2 dientes de ajo"
	p5.ingrediente4="1/2 paquete de espaguetis"
	p5.ingrediente5="1 taza de calabaza naranja"
	
	p6.dia="miercoles"
	p6.turno="cena"
	p6.nombre="pastel de choclo"
	p6.precio=6500
	p6.ingrediente1="1 cebolla mediana picada"
	p6.ingrediente2="6 dientes de  ajos "
	p6.ingrediente3="carne molida"
	p6.ingrediente4="choclo"
	p6.ingrediente5="sal y pimienta"
	
	p7.dia="sabado"
	p7.turno="desayuno"
	p7.nombre="ceviche de camaro a la piedra"
	p7.precio=2500
	p7.ingrediente1="camaron"
	p7.ingrediente2="1 camote cocido"
	p7.ingrediente3="3 a 4 hojas de lechuga"
	p7.ingrediente4="sal y pimienta"
	p7.ingrediente5="1 taza de choclo"
	
	p8.dia="sabado"
	p8.turno="almuerzo"
	p8.nombre="aji de gallina"
	p8.precio=3200
	p8.ingrediente1="2 pechugas de pollo o gallina"
	p8.ingrediente2="1 cebolla picada"
	p8.ingrediente3="1 cucharada de pimienta y comino"
	p8.ingrediente4="5 cucharadas de aji mirasol molido "
	p8.ingrediente5="1/2kg papas sancochadas y cortadas por la mitad "
	
	p9.dia="sabado"
	p9.turno="cena"
	p9.nombre="lomo saltado"
	p9.precio=4500
	p9.ingrediente1="1 libra de lomo  de res "
	p9.ingrediente2="arroz blanco"
	p9.ingrediente3="2 tazas de papas fritas"
	p9.ingrediente4="1 aji amarillo"
	p9.ingrediente5="2 dientes de ajo"
	
	p10.dia="martes"
	p10.turno="desayuno"
	
	p11.dia="martes"
	p11.turno="almuerzo"
	
	p12.dia="martes"
	p12.turno="cena"
	
	p13.dia="jueves"
	p13.turno="desayuno"
	
	p14.dia="jueves"
	p14.turno="almuerzo"
	
	p15.dia="jueves"
	p15.turno="cena"
	
	p16.dia="viernes"
	p16.turno="desayuno"
	
	p17.dia="viernes"
	p17.turno="almuerzo"
	
	p18.dia="viernes"
	p18.turno="cena"
	
	p19.dia="domingo"
	p19.turno="desayuno"
	
	p20.dia="domingo"
	p20.turno="almuerzo"
	
	p21.dia="domingo"
	p21.turno="cena"
	
	Listaplatos.append(p1)
	Listaplatos.append(p2)
	Listaplatos.append(p3)
	Listaplatos.append(p4)
	Listaplatos.append(p5)
	Listaplatos.append(p6)
	Listaplatos.append(p7)
	Listaplatos.append(p8)
	Listaplatos.append(p9)
	Listaplatos.append(p10)
	Listaplatos.append(p11)
	Listaplatos.append(p12)
	Listaplatos.append(p13)
	Listaplatos.append(p14)
	Listaplatos.append(p15)
	Listaplatos.append(p16)
	Listaplatos.append(p17)
	Listaplatos.append(p18)
	Listaplatos.append(p19)
	Listaplatos.append(p20)
	Listaplatos.append(p21)

	

	
Registrar_platos_dias_especiales()	
#registrar platos
	
	
Registrarusu()
def Ingresocompra():
	ciclo=True
	descuento=0
	suma=0
	while ciclo:
		print "(lunes-martes-miercoles-jueves-viernes-sabado-domingo)"
		dia=raw_input("ingrese dia en palabra :")
		turno=raw_input("ingrese turno (desayuno-almuerzo-cena):" )
		l=Liscompra()
		for p in Listaplatos:
			if p.dia == dia:
				if p.dia=="lunes" and turno =="desayuno" or p.dia=="miercoles" and turno =="almuerzo" or p.dia=="sabado" and turno == "cena" or p.dia=="sabado" and turno == "almuerzo":
					if dia == "lunes" and turno == "desayuno":
						l.descuento=p.precio*0.1
						l.nombre=p.nombre
						l.precio=p.precio
					elif dia == "miercoles" and turno == "almuerzo" :
						l.descuento=p.precio*0.2
						l.nombre=p.nombre
						l.precio=p.precio
					elif dia == "sabado" and turno =="cena" or dia =="sabado" and turno == "almuerzo"  :
						l.descuento=p.precio*015
						l.nombre=p.nombre
						l.precio=p.precio
				
				
				elif dia=="lunes" or dia == "martes"  or dia=="miercoles" or dia =="jueves" or dia =="viernes" or dia=="sabado" or dia =="domingo":
					if dia == "lunes" and turno == "almuerzo" or dia == "lunes" and turno == "cena":
						l.nombre=p.nombre
						l.precio=p.precio
						l.descuento=0
					elif dia == "martes" :
						l.nombre=p.nombre
						l.precio=p.precio
						l.descuento=0	
						
					elif dia == "miercoles" and turno == "desayuno" or dia == "miercoles" and turno == "cena" : 
						
						l.nombre=p.nombre
						l.precio=p.precio
						l.descuento=0
					elif dia == "jueves" :
						l.nombre=p.nombre
						l.precio=p.precio
						l.descuento=0
					elif dia == "viernes" :
						l.nombre=p.nombre
						l.precio=p.precio
						l.descuento=0
						
					elif dia == "sabado" and turno =="desayuno":
						
						l.nombre=p.nombre
						l.precio=p.precio
						l.descuento=0
					elif dia == "domingo" :
						l.nombre=p.nombre
						l.precio=p.precio
						l.descuento=0
						
		
				
		Listacompra.append(l)
		print "desea segir agregando"
		print "1.-si"
		print "2.-no"
		op=raw_input("")
		if op == "2":
			ciclo=False
	
def Vercompra():
	print "---lista compra---"
	for l in Listacompra:
		print "nombre :",l.nombre
		print "precio :",l.precio
		print "descuento :",l.descuento	
					
def Imprimircompra():
	print "imprimir compra"
	cont=0
	suma=0
	descuento=0
	for l in Listacompra:
		print "nombre :",l.nombre
		print "precio :",l.precio
		descuento+=l.descuento
		cont+=1
		suma+=l.precio
		print "---------------------"
		print ""
	
		
	total=suma-descuento
	print "-------------------"
	print "total :",total
	print "-------------------"
	Listacompra[:]=[]
							
					
		
	
			
def Principal():
	ciclo=True
	while ciclo :
		print ""
		print "----menu principal----"
		print ""
		print "1.-ingresar compra"
		print "2.-ver compra"
		print "3.-imprimir compra"
		print "4.-salir"
		op=raw_input("ingrese una  opcion :")
		if op == "1":
			Ingresocompra()
		elif op == "2":
			Vercompra()
		elif op == "3":
			Imprimircompra()
		elif op == "4":
			ciclo=False
		else :
			print "digito erronio"
			print ""	
		 		
def Validarusu(usu,clave):
	for u in Listausu:
		if u.usuario == usu and u.clave == clave:
			Principal()
			ciclo=True 
	

def Menuprincipal():
	cont=4
	ciclo=True
	while ciclo:
		print "ingrse usuario y clave"
		usu=raw_input("USUARIO :")
		clave=raw_input("clave :")
		for u in Listausu:
			if u.usuario == usu and u.clave == clave:
				Principal()
				ciclo=False 
		if cont==0 or ciclo ==False:

			ciclo=False
		elif cont != 0 :
			print "te quedan ",cont,"intentos"


def Cambio_clave():
	print "cambio de clave"
	print ""
	usu=raw_input("ingrese usuario :")
	clave=raw_input("ingrese clave actual :")
	newclave=raw_input("ingrese nueva clave :")
	for u in Listausu:
		if u.usuario == usu and u.clave ==clave:
			u.clave=newclave


def Crearusuario():
	admiusu=raw_input("ingrese usuario administrador :")
	admiclave=raw_input("ingrese clave administrador :")
	ciclo=False
	for u in Listausu:
		if u.usuario ==admiusu and u.clave == admiclave:
			ciclo=True
	if ciclo==True:
		print "ingrese datos nuevo usuario"
		u=Usuario()
		u.usuario=raw_input("ingrese usuario :")
		u.clave=raw_input("ingrese clave :")
		Listausu.append(u)
		print "usuario creado"
		print ""
		print "-----------------------"
		print ""
	else:
		print "usuario o clave erronia"

	
def Menulogin():
	ciclo=True
	while ciclo:
		print "----menu login----"
		print "1.-cambio de clave"
		print "2.-crear usuario"
		print "3.-salir"
		op=raw_input("ingrese opcion :")
		if op == "1":
			Cambio_clave()
		elif op == "2":
			Crearusuario()
		elif op == "3":
			ciclo=False
		else:
			print "dato ingresado erronio"

def Registro_plato_especificaciones(dia):
	if dia == "lunes" or dia == "miercoles" or dia == "sabado" :
		print "dia no puede alterarse"
	else :
		turno=raw_input("ingrese turno (desayuno-almuerzo-cena) :")
		for p in Listaplatos:
			if p.dia==dia and p.turno ==turno:
				print "ingrese datos de plato"
				nombre=raw_input("ingres nombre plato :")
				precio=input("ingrese precio ")
				ingredientea=raw_input("ingrese ingrediente 1 :")
				ingredienteb=raw_input("ingrese ingrediente 2 :")
				ingredientec=raw_input("ingrese ingrediente 3 :")
				ingrediented=raw_input("ingrese ingrediente 4 :")
				ingredientee=raw_input("ingrese ingrediente 5 :")
				p.nombre=nombre
				p.precio=precio
				p.ingrediente1=ingredientea
				p.ingrediente2=ingredienteb
				p.ingrediente3=ingredientec
				p.ingrediente4=ingrediented
				p.ingrediente5=ingredientee
				Listaplatos.append(p)
				
				
				
			
def Registroplato():
	print "---registro de plato---"
	print ""
	print ""
	op =raw_input("ingrese dia de la semana (1-7)")
	if op =="1":
		Registro_plato_especificaciones("martes")
	elif op == "2":
		Registro_plato_especificaciones("miercoles")
	elif op == "3":
		Registro_plato_especificaciones("jueves")
	elif op == "4":
		Registro_plato_especificaciones("viernes")
	elif OP == "5":
		Registro_plato_especificaciones("sabado")
	elif op == "6":
		Registro_plato_especificaciones("domingo")
	elif op == "7":
		Registro_plato_especificaciones("lunes")
	else:
		print "dato erronio"
		
def Verplato():
	dia=raw_input("ingrese dia en palabra :")
	turno=raw_input("ingrese turno (desayuno-almuerzo-cena):" )
	print ""
	print "lista platos"
	for p in Listaplatos:
		
		if p.dia==dia and p.turno == turno:
			
					
			print "dia :",p.dia
			print "turno :",p.turno
			print "nombre :",p.nombre
			print "precio :",p.precio
			print "ingrediente 1 :",p.ingrediente1
			print "ingrediente 2 :",p.ingrediente2 
			print "ingrediente 3 :",p.ingrediente3 
			print "ingrediente 4 :",p.ingrediente4 
			print "ingrediente 5 :",p.ingrediente5
			print "---------------------------------------------------"
		




def Menuadmin():
	print "ingrese usuario"
	usu=raw_input("ingrese usuario :")
	clave=raw_input("ingrese clave :")
	for u in Listausu:
		
		if u.usuario==usu and u.clave==clave:
			
			ciclo=True
			while ciclo:
				print "---menu administrador---"
				print ""
				print "1.-registrar platos"
				print "2.-ver platos por dia y turno"
				print "3.-salir"
				op =raw_input("ingrese opcion :")
				if op == "1":
					Registroplato()
				elif op =="2":
					Verplato()
				elif op =="3":
					ciclo=False
				else :
					print "digito erronio"

def Menureceta():
	print "ingrese usuario"
	usu=raw_input("ingrese usuario :")
	clave=raw_input("ingrese clave :")
	for u in Listausu:
		
		if u.usuario==usu and u.clave==clave:
			for p in Listaplatos:
				dia=raw_input("ingrese dia en palabra :")
				turno=raw_input("ingrese turno (desayuno-almuerzo-cena):" )
				print ""
				print "lista platos"
				if p.dia==dia and p.turno == turno:
					
					print "dia :",p.dia
					print "turno :",p.turno
					print "nombre :",p.nombre
					print "precio :",p.precio
					print "ingrediente 1 :",p.ingrediente1
					print "ingrediente 2 :",p.ingrediente2 
					print "ingrediente 3 :",p.ingrediente3 
					print "ingrediente 4 :",p.ingrediente4 
					print "ingrediente 5 :",p.ingrediente5
					print "---------------------------------------------------" 
				break		

def Rango(mini,maxi):
	for p in Listaplatos:
		if p.precio > mini and p.precio < maxi:
			print "dia :",p.dia
			print "turno :",p.turno
			print "nombre :",p.nombre
			print "precio :",p.precio 
		

def menucomensal():
	print "buscar platos por rangos de precios"
	print ""
	print "1.-(0-3.000)"
	print "2.-(3001-6000)"
	print "3.-(6001-1000)"
	op=raw_input("ingrese una opcion :")
	if op =="1":
		Rango(0,3000)
	elif op=="2":
		Rango(3001,6000)
	elif op == "3":
		Rango(6001,10000)
		

def main() :
	ciclo= True
	while ciclo:
		print ""
		print ""
		print "---------menu----------"
		print ""
		print "1.-menu principal"
		print "2.-menu login"
		print "3.-menu administrador"
		print "4.-menu recetas"
		print "5.-menu comensal (clientas)"
		print "6.-salir"
		op = raw_input("ingrse una opcion :")
		if op == "1":
			Menuprincipal()
		elif op == "2":
			Menulogin()
		elif op =="3":	 
			Menuadmin()
		elif op == "4":
			Menureceta()
		elif op == "5":
			menucomensal()
		elif op == "6":
			ciclo=False
			
		else:
			print "digito erronio"	
main()
