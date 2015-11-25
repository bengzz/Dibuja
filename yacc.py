import ply.yacc as yacc
import lex 
import sys
import re

from pila import Pila
from avail import avail

tokens = lex.tokens
hashT = dict()
funT = dict()
TipoV = None
TipoA = None
direc = dict()
cnst = dict()
idF = None
avail = avail()
CHF = [] 
aArch = ''
entero_val = 2000
float_val = 3000
void_val = 1000
cnst_entero_cnt = 40000
cnst_float_cnt = 41002
cnst_void_cnt = 42000
vacia = False
vD = 0
#offset
#ID
DimM = False
DirT = False
DirQty = False
apuntador = False
apuntadorD = 0
contadorP = 0

#Programa------------------------------------------------------
def p_prog(p):
		'''prog : PR prog1 princ locales AC Bloque CC'''
		mtemp = [(void_val-1000), (entero_val-2000), (float_val-3000)]
		mtemp.extend(avail.get_temp_dir())
		direc["princ"] = temp
		if("globales" in direc):
				mtemp = direc["globales"]
				mtemp.pop(0)
				direc["globales"] = mtemp
		cuads = ['ENDPROG', -1, -1, -1]
		avail.append_quad(cuads)

def p_princ(p):
		'''princ : PRINC'''
		avail.princ_goto()
		avail.setBloque(2)
		
def p_locales(p):
		'''locales : var'''
		bloque_dir(hashT, 2)
				
def p_prog1(p):
		'''prog1 : prog2 prog3''' 

def p_prog2(p):
		'''prog2 : globales'''
		avail.princ()
		
def p_prog3(p):
		'''prog3 : Funciones prog3
		| vacia'''
		
def p_globales(p):
		'''globales : glob var
		| vacia'''
		global entero_val, float_val, void_val
		bloque_dir(hashT, 1)
		dvDict = dict(hashT)
		mtemp = [dvDict, (void_val-1000), (entero_val-2000), (float_val-3000)]
		mtemp.extend(avail.get_temp_dir())
		direc["globales"] = mtemp
		hashT.clear()
		entero_val = 2000
		float_val = 3000
		void_val = 1000
		
def p_glob(p):
		'''glob : GL'''
		avail.setBloque(1)
#Programa------------------------------------------------------

#Funciones------------------------------------------------------
def p_Funciones(p):
		'''Funciones : Fun1 varFunciones funciones'''
		mtemp = avail.get_temp_dir()
		direc[avail.getAlcance()][5] = mtemp[0]
		direc[avail.getAlcance()][6] = mtemp[1]
		direc[avail.getAlcance()][7] = mtemp[2]
		direc[avail.getAlcance()][8] = mtemp[3]
		hashT.clear()
		avail.funcion_end()

def p_varFunciones(p):
		'''varFunciones : var'''
		bloque_dir(hashT, 3)
		global entero_val, float_val, void_val, idF
		direc[idF][2] = (void_val-1000)
		direc[idF][3] = (entero_val-2000)
		direc[idF][4] = (float_val-3000)
		void_val = 1000
		entero_val = 2000
		float_val = 3000
				
def p_Fun1(p):
		'''Fun1 : fBloque fID AP func CP'''
		DictV = dict(funT)
		global entero_val, float_val, void_val, contadorP, idF
		idF = avail.getAlcance()
		mtemp = [DictV, avail.getFuncQ(), (void_val-1000), (entero_val-2000), (float_val-3000), 0, 0, 0, 0]
		direc[avail.getAlcance()] = mtemp
		cant = direc["globales"][3]+1
		direc["globales"][0][avail.getAlcance()] = ["flotante", 'func', 13000 + cant]
		direc["globales"][3] = cant
		funT.clear()
		contadorP = 0
		
def p_fID(p):
		'''fID : ID'''
		avail.setAlcance(p[1])
		
