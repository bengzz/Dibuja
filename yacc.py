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
flotante_val = 3000
void_val = 1000
cnst_entero_val = 40000
cnst_flotante_val = 41002
cnst_void_val = 42000
vacia = False
vD = 0
ID = ''
DimM = False
DT = False
DirQty = 0
apuntador = False
apuntadorD = 0
contadoCP = 0

#Programa------------------------------------------------------------
def p_prog(p):
	'''prog : PROG prog1 princ AC locales Bloque CC'''
	temp = [(void_val-1000), (entero_val-2000), (flotante_val-3000)]
	temp.extend(avail.get_temporal_dirs())
	direc["princ"] = temp
	if("globales" in direc):
		temp = direc["globales"]
		temp.pop(0)
		direc["globales"] = temp
	sC = ['ENDPROG', -1, -1, -1]
	avail.append_quad(sC)

def p_princ(p):
	'''princ : PRINC '''
	avail.princ_goto()
	avail.setBloque(2)

def p_locales(p):
	'''locales : var'''
	Bloque_dir(hashT, 2)
	
def p_prog1(p):
	'''prog1 : prog2 prog3'''

def p_prog2(p):
	'''prog2 : globales'''
	avail.princ()

def p_prog3(p):
	'''prog3 : Funciones prog3
| vacia'''
#Programa------------------------------------------------------------

#Funciones------------------------------------------------------------
def p_Funciones(p): 
	'''Funciones : Fun1 varFunciones Bloque'''	
	temps = avail.get_temporal_dirs()
	direc[avail.getalcance()][5] = temps[0]
	direc[avail.getalcance()][6] = temps[1]
	direc[avail.getalcance()][7] = temps[2]
	direc[avail.getalcance()][8] = temps[3]
	hashT.clear()
	avail.function_end()
	
def p_Fun1(p):
        '''Fun1 : fBloque fID AP func CP'''
	vaDict = dict(funT)
	global void_val, entero_val, flotante_val, idF, contadoCP
	idF = avail.getalcance()
	temp = [vaDict, avail.getfuncCuad(), (void_val-2000), (entero_val-2000), (flotante_val-3000), 0, 0, 0, 0]
	direc[avail.getalcance()] = temp
	qty = direc["globales"][3] + 1
	direc["globales"][0][avail.getalcance()] = ["flotante", 'func', 13000 + qty]
	direc["globales"][3] = qty
	#print direc["globales"]
	funT.clear()
	contadoCP = 0

def p_fID(p):
	'''fID : ID '''
	avail.setalcance(p[1])

def p_fBloque(p):
        '''fBloque : FUNCION FTipo'''
	avail.setfuncCuad()
	avail.setBloque(3)

def p_FTipo(p):
        '''FTipo : VOID 
		| tipo'''
	global TipoV
	if(p[1] == 'void'):
		TipoV = p[1]
	avail.setRT(TipoV)

def p_func(p):
	'''func : fun1 fun2
| vacia'''

def p_fun2(p):
	'''fun2 : C fun1 fun2  
| vacia'''

def p_fun1(p):
	'''fun1 : tipo arreglo ID arrD'''
	global apuntador, apuntadorD, contadoCP
	if apuntador:
		pDir = avail.get_temporal_point()
		if p[3] in hashT:
			print "Existing var, ", p[3]
			sys.exit(0)
		else:
			hashT[p[3]] = [TipoA, "point", (pDir-30000)]
			if apuntadorD > 0:
				hashT[p[3]].append(apuntadorD)
		apuntador = False
	else:
		guardar_var(p[3])
	funT[p[3]] = [TipoV, contadoCP, (hashT[p[3]][2]+30000)]
	contadoCP += 1

def p_arr(p):
	'''arreglo : APN
| vacia '''
	global apuntador
	if p[1] == '&':
		apuntador = True
	else:
		apuntador = False	

