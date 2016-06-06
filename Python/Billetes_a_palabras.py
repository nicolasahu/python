#Convertir billetes(numeros a palabras) Hasta el 9.999

import math #para utilizar funciones matematicas
#En este algoritmo la version mas corta es usando arreglos
#como ven abajo hay que definir listas con unidades, decenas, centenas, etc
#------------------------------------------------------------------------------------------------------------------------------------------------
unidad=["Cero", "Un", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez" ]
decena=["Veinte", "Treinta", "Cuarenta", "Cincuenta", "Sesenta", "Setenta", "Ochenta", "Noventa"]
centena=["Ciento", "Doscientos", "Trescientos", "Cuatroscientos", "Quinientos", "Seiscientos", "Setescientos", "Ochoscientos", "Novescientos"]
miles=["Mil", "Dosmil", "Tresmil", "Cuatromil", "Cincomil", "Seismil", "Sietemil", "Ochomil", "Nuevemil"]
raro=["Once", "Doce", "Trece", "Catorce", "Quince", "Dieciseis", "Diecisiete", "Dieciocho", "Diecinueve"]
#------------------------------------------------------------------------------------------------------------------------------------------------
a=int(raw_input("Ingrese un valor (numero): "))
#-------------------------------------------------------
if a>=0 and a<11: #aca imprimira solo valores de unidad (inclui el diez por orden)
	print unidad[a], "Pesos" 
elif a<20: #En este caso imprimira los numeros que no se pueden concatenar (once, doce, quince, etc)					 
	print raro[a-11], "Pesos"
elif a>=20 and a<100: #Este filtro tomara del numero 20 al 99 osea las decenas
	uni=a%10 #Saque el resto del valor para separar la unidad de la decena
	dec=int(math.floor(a/10)) #aca tomo el valor entero para separar la decena de la unidad
	if uni==0: #si la unidad es 0, solo mostrara el valor de la decena
		print decena[dec-2], "Pesos"#en este caso puse -2 porque la lista comienza del numero 20
	else: #de lo ocntrario si la unidad no vale 0 imprimira ambas
		print decena[dec-2], "y", unidad[uni], "Pesos"
if a>=100 and a<1000: #Este filtro tomara del numero 100 al 999(centenas)
	if a==100:
		print "Cien Pesos"
	else:	
		uni=a%10 #separo la unidad
		dec=a%100 #separo la decena
		dec=dec-uni #le resto la unidad a la decena para que quede entera
		dec=int(math.floor(dec/10))#saco la posicion de la lista (si fuera 20 quedara = 2)
		cen=int(math.floor(a/100))#la centena en posicion de la lista
		if uni==0 and dec==0:
			print centena[cen-1], "pesos"
		elif uni==0 and dec!=0:
			print centena[cen-1], decena[dec-2], "Pesos"
		else:
			print centena[cen-1], decena[dec-2], "y", unidad[uni], "Pesos"
if a>=1000 and a<10000:
	uni=a%10
	dec=a%100
	dec=dec-uni
	dec=int(math.floor(dec/10))
	cen=a%1000
	cen=cen-dec-uni
	cen=int(math.floor(cen/100))
	mil=int(math.floor(a/1000))
	if uni==0 and dec==0 and cen==0:
		print miles[mil-1], "Pesos"
	elif uni==0 and dec==0 and cen!=0:
		print miles[mil-1], centena[cen-1], "Pesos"
	elif uni==0 and dec!=0 and cen!=0:
		print miles[mil-1], centena[cen-1], decena[dec-2], "Pesos"
	else:
		print miles[mil-1], centena[cen-1], decena[dec-2], "y", unidad[uni], "Pesos"
#----------------------------------------------------------------------------------------------------------