def p_fBloque(p):
		'''fBloque : FUNCION FTipo'''
		avail.setFuncQ()
		avail.setBloque(3)

def p_FTipo(p):
		'''FTipo : VOID
		| Tipo'''
		global TipoV
		if(p[1] == 'void'):
				TipoV = p[1]
		avail.setTR(TipoV)

def p_func(p):
		'''func : func1 func2
		| vacia'''
				
def p_func2(p):
		'''func2 : C func1 func2
		| vacia'''
				
def p_func1(p):
		'''func1 : Tipo arreglo fID arrD'''
		global apuntador, apuntadorD, contadorP
		if apuntador:
				pD = avail.get_temp_punto()
				if p[3] in hashT:
						print "Variable ya existe, ", p[3]
						sys.exit(0)
				else:
						hashT[[3]] = [TipoA, "punto", (pD - 30000)]
						if apuntadorD > 0:
									hashT[p[3]].append(apuntadorD)
						apuntador = False
		else:
				guarda_var(p[3])
		funT[p[3]] = [TipoV, contadorP, (hashT[p[3]][2]+30000)]
		contador += 1

def p_arreglo(p):
		'''arreglo : P
		| vacia'''
		global apuntador
		if p[1] == '&':
				apuntador = True
		else:
				apuntador = False

def p_arrD(p):
		'''arrD : AC Exp CC
		| vacia'''
		if len(p) > 2:
				global apuntadorD
				ex = avail.OPila_pop()
				for v, vD in cnst.iteritems():
						if ex == vD:
								apuntadorD = v

def p_funciones(p):
		'''funciones : AC Bloque func3 CC'''
										
def p_func3(p):
		'''func3 : REGRESA Regresar PC'''

def p_Regresar(p):
		'''Regresar : Exp
		| vacia'''
		global vacia, TipoV
		avail.funcion_return(vacia, dir_var(avail.getAlcance()))
		vacia = False
#Funciones------------------------------------------------------

#Variables------------------------------------------------------
def p_var(p):
		'''var : V var11'''
		
def p_var11(p):
		'''var11 : Tipo var1 PC var11
		| vacia'''
		
def p_var1(p):
		'''var1 : varSalvar var2 var23 var3'''

def p_var3(p):
		'''var3 : C varSalvar var2 var23 var3
		| vacia'''
		
def p_varSalvar(p):
		'''varSalvar : ID'''
		guarda_var(p[1])
		global vD
		vD = dir_var(p[1]) + (avail.getBloque() * 10000)
		avail.IDPila_push(p[1])
		
def p_var23(p):
		'''var23 : IG var4
		| vacia'''
		if(len(p) < 3):
			avail.DPila_pop(False)
			
def p_var2(p):
		'''var2 : AC var21
		| vacia'''
		if(len(p) < 3):
			avail.DPila_push(False)

def p_var4(p):
	'''var4 : Exp
	| AC Exp var41 CC'''
	global vD, TipoV, DirQty
	if len(p) == 2:
		if(avail.OPila_peek() < 10000):
			dV = avail.OPila_pop() + (avail.getBloque() * 10000)
			avail.OPila_push(dV)
		avail.asign(vD)
	elif(len(p) == 5):
		if(avail.DPila_pop()):
			ID = avail.IDPila_pop()
			vDm = dm(ID)
			while DirQty >= 0:
				avail.dmP(vD, DirQty, vDm)
				DirQty -= 1
			DirQty = 0
		else:
			print "Error de tipos"
			sys.exit(0)
	else:
		if not avail.DPila_pop():
			print "Error de tipos"
			sys.exit(0)
		else:
			ID = avail.IDPila_pop()
			vDm = dm(ID)
			while DirQty >= 0:
				avail.dmTP(vD, DirQty, vDm)
				DirQty -= 1
			DirQty = 0
			
def p_var41(p):
	'''var41 : C Exp var41
	| vacia'''
	if(len(p) > 2):
		global DirQty
		DirQty += 1
	
