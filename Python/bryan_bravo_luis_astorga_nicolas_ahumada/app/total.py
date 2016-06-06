# -*- coding: cp1252 -*-
import os
os.system("cls")
def borrar():
	from compra import listacompra
	listacompra[:]=[]
	print "lista de compra borrada"
	a=raw_input("precione enter ")


def menu():
	ciclo=True
	while ciclo:
		
		print "Donde Luchito"
		print "-----------------"
		print "      menu       "
		print "-----------------"
		print "1.-registrar compra"
		print "2.-lista de comidas"
		print "3.-imprimir compra"
		print "4,-lista de compra"
		print "5.-borrar lista de compra"
		print "6.-salir"
		op=input("ingrese opcion :")
		os.system("cls")
		if op ==1:
			from compra import registrarcompra
			registrarcompra()
			os.system("cls")
		
		elif op==2:
			from menucomida import listacomida
			listacomida()
			os.system("cls")
		elif op==3:
			from compra import imprimircompra
			imprimircompra()
		elif op ==4:
			from compra import listacom
			listacom()
		elif  op ==5:
			borrar()
		elif op==6:
			from compra import listacompra
			listacompra[:]=[]
				
			break