def p_arrD(p):
	'''arrD : AC exp CC 
| vacia'''
	if len(p) > 2:
		global apuntadorD
		exp = avail.OPila_pop()
		for value, vDir in cnst.iteritems():
			if exp == vDir :
				apuntadorD = value
	
#Funciones------------------------------------------------------------

#Regresar------------------------------------------------------------
def p_Regresar(p):	
	'''Regresar : RT Regresar2 PC'''
	if(avail.getalcance() == 'princ'):
			print "ERROR, no return in main"
			sys.exit(0)
			
def p_Regresar2(p):
	'''Regresar2 : exp 
	| vacia'''
	global vacia, TipoV
	avail.funcion_return(vacia, dir_var(avail.getalcance()))
	vacia = False
#Regresar------------------------------------------------------------

#Bloque------------------------------------------------------------
def p_Bloque(p):
	'''Bloque : LB Bloque3 RB'''

def p_Bloque3(p):
	'''Bloque3 : Estatuto Bloque3
| vacia '''
#Bloque------------------------------------------------------------

#Variables------------------------------------------------------------
def p_globales(p):
	'''globales : glob var
| vacia'''
	global void_val, entero_val, flotante_val
	Bloque_dir(hashT, 1)
	vaDict = dict(hashT)
	temp = [vaDict, (void_val-1000), (entero_val-2000), (flotante_val-3000)]
	temp.extend(avail.get_temporal_dirs())
	direc["globales"] = temp
	hashT.clear()
	void_val = 1000
	entero_val = 2000
	flotante_val = 3000

def p_glob(p):
	'''glob : GL'''
	avail.setBloque(1)

def p_varFunciones(p):
	'''varFunciones : var '''
	Bloque_dir(hashT, 3)
	global void_val, entero_val, flotante_val, idF
	direc[idF][2] = (void_val-1000)
	direc[idF][3] = (entero_val-2000)
	direc[idF][4] = (flotante_val-3000)
	void_val = 1000
	entero_val = 2000
	flotante_val = 3000
		
def p_var(p): 
	'''var : V var11 
| vacia'''

def p_var11(p):
        '''var11 : tipo var1 PC var11
| vacia'''

def p_var1(p):
	'''var1 : varSalvar var2 var23 var3 '''

def p_var3(p):
	'''var3 : C varSalvar var2 var23 var3 
| vacia '''

def p_varSalvar(p):
	'''varSalvar : ID '''
	guardar_var(p[1])
	global vD
	vD = dir_var(p[1]) + (avail.getBloque() * 10000)
	avail.IDPila_push(p[1])

def p_var23(p):
        '''var23 : IG var4 
| vacia'''
	if len(p) != 3:
		avail.DPila_pop()

def p_var2(p):
	'''var2 : AC var21
| LB var22
| vacia'''
	if(len(p) < 3):
		avail.DPila_push(False)

def p_var4(p):
	'''var4 : exp
| LB AP exp C exp CP var41 RB
| AC exp var42 CC'''
	global vD, TipoV, DirQty
	if len(p) == 2: 
		if(avail.OPila_peek() < 10000):
			dV = avail.OPila_pop() + (avail.getBloque() * 10000)
			avail.OPila_push(dV)
		avail.asign(vD)
	elif(len(p) == 5):
	#array
		if(avail.DPila_pop()):
			ID = avail.IDPila_pop()
			vDim = dim(ID)
			while DirQty >= 0 :
				avail.dmP(vD, DirQty, vDim)
				DirQty -= 1
			DirQty = 0
		else:
			print "error de tipos"
			sys.exit(0)
	else:
		if not avail.DPila_pop():
			print "error de tipos"
			sys.exit(0)
		else:
			ID = avail.IDPila_pop()
			vDim = dim(ID)
			while DirQty >= 0:
				avail.dmTP(vD, DirQty, vDim)
				DirQty -= 1
			DirQty = 0
			

def p_var41(p):
	'''var41 : C AP exp C exp CP var41
| vacia'''
	if(len(p) > 2):
		global DirQty
		DirQty += 1

