import sys
import math
from Tkinter import *
from adminMemoria import AdminMemoria
from pila import Pila

memoria = AdminMemoria()
quad = []
pro = dict()
activo = True
quadActual = 0
relleno = False
colorCont = '#000000000'
colorRell = '#000000000'
gros = 1

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
def dividir():
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
		colorCont = obtenerColor(rojo, verde, azul)
		quadActual += 1
		
#Funcion que cambia el color del relleno
def colorRelleno():
		global quadActual, colorRell
		rojo = memoria.getValor(quad[quadActual][1])
		verde = memoria.getValor(quad[quadActual][2])
		azul = memoria.getValor(quad[quadActual][3])
		colorRell = obtenerColor(rojo, verde, azul)
		quadActual += 1
			
#Funcion que cambia el gros 
def grosor():
		global quadActual, gros
		gros = memoria.getValor(quad[quadActual][1])
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

#Funcion para el texto
def texto():
		global quadActual, colorRell, gros
		final = int(quad[quadActual][3])
		inicio = int(quad[quadActual][2])
		longitud = final - inicio
		inicio = 0
		dire = int(quad[quadActual][1])
		palabra = ''
		while inicio <= longitud:
				dirTem = dire + inicio
				dirTem = str(dirTem)
				palabra += memoria.getValor(dirTem)
				inicio += 1
		w.create_text(memoria.getValor('41000'), memoria.getValor('41001'), text=palabra, fill=colorRell)
		quadActual += 1
		
#Funcion que crea una linea
def linea():
		global quadActual, gros, colorRell
		uno = int(quad[quadActual][1])
		dos = int(quad[quadActual][2])
		vertice = []
		aux = (memoria.getValor('41000'), memoria.getValor('41001'))
		vertice.append(aux)
		creaLin = 0
		while creaLin < dos:
				aux = (memoria.getValor(str(creaLin + uno)), memoria.getValor(str(creaLin + 1 + uno)))
				vertice.append(aux)
				creaLin += 2
		w.create_line(vertice, fill=colorRell)
		quadActual += 1
		
#funcion que crea un rectangulo
def rectangulo():
		global quadActual, relleno, colorRell, colorCont, gros
		x = memoria.getValor('41000')
		y = memoria.getValor('41001')
		x2 = x + memoria.getValor(quad[quadActual][1])
		y2 = y + memoria.getValor(quad[quadActual][2])
			
		if(relleno):
			w.create_rectangle(x, y, x2, y2, fill=colorRell, outline=colorCont, width=gros)	
		else:
			w.create_rectangle(x, y, x2, y2, fill='', outline=colorCont, width=gros )
			memoria.escribeValor('41000', x2)
			memoria.escribeValor('41001', y2)
			quadActual += 1
			
#Funcion que crea un rectangulo
def cuadrado():
        global quadActual, relleno, colorRell, colorCont, gros
        x = memoria.getValor('41000')
        y = memoria.getValor('41001')
        x2 = x + memoria.getValor(quad[quadActual][1])
        y2 = y + memoria.getValor(quad[quadActual][1])
        
        if(relleno):
        	w.create_rectangle(x, y, x2, y2, fill=colorRell, outline=colorCont, width=gros)
        else:
        	w.create_rectangle(x, y, x2, y2, fill='', outline=colorCont, width=gros)
        memoria.escribeValor('41000', x2)
        memoria.escribeValor('41001', y2)
        quadActual += 1

#Funcion que crea un triangulo        
def triangulo():
		global quadActual, relleno, colorRell, colorCont, gros
		x = memoria.getValor(quad[quadActual][1])
		y = memoria.getValor(quad[quadActual][2])
		quadActual += 1
		x2 = memoria.getValor(quad[quadActual][0])
		y2 = memoria.getValor(quad[quadActual][1])
		x3 = memoria.getValor(quad[quadActual][2])
		y3 = memoria.getValor(quad[quadActual][3])
		
		if(relleno):
			w.create_polygon(x, y, x2, y2, x3, y3, fill=colorRell, outline=colorCont, width=gros)
		else:
			w.create_polygon(x, y, x2, y2, x3, y3, fill='', outline=colorCont, width=gros)
		memoria.escribeValor('41000', x3)
		memoria.escribeValor('41001', y3)
		quadActual += 1
        
