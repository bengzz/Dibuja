import sys
import math
from Tkinter import *
from adminMemoria import AdminMemoria
from pila import Pila

memoria = AdminMemoria()
proc = dict()
quad = []
activo = True
quadActual = 0
relleno = False

#Funcion que corre mientras que no se ha terminado el programa
def vivo():
		while(activo):
					opciones[quad[quadActual][0]]()
			
#Funcion que suma 2 numeros del cuadruplo
def suma():
		global quadActual
		primero = memoria.getValor(quad[quadActual][1])
		segundo = memoria.getValor(quad[quadActual][2])
		resultado = primero + segundo
		memoria.escribeValor(quad[quadActual][3], resultado)
		quadActual += 1
		
#Funcion que resta 2 numeros del cuadruplo
def resta():
		global quadActual
		primero = memoria.getValor(quad[quadActual][1])
		segundo = memoria.getValor(quad[quadActual][2])
		resultado = primero - segundo
		memoria.escribeValor(quad[quadActual][3], resultado)
		quadActual += 1
		
#Funcion que multiplica 2 numeros del cuadruplo
def multiplica():
		global quadActual
		primero = memoria.getValor(quad[quadActual][1])
		segundo = memoria.getValor(quad[quadActual][2])
		resultado = primero * segundo
		memoria.escribeValor(quad[quadActual][3], resultado)
		quadActual += 1
		
#Funcion que divide 2 numeros del cuadruplo
def divide():
		global quadActual
		primero = memoria.getValor(quad[quadActual][1])
		segundo = memoria.getValor(quad[quadActual][2])
		resultado = primero / segundo
		memoria.escribeValor(quad[quadActual][3], resultado)
		quadActual += 1
				
#Funcion que compara si un numero es menor que el otro del cuadruplo
def menorQue():
		global quadActual
		primero = memoria.getValor(quad[quadActual][1])
		segundo = memoria.getValor(quad[quadActual][2])
		resultado = primero < segundo
		memoria.escribeValor(quad[quadActual][3], resultado)
		quadActual += 1
		
#Funcion que compara si un numero es menor o igual que el otro del cuadruplo
def menorIgQue():
		global quadActual
		primero = memoria.getValor(quad[quadActual][1])
		segundo = memoria.getValor(quad[quadActual][2])
		resultado = primero <= segundo
		memoria.escribeValor(quad[quadActual][3], resultado)
		quadActual += 1

#Funcion que compara si un numero es mayor que el otro del cuadruplo
def mayorQue():
		global quadActual
		primero = memoria.getValor(quad[quadActual][1])
		segundo = memoria.getValor(quad[quadActual][2])
		resultado = primero > segundo
		memoria.escribeValor(quad[quadActual][3], resultado)
		quadActual += 1
		
#Funcion que compara si un numero es mayor o igual que el otro del cuadruplo
def mayorIgQue():
		global quadActual
		primero = memoria.getValor(quad[quadActual][1])
		segundo = memoria.getValor(quad[quadActual][2])
		resultado = primero >= segundo
		memoria.escribeValor(quad[quadActual][3], resultado)
		quadActual += 1
		
#Funcion que compara si un numero es diferente que el otro del cuadruplo
def diferenteQue():
		global quadActual
		primero = memoria.getValor(quad[quadActual][1])
		segundo = memoria.getValor(quad[quadActual][2])
		resultado = primero != segundo
		memoria.escribeValor(quad[quadActual][3], resultado)
		quadActual += 1
		
#Funcion que compara si un numero es igual que el otro del cuadruplo
def igualQue():
		global quadActual
		primero = memoria.getValor(quad[quadActual][1])
		segundo = memoria.getValor(quad[quadActual][2])
		resultado = primero == segundo
		memoria.escribeValor(quad[quadActual][3], resultado)
		quadActual += 1
		