def p_var21(p):
	'''var21 : Exp CC'''
	global TipoA, entero_val, float_val
	ID = avail.IDPila_pop()
	ex = avail.OPila_pop()
	for v, vD in cnst.iteritems():
		if ex == vD:
			if TipoA == 'entero':
				entero_val += int(v) + 1
			else:
				float_val += int(v) + 1
			hashT[ID].append(v)
	avail.DPila_push(True)
	avail.IDPila_push(ID)
#Variables------------------------------------------------------

#Tipo------------------------------------------------------
def p_Tipo(p):
		'''Tipo : tipo'''
		
def p_tipo(p):
		'''tipo : ENT 
		| FLOT
		| BOOL'''
		global TipoV, TipoA
		TipoV = p[1]
		TipoA = p[1]
#Tipo------------------------------------------------------

#llamada------------------------------------------------------
def p_Llamada(p):
		'''Llamada : faID Llamada1'''

def p_Llamada1(p):
		'''Llamada1 : fEra Llamada2 CP PC'''
		global idF, vacia
		idF = "func"
		if avail.getFuncAlcance() not in direc:
				print "Error, funcion no existe"
				sys.exit(0)
		avail.funcion_param(direc[avail.getFuncAlcance()][0])
		vD = 10000
		cant = direc["globales"][6]
		vD += 6000 + cant
		direc["globales"][6] = cant + 1
		avail.llama_funcion_final(direc.getFuncAlcance()[1], dir_var(getFuncAlcance()), vD)
		vacia = False

def p_fEra(p):
		'''fEra : AP'''
		avail.llama_funcion(avail.getAlcance())
		
def p_Llamada2(p):
		'''Llamada2 : Llamada4 Llamada3
		| vacia'''
				
def p_Llamada3(p):
		'''Llamada3 : C Llamada4 Llamada3
		| vacia'''

def p_Llamada4(p):
		'''Llamada4 : Exp'''
		CHF.append(TipoV)
		
#llamada------------------------------------------------------

#ciclo------------------------------------------------------
def p_Ciclo(p):
		'''Ciclo : Mientras 
		| Para
		| Ciclo1'''

def p_Mientras(p):
		'''Mientras : MIENTRAS AP Expresion CP AC Estatuto aux2 CC'''
		
def p_aux2(p):
		'''aux2 : Estatuto aux2
		| vacia'''

def p_Para(p):
		'''Para : PARA AP fID IG Exp C Expresion C Expresion CP AC Estatuto aux2 CC'''
		
def p_Ciclo1(p):
		'''Ciclo1 : RE Ciclo2 Bloque'''
		avail.rep_salto(cnst['1'], cnst['0'])
		
def p_Ciclo2(p):
		'''Ciclo2 : VarCte
		| ID'''
		if p[1] != None:
			vars_declaradas(p[1])
			avail.TPila_push(tipo_variable(p[1], "var"))
			avail.OPila_push(dir_var(p[1]))
		avail.rep()
			
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
		avail.append_quad_dos(201)

def p_Circulo(p):
		'''Circulo : CIRC AP Exp C Exp CP PC'''
		avail.append_quad_uno(203)

def p_Arco(p):
		'''Arco : ARC AP Exp C Exp CP PC'''
		avail.append_quad_uno(207)

def p_Triangulo(p):
		'''Triangulo : TRIAN AP Exp C Exp C Exp C Exp C Exp C Exp CP PC'''
		avail.append_quad_tres(202)

def p_Poligono(p):
		'''Poligono : POLI AP Exp C Exp CP PC'''
		avail.append_quad_dos(205)

def p_Linea(p):
		'''Linea : LIN AP idL CP PC'''
		avail.append_quad_dos(206)

def p_Contorno(p):
		'''Contorno : CONTORNO AP Exp C Exp C Exp CP PC'''
		avail.append_quad_tres(301)