#Funcion para crear un circulo
def circulo():
		global quadActual, relleno, colorRell, colorCont, gros
		tamano = memoria.getValor(quad[quadActual][1])
		x = memoria.getValor('41000') - tamano
		y = memoria.getValor('41001') - tamano
		x2 = x + (tamano * 2)
		y2 = x + (tamano * 2)
		
		if(relleno):
			w.create_oval(x, y, x2, y2, fill=colorRell, outline=colorCont, width=gros)
		else:
			w.create_oval(x, y, x2, y2, fill='', outline=colorCont, width=gros)
		memoria.escribeValor('41000', x2)
		memoria.escribeValor('41001', y2)
		quadActual += 1

#Funcion para crear un arco
def arco():
		global quadActual, relleno, colorRell, colorCont, gros
		tamano = memoria.getValor(quad[quadActual][1])
		x = memoria.getValor('41000') - tamano
		y = memoria.getValor('41001') - tamano
		x2 = x + (tamano * 2)
		y2 = x + (tamano * 2)
		
		if(relleno):
			w.create_arc(x, y, x2, y2, fill=colorRell, outline=colorCont, width=gros)
		else:
			w.create_arc(x, y, x2, y2, fill='', outline=colorCont, width=gros)
		y2 = y2 - tamano
		memoria.escribeValor('41000', x2)
		memoria.escribeValor('41001', y2)
		quadActual += 1
        
#Funcion para crear un poligono
def poligono():
		global quadActual, colorRell, colorCont, gros
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
				w.create_polygon(vertices, fill=colorRell, outline=colorCont, width=gros)
		else:
				w.create_polygon(vertices, fill='', outline=colorCont, width=gros)
		quadActual += 1

def pxy():
#changes the pen position
	global quadActual
	memoria.escribeValor('41001', memoria.getValor(quad[quadActual][1]))
	memoria.escribeValor('41000', memoria.getValor(quad[quadActual][2]))
	quadActual += 1

#define si la figura tendra un color de relleno
def relleno():
		global quadActual, relleno
		if(quad[quadActual][3] == '1'):
				relleno = True
		else:
				relleno = False
		quadActual += 1
		
#Cambia el cuadruplo acutal
def goto():
		global quadActual
		quadActual = int(quad[quadActual][3])
		
#Cambia el cuadruplo cuando la condicion es falsa
def goto_falso():
		global quadActual
		temporal = memoria.getValor(quad[quadActual][1])
		if(temporal):
				quadActual += 1
		else:
				quadActual = int(quad[quadActual][3])

#Creacion de la memoria para la funcion llamada
def era():
		global quadActual
		temporal = pro[quad[quadActual][3]]
		memoria.setFunciones(temporal[0], temporal[1], temporal[2], temporal[3], temporal[4], temporal[5], temporal[6])
		quadActual += 1

#Funcion que asigna valores que seran mandandos a las funciones
def param():
		global quadActual
		if quad[quadActual][3][1] == '7':
			memoria.escribeValorApuntado(quad[quadActual][3], quad[quadActual][1], 1)
		else:
			memoria.escribeValorS(quad[quadActual][3], memoria.getValor(quad[quadActual][1]))
		quadActual += 1
		
#Guarda el cuadruplo actual, da la posicion a la cual va a regresar y cambia el scope actual y el cuadruplo
def goSub():
		global quadActual
		memoria.cambiaAlcance()
		memoria.push_apuntador(quadActual+1)
		quadActual = int(quad[quadActual][3])

#Para accesar a un valor desde un arreglo, checa que este dentro del rango		
def dimArreglo():
		global quadActual
		valor = memoria.getValor(quad[quadActual][2])
		dimA = int(quad[quadActual][1])
		if valor < 0 or valor > dimA:
				print "Fuera de rango", valor, " ", dimA
				sys.exit(0)
		quadActual += 1
		
