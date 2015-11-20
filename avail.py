from pila import Pila
import sys

class avail:
		cubo_semantico = None

		def _init_(self):
				self.temp_entero = 2000
				self.temp_flotante = 3000
				self.temp_booleano = 4000
				self.temp_dir = 5000
				self.bloque = 0
				self.PilaOp = Pila() #Pila de operadores
				self.POper = Pila() #Pila de operandos
				self.TPila = Pila() #Pila de tipos
				self.saltos = Pila() #Pila de saltos
				self.quads = []
				self.numQuad = 0
				self.funQuad = 0
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
                '<': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        }
                },
                '>': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        }
                },
                '<=': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        }
                },
                '>=': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        }
                },
                '!=': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        }
                },
                '==': {
                        'entero': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
                        },
                        'flotante': {
                                    'entero': 'booleano',
                                    'flotante': 'booleano'
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
                '%': {
                        'entero': {
                                    'entero': 'entero',
                                    'flotante': 'flotante'
                        },
                        'flotante': {
                                    'entero': 'flotante',
                                    'flotante': 'flotante'
                        }
                },
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
				'$': {
						'dir': {
									'-1': 'dir'
						}
				}
=======
>>>>>>> Stashed changes
                '$': {
                		'dir': {
                					'-1': 'dir'
                		}
                }
>>>>>>> origin/master
        }
        
		def get_tipo(self, operador, tipo1, tipo2):
		#regresa el tipo de la operacion
			tip = self.cubo_semantico.get(operador)
			if tip != None:
				tip = tip.get(tipo1)
				if tip != None:
					tip = tip.get(tipo2)
					return tip
			print 'error'
	
		def get_temp(self, operador, tipo1, tipo2):
		#se crea un nuevo valor temporal en base al resultado del cubo semantico
			temp_tipo = self.get_tipo(operador, tipo1, tipo2)
			if temp_tipo == 'entero':
				temp = self.temp_entero
				self.temp_entero += 1
			elif temp_tipo == 'flotante':
				temp = self.temp_flotante
				self.temp_flotante += 1
			elif temp_tipo == 'booleano':
				temp = self.temp_booleano
				self.temp_booleano +=1
			elif tipo1 == 'dir':
				temp = self.temp_dir
<<<<<<< Updated upstream
				self.temp_dir +=1
=======
<<<<<<< HEAD
				self.temp_dir += 1
=======
				self.temp_dir +=1
