import ply.yacc as yacc
import lex 
import sys
import re

from pila import Pila
from avail import avail

tokens = lex.tokens
hashT = dict()
funT = dict()
direc = dict()
cnst = dict()
entero_val = 1000
float_val = 2000
void_val = 3000
vacia = False
avail = avail()
idF = None
TipoV = None
apuntador = False
apuntadorD = 0
contadorP = 0
vDir = 0
aArch = ''
cnst_entero_cnt = 40000
cnst_float_cnt = 41002
cnst_void_cnt = 42000

#Programa------------------------------------------------------
def p_prog(p):
		'''prog : PR prog1 princ AC Bloque CC'''
		mtemp = [(void_val-3000), (entero_val-1000), (float_val-2000)]
		mtemp.extend(avail.get_temp_dir())
		direc["princ"] = temp
		if("globales" in direc):
				mtemp = direc["globales"]
				mtemp.pop(0)
				direc["globales"] = mtemp
		cuads = ['ENDPROG', -1, -1, -1]
		avail.append_quad(cuads)

def p_prog1(p):
		'''prog1 : prog2 prog3''' 

def p_prog2(p):
		'''prog2 : Vars prog2
		| vacia'''
		avail.princ()
		
def p_prog3(p):
		'''prog3 : Funciones prog3
		| vacia'''

def p_princ(p):
		'''princ : PRINC'''
		avail.princ_goto()
		avail.setBloque(2)
#Programa------------------------------------------------------

#Funciones------------------------------------------------------
def p_Funciones(p):
		'''Funciones : FUNCION funciones'''
		avail.setFuncQ()
		avail.setBloque(3)

def p_funciones(p):
		'''funciones : funcIn AC Bloque func3 CC'''
		mtemp = avail.get_temp_dir()
		direc[avail.getAlcance()][5] = mtemp[0]
		direc[avail.getAlcance()][6] = mtemp[1]
		direc[avail.getAlcance()][7] = mtemp[2]
		direc[avail.getAlcance()][8] = mtemp[3]
		hashT.clear()
		avail.funcion_end()

def p_funcIn(p):
		'''funcIn : FTipo fID AP func CP'''
		DictV = dict(funT)
		global entero_val, float_val, void_val, contadorP, idF
		idF = avail.getAlcance()
		mtemp = [DictV, avail.getFuncQ(), (void_val-3000), (entero_val-1000), (float_val-2000), 0, 0, 0, 0]
		direc[avail.getAlcance()] = mtemp
		cant = direc["globales"][3]+1
		direc["globales"][0][avail.getAlcance()] = ["flotante", 'func', 13000 + cant]
		direc["globales"][3] = cant
		funT.clear()
		contadorP = 0
		
def p_func(p):
		'''func : func1 func2
		| vacia'''
		
def p_func1(p):
		'''func1 : Tipo fID'''
		guarda_var(p[3])
		funT[p[3]] = [TipoV, contadorP, (hashT[p[3]][2]+30000)]
		contador += 1

def p_func2(p):
		'''func2 : C func1 func2
		| vacia'''
		
def p_func3(p):
		'''func3 : Regresar
		| vacia'''

def p_Regresar(p):
		'''Regresar : REGRESA Exp PC'''

def p_fID(p):
		'''fID : ID'''
		avail.setAlcance(p[1])
#Funciones------------------------------------------------------

#Bloque------------------------------------------------------
def p_Bloque(p):
		'''Bloque : b2 Estatuto b3'''
		
def p_b2(p):
		'''b2 : Vars b2
		| vacia'''	
			
def p_b3(p):
		'''b3 : Estatuto b3
		| vacia'''	
#Bloque------------------------------------------------------

#Variables------------------------------------------------------
def p_Vars(p):
		'''Vars : globales 
		| locales
		| varFunciones'''
		