def p_var42(p):
	'''var42 : C exp var42
| vacia'''
	if(len(p) > 2):
		global DirQty
		DirQty += 1

def p_var21(p):
	'''var21 : exp CC '''
	global TipoA, entero_val, flotante_val
	ID = avail.IDPila_pop()
	exp = avail.OPila_pop()
	for value, vDir in cnst.iteritems():
		if exp == vDir :
			if TipoA == 'entero':
				entero_val += int(value) + 1
			else:
				flotante_val += int(value) + 1
			hashT[ID].append(value)
	avail.DPila_push(True)
	avail.IDPila_push(ID)
	
def p_var22(p):
	'''var22 : exp RB'''
	global TipoA, entero_val, flotante_val
	ID = avail.IDPila_pop()
	exp = avail.OPila_pop()
	for value, vDir in cnst.iteritems():
		if exp == vDir :
			if TipoA == 'entero':
				entero_val += (int(value)+1)*2 
			else:
				flotante_val += (int(value)+1)*2 
			hashT[ID].append((int(value)+1)*2 )
	avail.DPila_push(True)
	avail.IDPila_push(ID)
				
#Variables------------------------------------------------------------

#Estatuto------------------------------------------------------------
def p_Estatuto(p):
	'''Estatuto : Objeto 
	| Condicion 
	| Asignacion
	| Ciclo
	| Regresar'''
#Estatuto------------------------------------------------------------

#Tipo----------------------------------------------------------------

def p_tipo(p):
	'''tipo : ENT 
| FLOT  '''
	global TipoV, TipoA
	TipoV = p[1]
	TipoA = p[1]

#Tipo----------------------------------------------------------------

#Expresion----------------------------------------------------------------
def p_expresion(p):
	'''expresion : exp ex2 '''

def p_ex2(p):
	'''ex2 : ex3 exp 
| vacia'''
	avail.expresion()

def p_ex3(p):
	'''ex3 : ME 
| MA 
| CD 
| CI
| LTH
| MTH'''
	avail.OpPila_push(p[1])
#Expresion----------------------------------------------------------------

#exp----------------------------------------------------------------

def p_exp(p):
	'''exp : Termino exprog2'''
	global vacia
	vacia = False

def p_exprog2(p):
	'''exprog2 : exp4 exprog3 exp 
| exp4 vacia'''

def p_exp4(p):
	'''exp4 : vacia'''
	avail.sum_res()

def p_exprog3(p):
	'''exprog3 : SUM 
| RES'''
	avail.OpPila_push(p[1])
#exp----------------------------------------------------------------

#Termino----------------------------------------------------------------
def p_Termino(p):
	'''Termino : Factor Termino2'''	

def p_Termino2(p):
	'''Termino2 : Termino4 Termino3 Termino 
| Termino4 vacia'''	

def p_Termino4(p):
	'''Termino4 : vacia'''
	avail.mult_div()	

def p_Termino3(p):
	'''Termino3 : MUL 
| DIV'''
	avail.OpPila_push(p[1])
#Termino----------------------------------------------------------------

#Factor----------------------------------------------------------------
def p_Factor(p):
	'''Factor : Factor2 exp CP 
| Factor4'''
	if(len(p) == 4):
		avail.OpPila_pop()

def p_Factor2(p):
	'''Factor2 : AP '''
	avail.OpPila_push(p[1])

def p_Factor4(p):
	'''Factor4 : varCte
| faID Factor5'''
	if(len(p) == 3):
		ID = avail.IDPila_pop()
		DimM = avail.DPila_pop()
		if(DimM):		
			apuntador = avail.OPila_pop()
		variables_declaradas(ID)
		avail.TPila_push(tipo_variable(ID, "var"))
		avail.OPila_push(dir_var(ID))
		if(DimM):
			avail.dim(dim(ID), apuntador)
		if not DimM:
			if avail.DPila_pop():
				avail.OPila_pop()
				avail.TPila_pop()
				