def p_Relleno(p):
		'''Relleno : RELLENO AP Exp C Exp C Exp CP PC'''
		spC = [209, -1, -1, 1]
		avail.append_quad(spC)
		avail.append_quad_tres(302)

def p_Texto(p):
		'''Texto : TEXTO AP STR CP PC'''
		global void_val, cnst_void_cnt
		su = 1
		inicio = void_val -1000
		sDir = void_val + (avail.getBloque() * 10000)
		w = p[3]
		while su < len(w)-1:
			if w[su] not in cnst:
				cnst[w[s]] = cnst_void_cnt
				cnst_void_cnt += 1
			spC = ['101',  cnst[w[su]], -1, (void_val + (avail.getBloque() * 10000))]
			void_val += 1
			avail.append_quad(spC)
			su += 1
		final = void_val - 1000	-1
		spC = ['208',  sDir , inicio, final]
		avail.append_quad(spC)

def p_Grosor(p):
		'''Grosor : GROSOR AP Exp CP PC'''
		avail.append_quad_uno(304)

def p_Posicion(p):
		'''Posicion : XY AP Exp C Exp CP PC'''
		avail.append_quad_dos(307)

def p_Rotacion(p):
		'''Rotacion : ROTACION AP Exp CP PC'''
		
def p_idL(p):
		'''idL : ID'''
		vars_declaradas(p[1])
		dm = dm(p[1])
		if dm(p[1]) == -1:
			print "dimension error"
			sys.error(0)
		avail.OPila_push(var_dir(p[1]))
		avail.OPila_push(dm)
#objeto------------------------------------------------------

#Expresion------------------------------------------------------
def p_Expresion(p):
		'''Expresion : Exp Expresion2'''

def p_Expresion2(p):
		'''Expresion2 : Expresion3 Exp
		| vacia'''
		avail.expresion()

def p_Expresion3(p):
		'''Expresion3 : ME
		| MA
		| CI
		| CD'''
		avail.PilaOp_push(p[1])
#Expresion------------------------------------------------------

#Exp, termino, factor -------------------------------------------------
def p_Exp(p):
		'''Exp : Termino Exp2'''
		global vacia
		vacia = False

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
		'''Factor3 : VarCte
		| faID Factor5'''
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
		
def p_faID(p):
		'''faID : ID'''
		avail.setFuncAlcance(p[1])
		avail.IDPila_push(p[1])
				
def p_Factor5(p):
		'''Factor5 : AC Exp CC
		| AP Exp CP
		| Llamada1
		| vacia'''
		global vacia
		if(len(p) == 4):
				avail.DPila_push(True)
				if p[1] == '[':
						avail.DPila_push(True)
				else:
						global D
						D = True
						avail.DPila_push(False)
		elif not vacia:
				avail.DPila_push(True)
				avail.DPila_push(False)
		else:
				avail.delFuncAlcance()
				avail.DPila_push(False)
				avail.DPila_push(False)
				
#Exp, termino, factor -------------------------------------------------

#varcte--------------------------------------------------------------------------------------
def p_VarCte(p):
		'''VarCte : VALI
		| VALF
		| STR'''
		r = re.compile('\d+\.\d+')
		if p[1] not in cnst:
				global cnst_entero_cnt, cnst_float_cnt
				if(r.match(p[1])):
					cnst[p[1]] = cnst_float_cnt
					cnst_float_cnt += 1
				else:
					cnst[p[1]] = cnst_entero_cnt
					cnst_entero_cnt += 1
		avail.OPila_push(cnst[p[1]])
		global TipoV
		if(r.match(p[1])):
			TipoV = "flotante"
		else:
			TipoV = "entero"
		avail.TPila_push(TipoV)
#varcte--------------------------------------------------------------------------------------