#Funcion que obtiene el color dado por el programador
def obtenerColor(rojo, verde, azul):
		rojo = int(rojo)
		if(rojo > 255):
				rojo = 255
		verde = int(verde)
		if(verde > 255):
				verde = 255
		azul = int(azul)
		if(azul > 255):
				azul = 255
				
		color = '#' + str(format(rojo, '02x')) + str(format(verde, '02x')) + str(format(azul, '02x'))
		return color
		
#Funcion que cambia el color del contorno
def colorContorno():
		global quadActual, colorCont
		rojo = memoria.getValor(quad[quadActual][1])
		verde = memoria.getValor(quad[quadActual][2])
		azul = memoria.getValor(quad[quadActual][3])
		colorCont = obtenerColor(red, green, blue)
		quadActual += 1
		
#Funcion que cambia el color del relleno
def colorRelleno():
		global quadActual, colorRell
		rojo = memoria.getValor(quad[quadActual][1])
		verde = memoria.getValor(quad[quadActual][2])
		azul = memoria.getValor(quad[quadActual][3])
		colorRell = obtenerColor(red, green, blue)
		quadActual += 1
		
#Funcion que cambia el grosor 
def grosor():
		global quadActual, grosor
		grosor = memoria.getValor(quad[quadActual][1])
		quadActual += 1
		
#Funcion que cambia la rotacion 
def rotacion():
		global quadActual, rotacion
		rotacion = memoria.getValor(quad[quadActual][1])
		quadActual += 1

#Funcion que cambia la posicion
def posicion():
		global quadActual, posicion
		posicion = memoria.getValor(quad[quadActual][1])
		quadActual += 1
		
#Funcion que asigna un valor a las variables
def asigna():
		global quadActual
		resultado = memoria.getValor(quad[quadActual][1])
		memoria.escribeValor(quad[quadActual][3], resultado)
		quadActual += 1

#Funcion que crea un rectangulo
def cuadrado():
        global quadActual, relleno, colorRelleno, colorContorno, grosor
        x = memoria.getValor('41000')
        y = memoria.getValor('41001')
        x2 = x + memoria.getValor(quad[quadActual][1])
        y2 = y + memoria.getValor(quad[quadActual][2])
        
        if(relleno):
        	w.create_rectangle(x, y, x2, y2, fill=colorRelleno, outline=colorContorno, width=grosor)
        else:
        	w.create_rectangle(x, y, x2, y2, fill='', outline=colorContorno, width=grosor)
        memoria.escribeValor('41000', x2)
        memoria.escribeValor('41001', y2)
        quadActual += 1

#Funcion que crea un triangulo        
def triangulo():
		global quadActual, relleno, colorRelleno, colorContorno, grosor
		x = memoria.getValor(quad[quadActual][1])
		y = memoria.getValor(quad[quadActual][2])
		quadActual += 1
		x2 = memoria.getValor(quad[quadActual][0])
		y2 = memoria.getValor(quad[quadActual][1])
		x3 = memoria.getValor(quad[quadActual][2])
		y3 = memoria.getValor(quad[quadActual][3])
		
		if(relleno):
			w.create_polygon(x, y, x2, y2, x3, y3, fill=colorRelleno, outline=colorContorno, width=grosor)
		else:
			w.create_polygon(x, y, x2, y2, x3, y3, fill='', outline=colorContorno, width=grosor)
		memoria.escribeValor('41000', x3)
		memoria.escribeValor('41001', y3)
		quadActual += 1
        
#Funcion para crear un circulo
def circulo():
		global quadActual, relleno, colorRelleno, colorContorno, grosor
		tamano = memoria.getValor(quad[quadActual][1])
		x = memoria.getValor('41000') - tamano
		y = memoria.getValor('41001') - tamano
		x2 = x + (tamano * 2)
		y2 = x + (tamano * 2)
		
		if(relleno):
			w.create_oval(x, y, x2, y2, fill=colorRelleno, outline=colorContorno, width=grosor)
		else:
			w.create_oval(x, y, x2, y2, fill='', outline=colorContorno, width=grosor)
		memoria.escribeValor('41000', x2)
		memoria.escribeValor('41001', y2)
		quadActual += 1