def p_faID(p):
	'''faID : ID '''
	avail.setFuncalcance(p[1])
	avail.IDPila_push(p[1])

def p_Factor5(p):
	'''Factor5 : AC exp CC
| LB exp RB
| Llamada
| vacia'''
	global vacia	
	if(len(p) == 4):
		avail.DPila_push(True)
		if p[1] == '[':
			avail.DPila_push(True)
		else:
			global DT
			DT = True
			avail.DPila_push(False)
	elif not vacia:
		avail.DPila_push(True)
		avail.DPila_push(False)
	else:
		avail.delFuncalcance()
		avail.DPila_push(False)
		avail.DPila_push(False)
#Factor----------------------------------------------------------------

#varCte----------------------------------------------------------------

def p_varCte(p):
	'''varCte : VALI 
| VALF  '''
	a = re.compile('\d+\.\d+')
	if p[1] not in cnst:
		global cnst_entero_val, cnst_flotante_val
		if(a.match(p[1])):
			cnst[p[1]] = cnst_flotante_val
			cnst_flotante_val += 1
		else:
			cnst[p[1]] = cnst_entero_val
			cnst_entero_val += 1
	avail.OPila_push(cnst[p[1]])
	global TipoV
	if(a.match(p[1])):
		TipoV = "flotante"
	else:
		TipoV = "entero"
	avail.TPila_push(TipoV)

#varCte----------------------------------------------------------------

#Condicion------------------------------------------------------------
def p_Condicion(p):
	'''Condicion : SI AP expresion condicion2 Bloque condicion3'''
	avail.condicion_inicio()

def p_condicion2(p):
	'''condicion2 : CP'''
	avail.condicion()
				

def p_condicion3(p):
	'''condicion3 : vacia  
| con3 Bloque'''

def p_con3(p):
	'''con3 : SINO '''
	avail.condition_else()
#Condicion------------------------------------------------------------

#Asignacion------------------------------------------------------------
def p_Asignacion2(p):
	'''Asignacion2 : Asigna
| PC'''

def p_Asigna(p):
	'''Asigna : IG AsignaT'''
	global idF
	idF = "asig"

def p_AsignaT(p):
	'''AsignaT : exp PC
| lAsigna '''

def p_Asignacion(p):
	'''Asignacion : faID Factor5 Asignacion2'''
	ID = avail.IDPila_pop()
	if(idF == "asig"):
		TDim = avail.DPila_pop()		
		variables_declaradas(ID)
		if(avail.DPila_pop()):
			if(TDim):
				par = avail.OPila_pop()
				par2 = avail.OPila_pop()
				avail.OPila_push(par)
				avail.TPila_push(tipo_variable(ID, "var"))
				avail.OPila_push(dir_var(ID))
				avail.OPila_push(par2)
				avail.dim(dim(ID), avail.OPila_pop())
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
				avail.dmT(dim(ID), avail.OPila_pop())
				avail.asign(avail.OPila_pop())
				avail.asign(avail.OPila_pop())
		else:
			avail.asign(dir_var(ID))
	else:
		if(ID not in direc):
			print "Funcion no declarada", ID
			sys.exit(0)	
		else:
			if((len(direc[ID][0])) != len(CHF)):
				print "Error de llamada de funcion, ", ID
				sys.error(0)
			else:
				cont = 0
				for key in direc[ID][0]:
					if(direc[ID][0][key][0] != CHF[cont]):
						
						print "Error de tipo de llamada de funcion"
						sys.error(0)
					cont += 1 
	CHF[:] = []
#Asignacion------------------------------------------------------------

#Llamada------------------------------------------------------------
def p_Llamada(p):
	'''Llamada : funEra func2 CP '''
	global idF, vacia
	idF = "func"
	if avail.getFuncalcance() not in direc:
		print "Error, function doesn't exist"
		sys.exit(0)
	avail.function_param(direc[avail.getFuncalcance()][0])
	vDir = 10000
	qty = direc["globales"][6]
	vDir += 6000 + qty
	direc["globales"][6] = qty + 1
	avail.llama_funcion_final(direc[avail.getFuncalcance()][1], dir_var(avail.getFuncalcance()), vDir)
	vacia = False