>>>>>>> origin/master
>>>>>>> Stashed changes
			temp += (self.block * 10000)
			return [temp, self.get_tipo(operador, tipo1, tipo2)]
			
		def setBloque(self, bloque):
		#resetea la memoria para el siguiente bloque
			self.bloque = bloque
			self.temp_entero = 2000
			self.temp_flotante = 3000
			self.temp_booleano = 4000
			self.temp_dir = 5000
			
		def getBloque(self):
		#regresa el bloque actual
			return self.bloque
			
		def get_temp_dir(self):
		#regresa la memoria necesaria para las temporales
			return [(self.temp_entero-2000), (self.temp_flotante-3000), (self.temp_booleano-4000), (self.temp_dir-5000)]
		
		def expresion(self):
		#si hay una expresion para resolver
			if(self.PilaOp.size() > 0):
				if(self.PilaOp.peek() == '>' or self.PilaOp.peek() == '<' or self.PilaOp.peek() == '!=' or self.PilaOp.peek() == '==' or self.PilaOp.peek() == '<=' or self.PilaOp.peek() == '>='):
					self.quad()
		
		def add_sub(self):
		#si hay una operacion se suma o resta
			if(self.PilaOp.size() > 0):
				if(self.PilaOp.peek() == '+' or self.PilaOp.peek() == '-'):
					self.quad()
					
		def mult_div(self):
		#si hay una operacion de multiplicacion o division
			if(self.PilaOp.size() > 0):
				if(self.PilaOp.peek() == '*' or self.PilaOp.peek() == '/'):
					self.quad()
			
		def rep_salto(self, dirUno, dirCero):
		#saca uno de los valores de la temporal 
			tem = self.POper.pop()
			cuads = ['-', tem, dirUno, tem]
			self.numQuad += 1
			self.quads.append(cuads)
			salto = self.saltos.pop()
			aux = self.get_temporal('==', self.TPila.pop(), 'entero')
			cuads = ['==', tem, dirCero, aux[0]]
			self.numQuad += 1
			self.quads.append(cuads)
			cuads = ['GOTOF', aux[0], -1, salto]
			self.numQuad += 1
			self.quads.append(cuads)
			
		def asign(self, var):
		#crea una asignacion
			if(self.POper.size() > 0):
				self.numQuad += 1
				cuads = [101, self.POper.pop(), -1, var]
				self.quads.append(cuads)
		
		def condicion_inicio(self):
		#al final de una condicion llena el ultimo goto que fue creado con el cuadruplo actual
			if(self.saltos.size() > 0):
				salto = self.saltos.pop() - 1
				cuads = self.quads[salto]
				cuads[3] = self.numQuad
				self.quads[salto] = cuads
			
		def condicion(self):
		#al inicio de una condicion se crea un gotof y se almacena el num de cuadruplo en la pila de saltos
			condicion = self.POper.pop()
			tipo_cond = self.TPila.pop()
			if(tipo_cond != "booleano"):
				print "Error, el tipo no coincide"
				sys.error(0)
			else:
				cuads = ['GOTOF', condicion, -1, -1]
				self.quads.append(cuads)
				self.numQuad += 1
				self.saltos.push(self.numQuad)
				
		def condicion_else(self):
		#si hay un else, se debe llenar el goto del if y crear un nuevo goto
			salto = self.saltos.pop() -1
			cuads = self.quads[salto]
			cuads[3] = self.numQuad +1
			self.quads[salto] = cuads
			cuads = ['GOTO', -1, -1, -1]
			self.quads.append(cuads)
			self.numQuad += 1
			self.saltos.push(self.numQuad)
			
		def printS(self):
		#imprime informacion
			print self.POper.printi()

		def get_temp_point(self):
		#crea un apuntador de direccion
			aux = self.get_temporal('$', 'dir', -1)
			return aux[0]
			
		def princ(self):
		#crea el goto al main, gurda el numero de cuadruplo en la pila de saltos
			cuads = ['GOTO', -1, -1, -1]
			self.quads.append(cuads)
			self.saltos.push(self.numQuad)
			self.numQuad += 1;
			
		def princ_goto(self):
		#hace el goto del main
			salto = self.saltos.pop()
			cuads = self.quads[salto]
			cuads[3] = self.numQuad
			self.quads[salto] = cuads
			
		def rep(self):
		#crea una copia del numero que representa las veces que el bloque fue creado, y almacena el valor en la pila
			h = self.get_temp('-', self.TPila.peek(), self.TPila.pop())
			tem = h[0]
			cuads = [101, self.POper.pop(), -1, tem]
			self.numQuad += 1
			self.quads.append(cuads)
			self.saltos.push(self.numQuad)
			self.POper.push(tem)
			self.TPila.push(h[1])
			
		def dim(self, dim, pointer):
		#para los arreglos, crea un cuad que checa que el valor ente en el rango
			cuads = ['DIM', dim, pointer]
			self.numQuad += 1
			self.quads.append(cuads)
			self.numQuad += 1
			h = self.get_temp('$', 'dir', -1)
			tem = h[0]
			cuads = ['DIR', self.POper.pop(), pointer, tem]
			self.quads.append(cuads)
			self.POper.push(tem)
			
		def dimT(self, dim, pointer):
		#para las matrices, pointer representa las filas
			h = self.get_temp('+', 'int', 'int')
			tem = h[0]
			cuads = ['*', pointer, '40002', tem]
			self.quads.append(cuads)
			pointer = tem
			
			cuads = ['DIM', dim, pointer, -1]
			self.quads.append(cuads)
			
			h = self.get_temp('$', 'dir', -1)
			tem = h[0]
			ren = self.POper.pop()
			cuads = ['DIR', ren, pointer, tem]
			one = tem
			self.quads.append(cuads)
			h = self.get_temp('+', 'int', 'int')
			tem = h[0]
			cuads = ['+', pointer, '40000', tem]
			self.quads.append(cuads)
			self.POper.push(tem)
			h = self.get_temp('$', 'dir', -1)
			tem = h[0]
			cuads = ['DIR', ren, self.POper.pop(), tem]
			self.quads.append(cuads)
			help = self.POper.pop()
			self.POper.push(tem)
			self.POper.push(help)
			self.POper.push(one)
			self.numQuad += 4
			
		def dimTP(self, direccion, row, dim):
		#al inicializar una matriz, revisa la dimension, crea un apuntador para que asigne algo al siguiente valor
			row *= 2
			cuads = ['DIMC', dim, row, -1]
			self.quads.append(cuads)
			
			h = self.get_temp('$', 'dir', -1)
			tem = h[0]
			cuads = ['DIMC', direccion, (row+1), tem]
			self.quads.append(cuads)
			self.asign(tem)
			
			h = self.get_temp('$', 'dir', -1)
			tem = h[0]
			cuads = ['DIMC', direccion, row, tem]
			self.quads.append(cuads)
			self.asign(tem)
			
			self.numQuad += 3
			
		def dimP(self, direccion, row, dim):
		#checa la dimension, obtiene la direccion del puntero, cuad que genera la direccion actual
			cuads = ['DIMC', dim, row, -1]
			self.quads.append(cuads)
			
			h = self.get_temp('$', 'dir', -1)
			tem = h[0]
			cuads = ['DIMC', direccion, row, tem]
			self.quads.append(cuads)
			self.asign(tem)
			
			self.numQuad += 2
			
		def funcion_return(self, emty, vDir):
		#revisa si la funcion regreso, si no crea un cuadruplo en la pila de operadores
			if(empty):
				cuads = ['RETURN', -1, -1, -1]
				self.numQuad += 1
				self.quads.append(cuads)
				return False
			else:
				cuads = ['RETURN', self.POper.pop(), -1, vDir]
				self.numQuad += 1
				self.quads.append(cuads)
				return True
				
		def funcion_end(self):
		#final del cuadruplo
			cuads = ['ENDPROC', -1, 1]
			self.numQuad += 1
			self.quads.append(cuads)
			
		def funcion_param(self, param):
		#checa los parametros de las funciones de acuerdo al orden
			cont = len(param)
			if self.POper.size() < cont:
				print "Faltan parametros"
				sys.exit(0)
			lista = []
			cont = len(param) -1
			while cont >= 0:
				for key in param:
					if cont == param[key][1]:
						cuads = ['PARAMETRO', self.POper.pop(), -1, param[key][2]]
						print cuads
						cont -= 1
						self.numQuad +=1
						self.quads.append(cuads)
						
		def llama_funcion(self, var):
		#cuadruplo que contiene el nombre de la funcion la cual se esta llamando
			cuads = ['ERA', -1, -1, var]
			self.numQuad += 1
			self.quads.append(cuads)
			self.PilaOp.push('[')
			
		def llama_funcion_final(self, var, vDir, temp):
		#se hace un go sub a la funcion de la gual se hizo el go, se hace una asignacion en caso de que se regrese un valor en una temporal
			cuads = ['GOSUB', -1, -1, var]
			self.numQuad += 1
			self.quads.append(cuads)
			cuads = ['101', vDir, -1, temp]
			self.POper.push(temp)
			self.numQuad += 1
			self.quads.append(cuads)
			self.PilaOp.pop()
			
		def append_quad(self, quad):
		#concatena los cuadruplos
			self.numQuad += 1
			self.quads.append(quad)
			
		def append_quad_one(self, fun):
		#usado por las funciones que solo tienen un parametro
			self.numQuad += 1
			spQuad = [fun, self.POper.pop(), -1, -1]
			self.TPila.pop()
			self.quads.append(spQuad)
			
		def append_quad_two(self, fun):
		#usado por funciones que tienen dos parametros
			self.numQuad += 1
			two = self.POper.pop()
			self.TPila.pop()
			spQuad = [fun, self.POper.pop(), two, -1]
			self.TPila.pop()
			self.quads.append(spQuad)
			
		def append_quad_three(self, fun):
		#usado por funciones con tres parametros
			self.numQuad += 1
			uno = self.POper.pop()
			self.TPila.pop()
			dos = self.POper.pop()
			self.TPila.pop()
			cuads = [fun, self.POper.pop(), dos, uno]
			self.TPila.pop()
			self.quads.append(cuads)
			
		def append_quad_tri(self, fun):
			self.numQuad += 2
			y3 = self.POper.pop()
			self.TPila.pop()
			x3 = self.POper.pop()
			self.TPila.pop()
			y2 = self.POper.pop()
			self.TPila.pop()
			x2 = self.POper.pop()
			self.TPila.pop()
			y = self.POper.pop()
			self.TPila.pop()
			x = self.POper.pop()
			self.TPila.pop()
			cuads = [fun, x, y, -1]
			self.quads.append(cuads)
			cuads = [x2, y2, x3, y3]
			self.quads.append(cuads)
		
		def quad(self):
		#lo utilizan las expresiones para crear cuadruplos
			self.numQuad += 1
			aux = self.get_temporal(self.PilaOp.peek(), self.TPila.pop(), self.TPila.pop())
			tem = aux[0]
			dos = self.POper.pop()
			cuads = [self.PilaOp.pop(), self.POper.pop(), dos, tem]
			self.quads.append(cuads)
			self.PilaOp.push(tem)
			self.TPila.push(aux[1])

		def PilaOp_pop(self):
			self.PilaOp.pop()

		def PilaOp_push(self, op):
			self.PilaOp.push(op)

		def TPila_push(self, op):
			self.TPila.push(op)

		def TPila_pop(self):
			self.TPila.pop()

		def POper_push(self, op):
			self.POper.push(op)
		
		def POper_pop(self):
			return self.POper.pop()

		def POper_peek(self):
			return self.POper.peek()
			
		def print_quads(self):
			print self.quads
		
		def get_quads(self):
			return self.quads
			
		def setAlcance(self, alcance):	
			self.alcance = alcance
			
		def getAlcance(self):
			return self.alcance
			
		def setFuncAlcance(self, alcance):
			self.alcanceF.push(alcance)
			
		def delFuncAlcance(self):
			self.alcanceF.pop()
		
		def getFuncAlcance(self):
			return self.AlcanceF.peek()
			
		def setRT(self, RT):
			self.RT = RT
			
		def getRT(self):
			return self.RT
		
		def setfuncQuad(self):
			self.funQuad = self.numQuad
			
		def getfuncQuad(self):
			return self.funQuad