def p_globales(p):
		'''globales : glob var'''
		global entero_val, float_val, void_val
		bloque_dir(hashT, 1)
		dvDict = dict(hashT)
		mtemp = [dvDict, (void_val-3000), (entero_val-1000), (float_val-2000)]
		mtemp.extend(avail.get_temp_dir())
		direc["globales"] = mtemp
		hashT.clear()
		entero_val = 1000
		float_val = 2000
		void_val = 3000
		
def p_glob(p):
		'''glob : GL'''
		avail.setBloque(1)
		
def p_varFunciones(p):
		'''varFunciones : loc var'''
		bloque_dir(hashT, 3)
		global entero_val, float_val, void_val, idF
		direc[idF][2] = (void_val-3000)
		direc[idF][3] = (entero_val-1000)
		direc[idF][4] = (float_val-2000)
		void_val = 3000
		entero_val = 1000
		float_val = 2000
		
def p_locales(p):
		'''locales : var'''
		bloque_dir(hashT, 2)

def p_loc(p):
		'''loc : LC'''

def p_var(p):
		'''var : Tipo var1 PC'''
		
def p_var1(p):
		'''var1 : varSalvar var2 var3'''

def p_var2(p):
		'''var2 : AC VarCte CC
		| vacia'''

def p_var3(p):
		'''var3 : C var1
		| vacia'''
		
def p_varSalvar(p):
		'''varSalvar : ID'''
		guarda_var(p[1])
		global vDir
		vDir = dir_var(p[1]) + (avail.getBloque() * 10000)
		avail.IDPila_push(p[1])
#Variables------------------------------------------------------

#Estatuto------------------------------------------------------
def p_Estatuto(p):
		'''Estatuto : Asignacion 
		| Condicion 
		| Ciclo 
		| Llamada 
		| Objeto'''
#Estatuto------------------------------------------------------

#Tipo------------------------------------------------------
def p_FTipo(p):
		'''FTipo : VOID
		| Tipo'''
		global TipoV
		if(p[1] == 'void'):
				TipoV = p[1]
		avail.setTR(TipoV)
		
def p_Tipo(p):
		'''Tipo : tipo'''
		
def p_tipo(p):
		'''tipo : ENT 
		| FLOT
		| BOOL'''
		global TipoV
		TipoV = p[1]
#Tipo------------------------------------------------------

#Expresion, subexpresion------------------------------------------------------
def p_Expresion(p):
		'''Expresion : Subexpresion Expresion2'''

def p_Expresion2(p):
		'''Expresion2 : Expresion3
		| vacia'''

def p_Expresion3(p):
		'''Expresion3 : Expresion4 Expresion'''
		avail.expresion()

def p_Expresion4(p):
		'''Expresion4 : Y
		| O'''
		avail.PilaOp_push(p[1])

def p_Subexpresion(p):
		'''Subexpresion : Exp Subexpresion2'''
		
def p_Subexpresion2(p):
		'''Subexpresion2 : Subexpresion3
		| vacia'''

def p_Subexpresion3(p):
		'''Subexpresion3 : Subexpresion4 Exp'''
		avail.expresion()
		
def p_Subexpresion4(p):
		'''Subexpresion4 : ME
		| MA
		| CI
		| CD'''
		avail.PilaOp_push(p[1])
#Expresion, subexpresion------------------------------------------------------

#Exp, termino, factor -------------------------------------------------
def p_Exp(p):
		'''Exp : Termino Exp2'''

def p_Exp2(p):
		'''Exp2 : Exp4 Exp3 Exp
		| Exp4 vacia'''

def p_Exp3(p):
		'''Exp3 : SUM
		| RES'''
		avail.PilaOp_push(p[1])

def p_Exp4(p):
		'''Exp4 : vacia'''
		avail.sum_res()

def p_Termino(p):
		'''Termino : Factor Termino2'''
		
def p_Termino2(p):
		'''Termino2 : Termino4 Termino3 Termino
		| Termino4 vacia'''

def p_Termino3(p):
		'''Termino3 : MUL
		| DIV'''
		avail.PilaOp_push(p[1])
		
def p_Termino4(p):
		'''Termino4 : vacia'''
		avail.mult_div()

