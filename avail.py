
class avail:
        cubo_semantico = None

        def _init_(self):
        		self.temp_entero = 2000
				self.temp_flotante = 3000
				self.temp_booleano = 4000
				self.bloque = 0
				self.PilaOp = Stack() #Pila de operadores
				self.POper = Stack() #Pila de operandos
				self.TPila = Stack() #Pila de tipos
				self.saltos = Stack() #Pila de saltos
				self.quads = []
				self.numQuad = 0
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
                }
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
                }
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
	
		def get_temporal(self, operador, tipo1, tipo2):
			#se crea un nuevo valor temporal
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
			temp += (self.block * 10000)
			return [temp, self.get_tipo(operador, tipo1, tipo2)]
			
		def setBloque(self, bloque):
			#resetea la memoria para el siguiente bloque
			self.bloque = bloque
			self.temp_entero = 2000
			self.temp_flotante = 3000
			self.temp_booleano = 4000
			
		def getBloque(self):
			#regresa el bloque actual
			return self.bloque
			
		def get_temp_dir(self):
			#regresa la memoria necesaria para las temporales
			return [(self.temp_entero-2000), (self.temp_flotante-3000), (self.temp_booleano-4000)]
		
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
			spCuad = ['-', tem, dirUno, tem]
			self.numQuad += 1
			self.quads.append(spCuad)
			salto = self.saltos.pop()
			aux = self.get_temporal('==', self.TPila.pop(), 'entero')
			spCuad = ['==', tem, dirCero, aux[0]]
			self.numQuad += 1
			self.quads.append(spCuad)
			spCuad.['GOTOF', aux[0], -1, salto]
			self.numQuad += 1
			self.quads.append(spCuad)
			
		def asign(self, var):
			#crea una asignacion
			if(self.POper.size() > 0):
				self.numQuad += 1
				spCuad = [101, self.POper.pop(), -1, var]
				self.quads.append(spCuad)
		
		def condicion_inicio(self):
			#al final de una condicion llena el ultimo goto que fue creado con el cuadruplo actual
			if(self.saltos.size() > 0)
				salto = self.saltos.pop() - 1
				spCuad = self.quads[salto]
				spCuad[3] = self.numQuad
				self.quads[salto] = spCuad
			
		def condicion(self):
			#al inicio de una condicion se crea un gotof y se almacena el num de cuadruplo en la pila de saltos
			condicion = self.POper.pop()
			tipo_cond = self.TPila.pop()
			if(tipo_cond = != "booleano"):
				print "Error, el tipo no coincide"
				sys.error(0)
			else:
				spCuad = ['GOTOF', condicion, -1, -1]
				self.quads.append(spCuad)
				self.numQuad += 1
				self.saltos.push(self.numQuad)
				
		def condicion_else(self):
			#si hay un else, se debe llenar el goto del if y crear un nuevo goto
			salto = self.saltos.pop() -1
			spCuad = self.quads[salto]
			spCuad[3] = self.numQuad +1
			self.quads[salto] = spCuad
			spCuad = ['GOTO', -1, -1, -1]
			self.quads.append(spCuad)
			self.numQuad += 1
			self.saltos.push(self.numQuad)
			
		def printS(self):
			#imprime informacion
			print self.POper.printi()

		def get_temp_point(self):
		#crea un apuntador de direccion
			aux = self.get_temporal('$', 'dir', -1)
			return aux[0]
			
		def main(self):
		#crea el goto al main, gurda el numero de cuadruplo en la pila de saltos
			spCuad = ['GOTO', -1, -1, -1]
			self.quads.append(spCuad)
			self.saltos.push(self.numQuad)
			self.numQuad += 1;
			
		def main_goto(self):
		#hace el goto del main
			salto = self.saltos.pop()
			spCuad = self.quads[salto]
			spCuad[3] = self.numQuad
			self.quads[salto] = spCuad
			
		def funcion_return(self, emty, vDir):
			#revisa si la funcion regreso, si no crea un cuadruplo en la pila de operadores
			if(empty):
				spCuad = ['RETURN', -1, -1, -1]
				self.numQuad += 1
				self.quads.append(spCuad)
				return False
			else:
				spCuad = ['RETURN', self.POper.pop(), -1, vDir]
				self.numQuad += 1
				self.quads.append(spCuad)
				return True
				
		def funcion_end(self):
			#final del cuadruplo
			spCuad = ['ENDPROC', -1, 1]
			self.numQuad += 1
			self.quads.append(spCuad)
			
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
						spCuad = ['PARAMETRO', self.POper.pop(), -1, param[key][2]]
						print spCuad
						cont -= 1
						self.numQuad +=1
						self.quads.append(spCuad)
						
		def llama_funcion(self, var):
		#cuadruplo que contiene el nombre de la funcion la cual se esta llamando
			spCuad = ['ERA', -1, -1, var]
			self.numQuad += 1
			self.quads.append(spCuad)
			self.PilaOp.push('[')
			
		def llama_funcion_final(self, var, vDir, temp):
		#se hace un go sub a la funcion de la gual se hizo el go, se hace una asignacion en caso de que se regrese un valor en una temporal
			spCuad = ['GOSUB', -1, -1, var]
			self.numQuad += 1
			self.quads.append(spCuad)
			spCuad = ['101', vDir, -1, temp]
			self.POper.push(temp)
			self.numQuad += 1
			self.quads.append(spCuad)
			self.PilaOp.pop()
			
		def append_quad(self, quad):
			#concatena los cuadruplos
			self.numQuad += 1
			self.quads.append(quad)
		
		def quad(self):
			#lo utilizan las expresiones para crear cuadruplos
			self.numQuad += 1
			aux = self.get_temporal(self.PilaOp.peek(), self.TPila.pop(), self.TPila.pop())
			tem = aux[0]
			dos = self.POper.pop()
			spCuad = [self.PilaOp.pop(), self.POper.pop(), dos, tem]
			self.quads.append(spCuad)
			self.PilaOp.push(tem)
			self.TPila.push(aux[1])

		def PilaOp_pop(self):
			self.PilaOp.pop()

		def PilaOp_push(self, op):
			self.PilaOp.push(op)

		def TPila_push(self, op):
			self.TPila.push(op)

		def TPila_pop(self, ):
			self.TPila.pop()

		def POper_push(self, op):
			self.POper.push(op)
		
		def POper_pop(self):
			return self.POper.pop()

		def POper_peek(self):
			return self.POper.peek()
				
			