#Para accesar a un valor desde una matriz, checa que este dentro del rango
def dimMat():
		global quadActual
		valor = int(quad[quadActual][2])
		dimM = int(quad[quadActual][1])
		if valor < 0 or valor > dimM:
				print "Fuera de rango", valor, " ", dimM
				sys.exit(0)
		quadActual += 1
		
#Regresa la direccion del valor al que se quiere accesar
def apuntadorDir():
		global quadActual
		if quad[quadActual][1][1] == '7':
				dirV = memoria.getValorApuntado(quad[quadActual][1])
		else:
				dirV = int(quad[quadActual][1])
		apuntaV = memoria.getValor(quad[quadActual][2])
		dirV = dirV + apuntaV
		memoria.escribeValorApuntado(quad[quadActual][3], str(dirV), 0)
		quadActual += 1

#Obtiene la direccion para el valor y lo almacena en el apuntador
def apuntadorDirC():
		global quadActual
		dirV = int(quad[quadActual][1])
		apuntaV = int(quad[quadActual][2])
		dirV = dirV + apuntaV
		memoria.escribeValorApuntado(quad[quadActual][3], str(dirV), 0)
		quadActual += 1

#Termina el procedimiento y borra la memoria que utilizo		
def endProc():
		global quadActual
		quadActual = int(memoria.pop_apuntador())
		memoria.borrar_funcion()
		
#Termina el programa
def endProg():
		global activo
		activo = False

opciones = { '+' : suma,
		'-' : resta,
		'*' : multiplica,
		'/' : dividir,
		'<' : menorQue,
		'>' : mayorQue,
		'<=' : menorIgQue,
		'>=' : mayorIgQue,
		'!=' : diferenteQue,
		'==' : igualQue,
		'GOTO': goto,
		'GOTOF' : goto_falso,
		'ENDPROG': endProg,
		'101': asigna,
		'201' : rectangulo,
		'202' : triangulo,
		'203' : circulo,
		'204' : cuadrado,
		'205' : poligono,
		'206' : linea,
		'207' : arco,
		'208' : texto,
		'209' : relleno,
		'301' : colorContorno,
		'302' : colorRelleno,
		'304' : grosor,
		'307' : pxy,
		'ERA' : era,
		'PARAMETRO' : param,
		'GOSUB' : goSub,
		'RETURN' : param,
		'DIM' : dimArreglo,
		'DIMC' : dimMat,
		'DIR' : apuntadorDir,
		'DIRC' : apuntadorDirC,
		'ENDPROC' : endProc}
				
#Correr el programa
if(len(sys.argv) > 1):
	archivo = open(sys.argv[1], "r")
	contador = 0.5
	l = archivo.readlines()
	acumulador = ""
	for linea in l:
		linea = linea.strip()
		if(linea == '%%'):
			contador += 1
		else:
			if(contador <= 1):
				if(contador == 1):
					i = linea.split(' ')
					memoria.escribeValor(i[1], i[0])
				else:
					contador += 0.5
					i = linea.split(' ')
					memoria.constTamano(int(i[0]), int(i[1]), int(i[2]))
			if(contador == 2):
				i = linea.split(' ')
				if(i[0] == 'princ'):
					memoria.setMemoriaPrinc(i[1], i[2], i[3], i[4], i[5], i[6], i[7]) 
				elif(i[0] == 'globales'):
					memoria.setMemoriaGlobales(i[1], i[2], i[3], i[4], i[5], i[6], i[7])
				else:
					pro[i[0]] = [i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
			if(contador == 3):
				i = linea.split(' ')
				s = [i[0], i[1], i[2], i[3]]
				quad.append(s)
		acumulador += linea
	rt = Tk()
	print "const int float", len(quad)
	memoria.imprimeConstantes()
	w = Canvas(rt, width=600, height=480)
	w.configure(background='white')
	w.pack()
	vivo()
	print "const int float"
	memoria.imprimeConstantes()
	print "main"
	memoria.imprimePrinc()
	print "global"
	memoria.imprimeGlobales()
	mainloop()
		
else:
    print "No se ejecuto correctamente"