def p_funEra(p):
	'''funEra : AP '''
	avail.llama_funcion(avail.getalcance())

def p_func2(p):
	'''func2 : func4 func3
| vacia'''

def p_func3(p):
	'''func3 : C func4 func3
| vacia'''

def p_func4(p):
	'''func4 : exp '''
	CHF.append(TipoV)
	
def p_lAsigna(p):
	'''lAsigna : LB exp C exp RB PC'''
	global DT
	if(not DT):
		print "Dimension error"
		sys.error(0)
	else:
		DT = False
#Llamada------------------------------------------------------------

#Ciclo----------------------------------------------------------------

def p_Ciclo(p):
	'''Ciclo : RE Cicloprog3 Bloque'''
	avail.rep_salto(cnst['1'], cnst['0'])

def p_Cicloprog3(p):
	'''Cicloprog3 : varCte
| ID'''
	if p[1] != None:
		variables_declaradas(p[1])
		avail.TPila_push(tipo_variable(p[1], "var"))
		avail.OPila_push(dir_var(p[1]))
	avail.rep()
#Ciclo----------------------------------------------------------------

#Objeto----------------------------------------------------------------
def p_Objeto(p):
	'''Objeto : Figura
	| Color
	| Posicion
	| Grosor'''
		
		
def p_Figura(p):
	'''Figura : Rectangulo
	| Triangulo
	| Poligono
	| Linea
	| CUADCIR
	| Arco
	| Texto'''
	
def p_Posicion(p):
	'''Posicion : XY AP exp C exp CP PC'''
	avail.append_quad_dos(307)

def p_Color(p):
	'''Color : CONTORNO AP exp C exp C exp CP PC 
| RELLENO AP exp C exp C exp CP PC'''
	if(p[1] == 'contorno'):
		fond = 301
	elif(p[1] == 'relleno'):
		fond = 302
	avail.append_quad_tres(fond)

def p_Grosor(p):
	'''Grosor : GROSOR AP exp CP PC '''
	avail.append_quad_uno(304)

def p_Rectangulo(p):
	'''Rectangulo : REC AP exp C exp fondo CP PC'''
	avail.append_quad_dos(201)

def p_fondo(p):
	'''fondo : C Fondo 
| vacia'''
	if(len(p) == 3):
		sC = [209, -1, -1, 1]
	else:
		sC = [209, -1, -1, -1]
	avail.append_quad(sC)

def p_Triangulo(p):
	'''Triangulo : TRI AP AC exp C exp CC C AC exp C exp CC C AC exp C exp CC fondo CP PC'''
	avail.append_quad_tri(202)

def p_CUADCIR(p):
	'''CUADCIR : CIR AP exp fondo CP PC
| SQ AP exp fondo CP PC'''
	if(p[1] == 'circulo'):
		sC = 203
	else:
		sC = 204
	avail.append_quad_uno(sC)

def p_Poligono(p):
	'''Poligono : POL AP idList fondo CP PC'''
	avail.append_quad_dos(205)

def p_Linea(p):
	'''Linea : LS AP idList CP PC'''
	avail.append_quad_dos(206)

def p_idList(p):
	'''idList : ID'''
	variables_declaradas(p[1])
	dimention = dim(p[1])
	if dim(p[1]) == -1:
		print "dimension error"
		sys.error(0)
	avail.OPila_push(dir_var(p[1]))
	avail.OPila_push(dimention)

def p_Arco(p):
	'''Arco : ARC AP exp fondo CP PC'''
	avail.append_quad_uno(207)

