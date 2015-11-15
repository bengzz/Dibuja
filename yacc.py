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


def p_prog(p):
		'''prog : PR Vars Funciones princ Bloque '''
		mtemp = [(entero_val-1000), (float_val-2000), (void_val-3000)]
		direc["princ"] = temp
		if("globales" in direc):
			mtemp = direc["globales"]
			mtemp.pop(0)
			direc["globales"] = mtemp

def p_princ(p):
		'''princ : PRINC'''

def p_Funciones(p):
		'''Funciones : funciones 
		| vacia'''

def p_funciones(p):
		'''funciones : Tipo func Bloque Regresar'''

def p_func(p):
		'''func : Tipo fID'''

def p_fID(p):
		'''fID : ID'''

def p_Regresar(p):
		'''Regresar : Exp'''

def p_Bloque(p):
		'''Bloque : Vars Estatuto'''

#Variables ------------------------------
def p_Vars(p):
		'''Vars : globales 
		| locales
		| vacia'''
		
def p_globales(p):
	'''globales : glob var'''
	
def p_glob(p):
		'''glob : GL'''
		
def p_locales(p):
		'''locales : loc var'''

def p_loc(p):
		'''loc : LC'''

def var(p):
		'''var : V Tipo fID VarCte'''
#Variables ------------------------------

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
		'''Expresion : Subexpresion'''

def p_Subexpresion(p):
		'''Subexpresion : Exp'''

def p_Exp(p):
		'''Exp : Termino'''

def p_Termino(p):
		'''Termino : Factor'''

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

def p_Factor(p):
		'''Factor : Expresion'''

def p_VarCte(p):
		'''VarCte : Exp'''

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