def p_Factor(p):
		'''Factor : Factor2 Expresion CP
		| Factor3'''
		if(len(p) == 4):
				avail.PilaOp_pop()
		
def p_Factor2(p):
		'''Factor2 : AP'''
		avail.PilaOp_push(p[1])
		
def p_Factor3(p):
		'''Factor3 : Factor4 VarCte'''
		if(len(p) == 3):
				ID = avail.IDPila_pop()
				MD = avail.DPila_pop()
				if(MD):
						apuntador = avail.OPila_pop()
				vars_declaradas(ID)
				avail.TPila_push(tipo_variable(ID, "var"))
				avail.OPila_push(dir_var(ID))
				if(MD):
						avail.dm(dm(ID), apuntador)
				if not MD:
						if avail.DPila_pop():
								avail.OPila_pop()
								avail.TPila_pop()
		
def p_Factor4(p):
		'''Factor4 : SUM
		| RES'''
#Exp, termino, factor -------------------------------------------------

#falta terminar varcte bool---------------------------------------------------------------------------------------------------
def p_VarCte(p):
		'''VarCte : VarCte2
		| VALI
		| VALF
		| STR'''

def p_VarCte2(p):
		''' VarCte2 : fID VarCte3'''
		
def p_VarCte3(p):
		''' VarCte3 : AP Exp VarCte4 CP
		| AC Exp CC
		| vacia'''
		
def p_VarCte4(p):
		''' VarCte4 : C Exp VarCte4
		| vacia'''
#falta terminar varcte bool---------------------------------------------------------------------------------------------------

#condicion------------------------------------------------------
def p_Condicion(p):
		'''Condicion : SI AP Expresion CP Estatuto Condicion2'''

def p_Condicio2(p):
		'''Condicion2 : SINO Estatuto
		| vacia'''
#condicion------------------------------------------------------

#asignacion------------------------------------------------------
def p_Asignacion(p):
		'''Asignacion : fID Asignacion2 IG Expresion PC'''
		
def p_Asignacion2(p):
		'''Asignacion2 : AC Exp CC
		| vacia'''
#asignacion------------------------------------------------------

#llamada------------------------------------------------------
def p_Llamada(p):
		'''Llamada : fID AP Llamada2 CP PC'''

def p_Llamada2(p):
		'''Llamada2 : Llamada3
		| vacia'''
				
def p_Llamada3(p):
		'''Llamada3 : Exp Llamada4'''

def p_Llamada4(p):
		'''Llamada4 : C Llamada3
		| vacia'''
#llamada------------------------------------------------------

#ciclo------------------------------------------------------
def p_Ciclo(p):
		'''Ciclo : Mientras 
		| Para'''

def p_Mientras(p):
		'''Mientras : MIENTRAS AP Expresion CP AC Estatuto aux2 CC'''
		
def p_aux2(p):
		'''aux2 : Estatuto aux2
		| vacia'''

def p_Para(p):
		'''Para : PARA AP fID IG Exp C Expresion C Expresion CP AC Estatuto aux2 CC'''
#ciclo------------------------------------------------------

#objeto------------------------------------------------------
def p_Objeto(p):
		'''Objeto : Figura Color Objeto2 Posicion
		| Texto Color Objeto2 Posicion'''
		
def p_Objeto2(p):
		'''Objeto2 : Grosor Rotacion
		| Grosor
		| Rotacion
		| vacia'''
		
def p_Figura(p):
		'''Figura : Cuadrado
		| Circulo
		| Arco
		| Triangulo
		| Poligono
		| Linea'''

def p_Color(p):
		'''Color : Contorno Color2
		| Relleno'''

def p_Color2(p):
		'''Color2 : Relleno
		| vacia'''
				
def p_Cuadrado(p):
		'''Cuadrado : CUAD AP Exp C Exp CP PC'''

def p_Circulo(p):
		'''Circulo : CIRC AP Exp C Exp CP PC'''

def p_Arco(p):
		'''Arco : ARC AP Exp C Exp CP PC'''

def p_Triangulo(p):
		'''Triangulo : TRIAN AP Exp C Exp C Exp C Exp C Exp C Exp CP PC'''