def p_Texto(p):
	'''Texto : LA AP STR CP PC'''
	global void_val, cnst_void_val
	sub = 1
	start = void_val - 1000
	strDir = void_val + (avail.getBloque() * 10000)
	word = p[3]
	while sub < len(word)-1:
		if word[sub] not in cnst:
			cnst[word[sub]] = cnst_void_val
			cnst_void_val += 1
		sC = ['101',  cnst[word[sub]], -1, (void_val + (avail.getBloque() * 10000))]
		void_val += 1
		avail.append_quad(sC)
		sub += 1
	finish = void_val - 1000	-1
	sC = ['208',  strDir , start, finish]
	avail.append_quad(sC)
#Objeto----------------------------------------------------------------
	
def p_vacia(p):
	'''vacia : '''
	global vacia
	vacia = True

def guardar_var(var):
	global TipoA
	if var in hashT:
		print "Existing var, ", var
		sys.exit(0)
	else:
		if TipoA == "entero":
			global entero_val
			hashT[var] = [TipoA, "var", entero_val]
			entero_val += 1 
		else:
			global flotante_val
			hashT[var] = [TipoA, "var", flotante_val] 
			flotante_val += 1

def Bloque_dir(BloqueDict, Bloque):
	for key in BloqueDict:
		info = BloqueDict[key]
		info[2] = info[2] + (Bloque * 10000)
		BloqueDict[key] = info

def variables_declaradas(p):
	global TipoV
	if(p != None):
		if(p not in hashT):
			if("globales" in direc):
				if(p not in direc["globales"][0]):
					print "Undeclared variable. ", p
					sys.exit(0)
				else:
					TipoV = direc["globales"][0][p][0]
			else:
				print "Undeclared variable. ", p
				sys.exit(0)
		else:
			TipoV = hashT[p][0]

def tipo_variable(p, tipo_v):
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

def dim(p):
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

def dic_a_str(convDict):
	s = ''
	for key in convDict:
		info = convDict[key]
		if(key == 'princ' or key == 'globales'):
			s += str(key) + ' ' + str(info[0]) + ' ' + str(info[1]) + ' ' + str(info[2]) + ' ' + str(info[3]) + ' ' + str(info[4]) + ' ' + str(info[5]) + ' ' + str(info[6]) + '\n'
		else:
			s += str(key) + ' ' + str(info[2]) + ' ' + str(info[3]) + ' ' + str(info[4]) + ' ' + str(info[5]) + ' ' + str(info[6]) + ' ' + str(info[7]) + ' ' + str(info[8]) + '\n'
	s += '%%' + '\n'
	return s

def dic_a_str_cons(convDict):
	s = ''
	for key in convDict:
		info = convDict[key]
		s += str(key) + ' ' + str(info) + '\n'
	s += '%%' + '\n'
	return s

def cuad_to_file():
	global aArch
	cuad = avail.get_cuad()
	for q in cuad:
		aArch += str(q[0]) + " " + str(q[1]) + " " + str(q[2]) + " " + str(q[3]) + " " + '\n'

def agr():
	global cnst_entero_val
	if 1 not in cnst:
		cnst['1'] = cnst_entero_val
		cnst_entero_val += 1
	if 0 not in cnst:		
		cnst['0'] = cnst_entero_val
		cnst_entero_val += 1
	if 2 not in cnst:		
		cnst['2'] = cnst_entero_val
		cnst_entero_val += 1
def p_error(p):
	print "Error de sintaxis de entrada en:", p.type

parser = yacc.yacc()

if(len(sys.argv) > 1):
    f = open(sys.argv[1], "r")
    agr()
    s = f.readlines()
    string = ""
    for line in s:
        string += line
    result = parser.parse(string)
    aArch += str(cnst_entero_val - 40000) + " " + str(cnst_flotante_val - 41000) + " " + str(cnst_void_val - 42000) + '\n'
    aArch += str(dic_a_str_cons(cnst))
    aArch += str(dic_a_str(direc))
    #print direc
    cuad_to_file()
    #print aArch
    wFile = open('compilado.txt', 'w+')
    wFile.write(aArch)
    wFile.close()
else:
    print "):"
