from pila import Pila
import sys

	
class avail:
	cubo_semantico = None
	
	def __init__(self):
		self.temp_booleano = 4000 
		self.temp_entero = 5000
		self.temp_flotante = 6000
		self.temp_dir = 7000 
		self.Bloque = 0
		self.OPila = Pila() 
		self.TPila = Pila() 
		self.OpPila = Pila() 
		self.salto = Pila()
		self.numCuad = 0
		self.funcCuad = 0
		self.cuad = []
		self.DPila = Pila()
		self.IDPila = Pila()
		self.alcanceF = Pila()
		self.alcance = ''
		self.RT = ''
		self.cubo_semantico = {
		'=': {
			'entero': {
				'entero': 'entero',
				'flotante': 'flotante'
			},
			'flotante': {
				'entero': 'error',
				'flotante': 'flotante'
			}
		},
		'>': {
			'entero': {
				'entero': 'bool',
				'flotante': 'bool'
			},
			'flotante': {
				'entero': 'bool',
				'flotante': 'bool'
			}
		},
		'<': {
			'entero': {
				'entero': 'bool',
				'flotante': 'bool'
			},
			'flotante': {
				'entero': 'bool',
				'flotante': 'bool'
			}
		},
		'>=': {
			'entero': {
				'entero': 'bool',
				'flotante': 'bool'
			},
			'flotante': {
				'entero': 'bool',
				'flotante': 'bool'
			}
		},
		'<=': {
			'entero': {
				'entero': 'bool',
				'flotante': 'bool'
			},
			'flotante': {
				'entero': 'bool',
				'flotante': 'bool'
			}
		},
		'!=': {
			'entero': {
				'entero': 'bool',
				'flotante': 'bool'
			},
			'flotante': {
				'entero': 'bool',
				'flotante': 'bool'
			}
		},
		'==': {
			'entero': {
				'entero': 'bool',
				'flotante': 'bool'
			},
			'flotante': {
				'entero': 'bool',
				'flotante': 'bool'
			}
		},
		'+': {
			'entero': {
				'entero': 'entero',
				'flotante': 'flotante'
			},
			'flotante': {
				'entero': 'flotante',
				'flotante': 'flotante'
			}
		},
		'-': {
			'entero': {
				'entero': 'entero',
				'flotante': 'flotante'
			},
			'flotante': {
				'entero': 'flotante',
				'flotante': 'flotante'
			}
		},
		'*': {
			'entero': {
				'entero': 'entero',
				'flotante': 'flotante'
			},
			'flotante': {
				'entero': 'flotante',
				'flotante': 'flotante'
			}
		},
		'/': {
			'entero': {
				'entero': 'entero',
				'flotante': 'flotante'
			},
			'flotante': {
				'entero': 'flotante',
				'flotante': 'flotante'
			}
		},
		'$': {
			'dir': {
				'-1': 'dir'
			}
		}
	}
	
	#regresa el tipo de la operacion
	def get_tipo(self, argOper, uno, dos): 
		esperado = self.cubo_semantico.get(argOper)
		if esperado != None:
			esperado = esperado.get(uno)
			if esperado != None:
				esperado = esperado.get(dos)
				return esperado
		print 'error'
		
	#se crea un nuevo valor temporal en base al resultado del cubo semantico	
	def get_temporal(self, argOper, uno, dos):
		tempoTipo = self.get_tipo(argOper, uno, dos)
		if tempoTipo == 'entero':
			res = self.temp_entero
			self.temp_entero += 1 
		elif tempoTipo == 'flotante':
			res = self.temp_flotante
			self.temp_flotante += 1
		elif tempoTipo == 'bool':
			res = self.temp_booleano
			self.temp_booleano += 1
		elif uno == 'dir':
			res = self.temp_dir
			self.temp_dir += 1
		res += (self.Bloque * 10000)
		return [res, self.get_tipo(argOper, uno, dos)]

	#regresa el bloque actual
	def getBloque(self):
		return self.Bloque
	
	#resetea la memoria para el siguiente bloque
	def setBloque(self, Bloque):
		self.Bloque = Bloque
		self.temp_booleano = 4000
		self.temp_entero = 5000
		self.temp_flotante = 6000
		self.temp_dir = 7000 
	
	#regresa la memoria necesaria para las temporales
	def get_temporal_dirs(self):
		return [(self.temp_booleano-4000), (self.temp_entero-5000), (self.temp_flotante-6000), (self.temp_dir-7000)]

	#si hay una expresion para resolver
	def expresion(self):
		if(self.OpPila.size() > 0):
			if(self.OpPila.peek() == '>' or self.OpPila.peek() == '<' or self.OpPila.peek() == '!=' or self.OpPila.peek() == '==' or self.OpPila.peek() == '<=' or self.OpPila.peek() == '>='):
				self.quad()

	#si hay una operacion se suma o resta
	def sum_res(self):
		if(self.OpPila.size() > 0):
			if(self.OpPila.peek() == '+' or self.OpPila.peek() == '-'):
				self.quad()

	#si hay una operacion de multiplicacion o division
	def mult_div(self):
		if(self.OpPila.size() > 0):
			if(self.OpPila.peek() == '*' or self.OpPila.peek() == '/'):
				self.quad()

	#crea una asignacion
	def asign(self, dato):
		if(self.OPila.size() > 0):
			self.numCuad += 1
			cuads = [101, self.OPila.pop(), -1, dato]
			self.cuad.append(cuads)
	
	#saca uno de los valores de la temporal 
	def rep_salto(self, primDir, dirInic):
		valT = self.OPila.pop()
		cuads = ['-', valT, primDir, valT]
		self.numCuad += 1
		self.cuad.append(cuads)
		salto = self.salto.pop()
		aux = self.get_temporal('==', self.TPila.pop(), 'entero') 
		cuads = ['==', valT, dirInic, aux[0]]
		self.numCuad += 1
		self.cuad.append(cuads)
	
		cuads = ['GOTOF', aux[0], -1, salto]
		self.numCuad += 1
		self.cuad.append(cuads)

	#al inicio de una condicion se crea un gotof y se almacena el num de cuadruplo en la pila de saltos
	def condicion(self):
		estCondic = self.OPila.pop()
		tipoCondicion = self.TPila.pop()
		if(tipoCondicion != "bool"):
			print "Error, el tipo no coincide"
			sys.error(0)
		else:
			cuads = ['GOTOF', estCondic, -1, -1]
			self.cuad.append(cuads)
			self.numCuad += 1
			self.salto.push(self.numCuad)

	#al final de una condicion llena el ultimo goto que fue creado con el cuadruplo actual
	def condicion_inicio(self):
		if(self.salto.size() > 0):
			salto = self.salto.pop() - 1
			cuads = self.cuad[salto]
			cuads[3] = self.numCuad 
			self.cuad[salto] = cuads

	#si hay un else, se debe llenar el goto del if y crear un nuevo goto
	def condition_else(self):
		salto = self.salto.pop() -1
		cuads = self.cuad[salto]
		cuads[3] = self.numCuad +1
		self.cuad[salto] = cuads
		cuads = ['GOTO', -1, -1, -1]
		self.cuad.append(cuads)
		self.numCuad += 1
		self.salto.push(self.numCuad)
	
	#revisa si la funcion regreso, si no crea un cuadruplo en la pila de operadores
	def funcion_return(self, vacio, valDireccion):
		if(vacio):
			cuads = ['RETURN',-1, -1, -1]
			self.numCuad += 1
			self.cuad.append(cuads)
			return False
		else:
			cuads = ['RETURN', self.OPila.pop(), -1, valDireccion]
			self.numCuad += 1
			self.cuad.append(cuads)
			return True

	#final del cuadruplo
	def function_end(self):
		cuads = ['ENDPROC', 1, -1, 1]
		self.numCuad += 1
		self.cuad.append(cuads)

	#checa los parametros de las funciones de acuerdo al orden
	def function_param(self, varParametro):
		numParams = len(varParametro)
		if self.OPila.size() < numParams:
			print "Faltan paramentros de la funcion"
			sys.exit(0)
		lista = []
		numParams = len(varParametro) -1		
		while numParams >= 0:
			for key in varParametro:
				if numParams == varParametro[key][1]:
					cuads = ['PARAMETRO', self.OPila.pop(), -1, varParametro[key][2]]
					print cuads
					numParams -= 1
					self.numCuad += 1
					self.cuad.append(cuads)

	#cuadruplo que contiene el nombre de la funcion la cual se esta llamando
	def llama_funcion(self, param):
		cuads = ['ERA', -1, -1, param]
		self.numCuad += 1
		self.cuad.append(cuads)
		self.OpPila.push('(')

	#se hace un go sub a la funcion de la gual se hizo el go, se hace una asignacion en caso de que se regrese un valor en una temporal
	def llama_funcion_final(self,param, valDire, valTempo):
		cuads = ['GOSUB', -1, -1, param]
		self.numCuad += 1
		self.cuad.append(cuads)
		cuads = ['101', valDire, -1, valTempo]
		self.OPila.push(valTempo)
		self.numCuad += 1
		self.cuad.append(cuads)
		self.OpPila.pop()
	
	#crea una copia del numero que representa las veces que el bloque fue creado, y almacena el valor en la pila
	def rep(self):
		aux = self.get_temporal('-', self.TPila.peek(), self.TPila.pop()) 
		valT = aux[0]
		cuads = [101, self.OPila.pop(), -1, valT]
		self.numCuad += 1
		self.cuad.append(cuads)
		self.salto.push(self.numCuad)
		self.OPila.push(valT)
		self.TPila.push(aux[1])

	#para los arreglos, crea un cuad que checa que el valor ente en el rango
	def dim(self, tamDim, vapunta):
		cuads = ['DIM', tamDim, vapunta, -1]
		self.numCuad += 1
		self.cuad.append(cuads)
		self.numCuad += 1
		aux = self.get_temporal('$', 'dir', -1) 
		valT = aux[0]
		cuads = ['DIR', self.OPila.pop(), vapunta, valT]
		self.cuad.append(cuads)
		self.OPila.push(valT)
	
	#para las matrices, pointer representa las filas
	def dmT(self, tamDim, vapunta):
		aux = self.get_temporal('+', 'entero', 'entero') 
		valT = aux[0]
		cuads = ['*', vapunta, '40002', valT]
		self.cuad.append(cuads)
		vapunta = valT

		cuads = ['DIM', tamDim, vapunta, -1]
		self.cuad.append(cuads)
		
		aux = self.get_temporal('$', 'dir', -1) 
		valT = aux[0]
		saleRes = self.OPila.pop()
		cuads = ['DIR', saleRes, vapunta, valT]
		uno = valT
		self.cuad.append(cuads)	
		
		aux = self.get_temporal('+', 'entero', 'entero') 
		valT = aux[0]
		cuads = ['+', vapunta, '40000', valT]
		self.cuad.append(cuads)
		self.OPila.push(valT)
		aux = self.get_temporal('$', 'dir', -1) 
		valT = aux[0]
		cuads = ['DIR', saleRes, self.OPila.pop(), valT]
		self.cuad.append(cuads)	
		
		tempo = self.OPila.pop()
		self.OPila.push(valT)
		self.OPila.push(tempo)
		self.OPila.push(uno)
		self.numCuad += 4

	#al inicializar una matriz, revisa la dimension, crea un apuntador para que asigne algo al siguiente valor
	def dmTP(self, valDire, casilla, valTam):
		casilla *= 2
		cuads = ['DIMC', valTam, casilla, -1]
		self.cuad.append(cuads)
		
		aux = self.get_temporal('$', 'dir', -1) 
		valT = aux[0]
		cuads = ['DIRC', valDire, (casilla+1), valT]
		self.cuad.append(cuads)
		self.asign(valT)

		aux = self.get_temporal('$', 'dir', -1) 
		valT = aux[0]
		cuads = ['DIRC', valDire, casilla, valT]
		self.cuad.append(cuads)
		self.asign(valT)

		self.numCuad += 3

	#checa la dimension, obtiene la direccion del puntero, cuad que genera la direccion actual
	def dmP(self, valDire, casilla, valTam):
		cuads = ['DIMC', valTam, casilla, -1]
		self.cuad.append(cuads)
		
		aux = self.get_temporal('$', 'dir', -1) 
		valT = aux[0]
		cuads = ['DIRC', valDire, casilla, valT]
		self.cuad.append(cuads)
		self.asign(valT)

		self.numCuad += 2

	#crea el goto al main, gurda el numero de cuadruplo en la pila de saltos
	def princ(self):
		cuads = ['GOTO', -1, -1, -1]
		self.cuad.append(cuads)
		self.salto.push(self.numCuad)
		self.numCuad += 1

	#hace el goto al programa principal
	def princ_goto(self):
		salto = self.salto.pop()
		cuads = self.cuad[salto]
		cuads[3] = self.numCuad 
		self.cuad[salto] = cuads
	
		
	#concatena los cuadruplos
	def append_quad(self, cuadruplo):
		self.numCuad += 1
		self.cuad.append(cuadruplo)

	#usado por las funciones que solo tienen un parametro
	def append_quad_uno(self, unoFuncion):
		self.numCuad += 1
		cuads = [unoFuncion, self.OPila.pop(), -1, -1]
		self.TPila.pop()
		self.cuad.append(cuads)

	#usado por funciones que tienen dos parametros
	def append_quad_dos(self, dosFuncion):
		self.numCuad += 1
		dosParam = self.OPila.pop()
		self.TPila.pop()
		cuads = [dosFuncion, self.OPila.pop(),dosParam, -1]
		self.TPila.pop()
		self.cuad.append(cuads)

	#usado por funciones con tres parametros
	def append_quad_tres(self, tresFuncion):
		self.numCuad += 1
		uno = self.OPila.pop()
		self.TPila.pop()
		dos = self.OPila.pop()
		self.TPila.pop()
		cuads = [tresFuncion, self.OPila.pop(), dos, uno]
		self.TPila.pop()
		self.cuad.append(cuads)

	#usado por la funcion del triangulo
	def append_quad_tri(self, triaFuncion):
		self.numCuad += 2
		y3 = self.OPila.pop()
		self.TPila.pop()
		x3 = self.OPila.pop()
		self.TPila.pop()
		y2 = self.OPila.pop()
		self.TPila.pop()
		x2 = self.OPila.pop()
		self.TPila.pop()
		y = self.OPila.pop()
		self.TPila.pop()
		x = self.OPila.pop()
		self.TPila.pop()
		spQuad = [triaFuncion, x, y, -1]
		self.cuad.append(spQuad)
		spQuad = [x2, y2, x3, y3]
		self.cuad.append(spQuad)

	#lo utilizan las expresiones para crear cuadruplos
	def quad(self):
		self.numCuad += 1
		aux = self.get_temporal(self.OpPila.peek(), self.TPila.pop(), self.TPila.pop()) 
		valT = aux[0]
		operando2 = self.OPila.pop() 
		cuads = [self.OpPila.pop(), self.OPila.pop(), operando2, valT]
		self.cuad.append(cuads)	
		self.OPila.push(valT)
		self.TPila.push(aux[1])

	#imprime info
	def printS(self):
		print self.OPila.printi()

	#crea un apuntador a una direccion
	def get_temporal_point(self):
		aux = self.get_temporal('$', 'dir', -1)
		return aux[0]
		

	def OpPila_pop(self):
		self.OpPila.pop()

	def OpPila_push(self, op):
		self.OpPila.push(op)

	def TPila_push(self, op):
		self.TPila.push(op)

	def TPila_pop(self, ):
		self.TPila.pop()

	def OPila_push(self, op):
		self.OPila.push(op)
		
	def OPila_pop(self):
		return self.OPila.pop()

	def OPila_peek(self):
		return self.OPila.peek()
	
	def DPila_push(self, op):
		self.DPila.push(op)
		
	def DPila_pop(self):
		return self.DPila.pop()

	def IDPila_push(self, op):
		self.IDPila.push(op)
		
	def IDPila_pop(self):
		return self.IDPila.pop()

	def print_cuad(self):
		print self.cuad

	def get_cuad(self):
		return self.cuad

	def setalcance(self, alcance):
		self.alcance = alcance
	
	def getalcance(self):
		return self.alcance

	def setFuncalcance(self, alcance):
		self.alcanceF.push(alcance)

	def delFuncalcance(self):
		self.alcanceF.pop()

	def getFuncalcance(self):
		return self.alcanceF.peek()
	
	def setRT(self, RT):
		self.RT = RT

	def getRT(self):
		return self.RT

	def setfuncCuad(self):
		self.funcCuad = self.numCuad

	def getfuncCuad(self):
		return self.funcCuad