def p_Poligono(p):
		'''Poligono : POLI AP Exp C Exp CP PC'''

def p_Linea(p):
		'''Linea : LIN AP Exp C Exp CP PC'''

def p_Contorno(p):
		'''Contorno : CONTORNO AP Exp C Exp C Exp CP PC'''
		avail.append_quad_tres(302)

def p_Relleno(p):
		'''Relleno : RELLENO AP Exp C Exp C Exp CP PC'''
		avail.append_quad_tres(303)

def p_Texto(p):
		'''Texto : TEXTO AP Exp CP PC'''

def p_Grosor(p):
		'''Grosor : GROSOR AP Exp CP PC'''
		avail.append_quad_uno(301)

def p_Posicion(p):
		'''Posicion : XY AP Exp C Exp CP PC'''
		avail.append_quad_dos(307)

def p_Rotacion(p):
		'''Rotacion : ROTACION AP Exp CP PC'''
#objeto------------------------------------------------------

def p_vacia(p):
		'''vacia : '''
		global vacia
		vacia = True

def guarda_var(var):
		global tipoVar
		if var in hashT:
			print "Variable existe ", var
			sys.exit(0)
		else:
			if tipoVar == "entero":
				global entero_val
				hashT[var] = [tipoVar, "var", entero_val]
				entero_val += 1
			else:
				global float_val
				hashT[var] = [tipoVar, "var", float_val]
				float_val += 1

def dir_bloque(dictB, bloque):
		for i in dictB:
				inf = dictB[i]
				inf[2] = inf[2] + (bloque * 10000)
				dictB[i] = inf
				
def vars_declaradas(p):
		global tipoVar
		if(p != None):
			if(p not in hashT):
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
				tipoVar = hashT[p][0]

def tipo_variable(p, tipov):
		if p in hashT:
				return hashT[p][0]
		else:
				if "globales" in direc:
					return direc["globales"][0][p][0]

def dir_var(p):
		if p in hashT:
			return hashT[p][2]
		else:
			if "globales" in direc:
				return direc["globales"][0][p][2]

def dm(p):
		if p in hashT:
				try:
						return hashT[p][3]
				except IndexError:
						return -1
		else:
				if "globales" in direc:
					try:
							return direc["globales"][0][p][3]
					except IndexError:
							return -1

def cuad_a_arch():
		global aArch
		cuads = avail.get_cuads()
		for c in cuads:
				aArch += str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + " " + str(c[3]) + " " + '\n'
									
def dic_a_str(dictC):
		st = ''
		for i in dictC:
				inf = dictC[i]
				if(i == 'princ' or i == 'globales'):
						st += str(i) + ' ' + str(inf[0]) + ' ' + str(inf[1]) + ' ' + str(inf[2]) + ' ' + str(inf[3]) + ' ' + str(inf[4]) + ' ' + str(inf[5]) + ' ' + str(inf[6]) + '\n'
				else:
						st += str(i) + ' ' + str(inf[2]) + ' ' + str(inf[3]) + ' ' + str(inf[4]) + ' ' + str(inf[5]) + ' ' + str(inf[6]) + ' ' + str(inf[7]) + ' ' + str(inf[8]) + '\n'
		st += '%%' + '\n'
		return st

def dic_a_str_cons(dictC):
		st = ''
		for i in dictC:
			inf = dictC[i]
			st += str(i) + ' ' + str(inf) + '\n'
		st += '%%' + '\n'
		return st

def agr():
		global cnst_entero_cnt
		if 1 not in cnst:
			cnst['1'] = cnst_entero_cnt
			cnst_entero_cnt += 1
		if 0 not in cnst:		
			cnst['0'] = cnst_entero_cnt
			cnst_entero_cnt += 1
		if 2 not in cnst:		
			cnst['2'] = cnst_entero_cnt
			cnst_entero_cnt += 1
			
def p_error(p):
		print "Syntax error en entrada!", p.tipo
					
parser = yacc.yacc()

#930949