#Funcion para crear un arco
def arco():
		global quadActual, relleno, colorRelleno, colorContorno, grosor
		tamano = memoria.getValor(quads[quadActual][1])
		x = memoria.getValor('41000') - tamano
		y = memoria.getValor('41001') - tamano
		x2 = x + (tamano * 2)
		y2 = x + (tamano * 2)
		
		if(relleno):
			w.create_arc(x, y, x2, y2, fill=colorRelleno, outline=colorContorno, width=grosor)
		else:
			w.create_arc(x, y, x2, y2, fill='', outline=colorContorno, width=grosor)
		y2 = y2 - tamano
		memoria.escribeValor('41000', x2)
		memoria.escribeValor('41001', y2)
		quadActual += 1
        
#Funcion para crear un poligono
def poligono():
		global quadActual, colorRelleno, colorContorno, grosor
		direccion = int(quad[quadActual][1])
		aux = int(quad[quadActual][2])
		vertices = []
		dmem = (memoria.getValor('41000'), memoria.getValor('41001'))
		vertices.append(dmem)
		cont = 0
		while cont < aux:
				dmem = (memoria.getValor(str(cont + direccion)), memoria.getValor(str(cont + 1 + direccion)))
				vertices.append(dmem)
				cont += 2
		if(relleno):
				w.create_polygon(vertices, fill=colorRelleno, outline=colorContorno, width=grosor)
		else:
				w.create_polygon(vertices, fill='', outline=colorContorno, width=grosor)
		quadActual += 1

#Funcion para crear una linea

#define si la figura tendra un color de relleno
def relleno():
		global quadActual, relleno
		if(quad[quadActual][3] == '1'):
				relleno = True
		else:
				relleno = False
		quadActual += 1
		
#Seguir trabajando en los demas detalles.................................187
#Seguir trabajando en los demas detalles.................................187
#Seguir trabajando en los demas detalles.................................435
#Seguir trabajando en los demas detalles.................................435

#Cambia el cuadruplo acutal
def goto():
		global quadActual
		quadActual = int(quad[quadActual][3])
		
#Cambia el cuadruplo cuando la condicion es falsa
def goto_falso():
		global quadActual
		temporal = int(quad[quadActual][1])
		if(temporal):
						quadActual += 1
		else:
						quadActual = int(quad[quadActual[3]])

#Creacion de la memoria para la funcion llamada
def era():
		global quadActual
		temporal = int(quad[quadActual][3])
		memoria.setFunciones(temporal[0], temporal[1], temporal[2], temporal[3], temporal[4], temporal[5], temporal[6])
		quadActual += 1

#Funcion que asigna valores que seran mandandos a las funciones
def param():
		global quadActual
		if quad[quadActual][3][1] == '7':
			memoria.escribeValorApuntado(quad[quadActual][3], quad[quadActual][1], 1)
		else:
			memoria.escribeValor(quad[quadActual][3], quad[quadActual][1])
		quadActual += 1
		
#Guarda el cuadruplo actual, da la posicion a la cual va a regresar y cambia el scope actual y el cuadruplo
def goSub():
		global quadActual
		memoria.cambiaAlcance()
		memoria.push_apuntador(quadActual+1)
		quadActual = int(quad[quadActual][3])
		
#Seguir trabajando en los demas detalles.................................479
#Seguir trabajando en los demas detalles.................................479
#Seguir trabajando en los demas detalles.................................479
#Seguir trabajando en los demas detalles.................................479
#Seguir trabajando en los demas detalles.................................630
#Seguir trabajando en los demas detalles.................................630
#Seguir trabajando en los demas detalles.................................630
#Seguir trabajando en los demas detalles.................................630
		