#asignacion------------------------------------------------------
def p_WDAsignacion(p):
		'''WDAsignacion : faID Factor5 WD2'''
		ID = avail.IDPila_pop()
		if (idF == "asign"):
			TDM = avail.DPila_pop()
			vars_declaradas(ID)
			if(avail.DPila_pop()):
					if(TDM):
						par = avail.OPila_pop()
						par2 = avail.OPila_pop()
						avail.OPila_push(par)
						avail.TPila_push(tipo_variable(ID, "var"))
						avail.OPila_push(var_dir(ID))
						avail.OPila_push(par2)
						avail.dm(dm(ID), avail.OPila_pop())
						avail.asign(avail.OPila_pop())
					else:
						par = avail.OPila_pop()
						par2 = avail.OPila_pop()
						par3 = avail.OPila_pop()
						avail.OPila_push(par)
						avail.OPila_push(par2)
						avail.TPila_push(tipo_variable(ID, "var"))
						avail.OPila_push(dir_var(ID))
						avail.OPila_push(par3)
						avail.dimT(dm(ID), avail.OPila_pop())
						avail.asigna(avail.OPila_pop())
						avail.asigna(avail.OPila_pop())
			else:
					avail.asigna(dir_var(ID))
		else:
			if(ID not in direc):
					print "Funcion no declarada", ID
					sys.exit(0)
			else:
					if((len(direc[ID][0]) != len(CHF))):
						print "Error de llamada de funcion", ID
						sys.error(0)
					else:
						cont = 0
						for i in direc[ID][0]:
							if(direc[ID][0][i][0] != CHF[cont]):
								print "Error de tipo de llamada de funcion"
								sys.error(0)
							cont += 1
		CHF[:] = []

def p_WD2(p):
		'''WD2 : Asignacion
		| PC'''		
						
def p_Asignacion(p):
		'''Asignacion : IG Asignacion2'''
		global idF
		idF = "asign"
		
def p_Asignacion2(p):
		'''Asignacion2 : Exp PC
		| listaAsig'''
		
def p_listaAsig(p):
		'''listaAsig : AC Exp C Exp CC PC'''
		global DirT
		if(not DirT):
			print "Error de Dimension"
			sys.error(0)
		else:
			DirT = False
#asignacion------------------------------------------------------

#condicion------------------------------------------------------
def p_Condicion(p):
		'''Condicion : SI AP Expresion CondicionCP Bloque Condicion2'''
		avail.condicion_inicio()

def p_CondicionCP(p):
		'''CondicionCP : CP'''
		avail.condicion()
		
def p_Condicion2(p):
		'''Condicion2 : vacia
		| Condicion3 Bloque'''

def p_Condicion3(p):
		'''Condicion3 : SINO'''
		avail.condicion_else()
#condicion------------------------------------------------------

#Bloque------------------------------------------------------
def p_Bloque(p):
		'''Bloque : Estatuto b3'''
		
def p_b3(p):
		'''b3 : Estatuto b3
		| vacia'''	
#Bloque------------------------------------------------------

#Estatuto------------------------------------------------------
def p_Estatuto(p):
		'''Estatuto : WDAsignacion 
		| Condicion 
		| Ciclo 
		| Llamada
		| Objeto'''
#Estatuto------------------------------------------------------

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
		print "Syntax error en entrada!", p.type
					
parser = yacc.yacc()

if(len(sys.argv) > 1):
	archivo = open(sys.argv[1], "r")
	agr()
	l = archivo.readlines()
	acumulador = ""
	for linea in l:
		acumulador += linea
	resultado = parser.parse(acumulador)
	aArch += str(cnst_entero_cnt - 40000) + " " + str(cnst_float_cnt - 41000) + " " + str(cnst_void_cnt - 42000) + '\n'
	aArch += str(dic_a_str_cons(cnst))
	aArch += str(dic_a_str(cnst))
	cuad_a_arch()
	wF = open('program.txt', 'w+')
	wF.write(aArch)
	wF.close()
else:
	print "No se compilo correctamente"