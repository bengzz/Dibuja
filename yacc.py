import ply.yacc as yacc
import lex 
import sys
import re

#from stack import Stack
#from avail import avail

direc = dict()
dirtemp = dict()
entero_val = 1000
float_val = 2000
void_val = 3000
tokens = lex.tokens
vacia = False

#Programa------------------------------------------------------
def p_prog(p):
		'''prog : PR prog1 princ AC Bloque CC'''
		mtemp = [(entero_val-1000), (float_val-2000), (void_val-3000)]
		direc["princ"] = temp
		if("globales" in direc):
			mtemp = direc["globales"]
			mtemp.pop(0)
			direc["globales"] = mtemp

def p_prog1(p):
		'''prog1 : prog2 prog3''' 
	
def p_prog2(p):
		'''prog2 : Vars prog2
		| vacia'''
		
def p_prog3(p):
		'''prog3 : Funciones prog3
		| vacia'''

def p_princ(p):
		'''princ : PRINC'''
#Programa------------------------------------------------------

#Funciones------------------------------------------------------
def p_Funciones(p):
		'''Funciones : funciones'''

def p_funciones(p):
		'''funciones : Tipo fID AP func CP AC Bloque func4 CC'''

def p_func(p):
		'''func : func1
		| vacia'''
		
def p_func1(p):
		'''func1 : func2
		| func2 func3'''

def p_func2(p):
		'''func2 : Tipo fID func'''
		
def p_func3(p):
		'''func3 : C Tipo fID func'''
		
def p_func4(p):
		'''func4 : Regresar
		| vacia'''

def p_Regresar(p):
		'''Regresar : Exp PC'''

def p_fID(p):
		'''fID : ID'''
#Funciones------------------------------------------------------

#Bloque------------------------------------------------------
def p_Bloque(p):
		'''Bloque : b1
		| b2 '''
		
def p_b1(p):
		'''b1 : Estatuto'''
		
def p_b2(p):
		'''b2 : b3 Estatuto'''

def p_b3(p):
		'''b3 : Vars b3
		| vacia'''
#Bloque------------------------------------------------------

#Variables------------------------------------------------------
def p_Vars(p):
		'''Vars : globales 
		| locales'''
		
def p_globales(p):
	'''globales : glob var'''
	
def p_glob(p):
		'''glob : GL'''
		
def p_locales(p):
		'''locales : loc var'''

def p_loc(p):
		'''loc : LC'''

def p_var(p):
		'''var : V Tipo fID VarCte'''
#Variables------------------------------------------------------

def p_Estatuto(p):
		'''Estatuto : Asignacion 
		| Condicion 
		| Ciclo 
		| Llamada 
		| Objeto'''

def p_Tipo(p):
		'''Tipo : tipo'''
		
def p_tipo(p):
		'''tipo : ENT 
		| FLOT
		| BOOL  '''

def p_Expresion(p):
		'''Expresion : Subexpresion Expresion2'''

def p_Expresion2(p):
		'''Expresion2 : Expresion3
		| vacia'''

def p_Expresion3(p):
		'''Expresion3 : Expresion4 Expresion'''

def p_Expresion4(p):
		'''Expresion4 : Y
		| O'''

def p_Subexpresion(p):
		'''Subexpresion : Exp Subexpresion2'''
		
def p_Subexpresion2(p):
		'''Subexpresion2 : Subexpresion3
		| vacia'''

def p_Subexpresion3(p):
		'''Subexpresion3 : Subexpresion4 Exp'''
		
def p_Subexpresion4(p):
		'''Subexpresion4 : ME
		| MA
		| CI
		| CD'''

#Exp ------------------------------

def p_Exp(p):
		'''Exp : Termino Exp2'''

def p_Exp2(p):
		'''Exp2 : Exp4 Exp3 Exp
		| Exp4 vacia'''

def p_Exp3(p):
		'''Exp3 : SUM
		| RES'''

def p_Exp4(p):
		'''Exp4 : vacia'''

def p_Termino(p):
		'''Termino : Factor Termino2'''
		
def p_Termino2(p):
		'''Termino2 : Termino4 Termino3 Termino
		| Termino4 vacia'''

def p_Termino3(p):
		'''Termino3 : MUL
		| DIV'''
		
def p_Termino4(p):
		'''Termino4 : vacia'''

def p_Factor(p):
		'''Factor : Factor2
		| Factor3'''
		
def p_Factor2(p):
		'''Factor2 : AP Expresion CP'''
		
def p_Factor3(p):
		'''Factor3 : Factor4 VarCte'''
		
def p_Factor4(p):
		'''Factor4 : SUM
		| RES'''

#falta terminar varcte------------------------------------------------------
def p_VarCte(p):
		'''VarCte : VALI
		| VALF'''
#falta terminar varcte------------------------------------------------------

def p_Condicion(p):
		'''Condicion : Expresion Estatuto'''

def p_Asignacion(p):
		'''Asignacion : Exp Expresion'''

def p_Llamada(p):
		'''Llamada : Exp'''

def p_Ciclo(p):
		'''Ciclo : Mientras Para'''

def p_Mientras(p):
		'''Mientras : Expresion Estatuto'''

def p_Para(p):
		'''Para : Exp Expresion Expresion Estatuto'''

def p_Objeto(p):
		'''Objeto : Figura Color Posicion Grosor Rotacion
		| Texto Color Posicion Grosor Rotacion'''

def p_Color(p):
		'''Color : Contorno
		| Relleno'''

def p_Figura(p):
		'''Figura : Cuadrado
		| Circulo
		| Arco
		| Triangulo
		| Poligono
		| Linea'''

def p_Cuadrado(p):
		'''Cuadrado : Exp Exp'''

def p_Circulo(p):
		'''Circulo : Exp Exp'''

def p_Arco(p):
		'''Arco : Exp Exp'''

def p_Triangulo(p):
		'''Triangulo : Exp Exp Exp Exp Exp Exp'''

def p_Poligono(p):
		'''Poligono : Exp Exp'''

def p_Linea(p):
		'''Linea : Exp Exp'''

def p_Contorno(p):
		'''Contorno : Exp Exp Exp'''

def p_Relleno(p):
		'''Relleno : Exp Exp Exp'''

def p_Texto(p):
		'''Texto : Exp'''

def p_Grosor(p):
		'''Grosor : Exp'''

def p_Posicion(p):
		'''Posicion : Exp Exp'''

def p_Rotacion(p):
		'''Rotacion : Exp'''

def p_vacia(p):
		'''vacia : '''
		global vacia
		vacia = True

def guarda_var(var):
		global tipoVar
		if var in dirtemp:
			print "Variable existe ", var
			sys.exit(0)
		else:
			if tipoVar == "entero":
				global entero_val
				dirtemp[var] = [tipoVar, "var", entero_val]
				entero_val += 1
			else:
				global float_val
				dirtemp[var] = [tipoVar, "var", float_val]
				float_val += 1

def vars_declaradas(p):
		global tipoVar
		if(p != None):
			if(p not in dirtemp):
				if("Vars" in direc):
					if(p not in direc["Vars"[0]]):
						print "Variable no declarada ", p
						sys.exit(0)
					else:
						tipoVar = direc["Vars"][0][p][0]
				else:
					print "Variable no declarada ", p
					sys.exit(0)
			else:
				tipoVar = dirtemp[p][0]

def dir_var(p):
		if p in dirtemp:
			return dirtemp[p][2]
		else:
			if "Vars" in direc:
				return direc["Vars"][0][p][2]

def p_error(p):
		print "Syntax error en entrada!", p.tipo
					
parser = yacc.yacc()