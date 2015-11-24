from memoria import Memoria
from pila import Pila

class AdminMemoria:

	def __init__(self):
			self.constante_entero = []
			self.constante_flotante = []
			self.constante_str = []
			self.apuntador = Pila()
			self.globales = Memoria()
			self.main = Memoria()
			self.alcanceActual = 0
			self.funciones = dict()
		
	def constTamano(self, sizeE, sizeF, sizeS):
	#modifica la memoria necesaria por las constantes
			self.constante_entero = [0] * sizeE
			self.constante_flotante = [0.0] * sizeF
			self.constante_str = [0] * sizeS
		
	def setMemoriaPrinc(self, strP, enteroP, floatP, boolP, enteroPT, floatPT, pointerP):
	#modifica la memoria del main
			self.main.setMemoria(int(strP), int(enteroP), int(floatP), int(boolP), int(enteroPT), int(floatPT), int(pointerP))
		
	def setMemoriaGlobales(self, strP, enteroP, floatP, boolP, enteroPT, floatPT, pointerP):
	#modifica la memoria de las globales
			self.globales.setMemoria(int(strP), int(enteroP), int(floatP), int(boolP), int(enteroPT), int(floatPT), int(pointerP))
		
	def setFunciones(self, strP, enteroP, floatP, boolP, enteroPT, floatPT, pointerP):
	#crea memoria para la nueva funcion, modifica la memoria y la agrega al diccionario de funciones
			funcion = Memoria()
			funcion.setMemoria(int(strP), int(enteroP), int(floatP), int(boolP), int(enteroPT), int(floatPT), int(pointerP))
			self.funciones[self.alcanceActual+1] = funcion
		
	def cambiaAlcance(self):
	#cambia el alcance actual al siguiente
			self.alcanceActual += 1
		
	def borrar_funcion(self):
	#destruye la memoria asignada para la funcion y regresa al alcance anterior
			self.funciones[self.alcanceActual].dejarMemoria()
			del self.funciones[self.alcanceActual]
			self.alcanceActual -= 1
		
	def escribeValor(self, dirV, valor):
	#escribe el valor de la direccion dada, si la direccion es un apuntador primero recupera la direccion real
			if dirV[1] == '7':
				dirV = int(dirV)
				if((dirV-10000) < 10000):
				#valores globales
					dirV = self.globales.leerValor(dirV-10000)
				elif((dirV-20000) < 10000):
				#valores del main
					dirV = self.main.leerValor(dirV-20000)
				elif((dirV-30000) < 10000):
				#valores de funciones
					dirV = self.funciones[self.alcanceActual].leerValor(dirV-30000)
				dirV = str(dirV)
			dirV = int(dirV)
		#imprime la direccion, dirV
			if((dirV-10000) < 10000):
			#valores globales
				dirV = dirV-10000
				self.globales.escribeValor(dirV, valor)
				return
			if((dirV-20000) < 10000):
			#valores del main
				dirV = dirV-20000
				self.main.escribeValor(dirV, valor)
				return
			if((dirV-30000) < 10000):
			#valores de funciones
				dirV = dirV-30000
				self.funciones[self.alcanceActual].escribeValor(dirV, valor)
				return
			if((dirV-40000) < 10000):
			#constantes
				dirV = dirV-40000
				if(dirV < 1000):
					self.constante_entero[dirV] = int(valor)
				elif(dirV < 2000):
					self.constante_flotante[dirV-1000] = float(valor)
				else:
					self.constante_str[dirV-2000] = str(valor)
				return
			
	def escribeValorS(self, dirV, valor):
	#escribe valores que solo son usados como por patamentros 
			if dirV[1] == '7':
				dirV = int(dirV)
				if((dirV-10000) < 10000):
				#valores globales
					dirV = self.globales.leerValor(dirV-10000)
				elif((dirV-20000) < 10000):
				#valores del main
					dirV = self.main.leerValor(dirV-20000)
				elif((dirV-30000) < 10000):
				#valores de funciones
					dirV = self.funciones[self.alcanceActual+1].leerValor(dirV-30000)
				dirV = str(dirV)
			dirV = int(dirV)
		#imprime la direccion, dirV
			if((dirV-10000) < 10000):
			#valores globales
				dirV = dirV-10000
				self.globales.escribeValor(dirV, valor)
				return
			if((dirV-20000) < 10000):
			#valores del main
				dirV = dirV-20000
				self.main.escribeValor(dirV, valor)
				return
			if((dirV-30000) < 10000):
			#valores de funciones
				dirV = dirV-30000
				self.funciones[self.alcanceActual+1].escribeValor(dirV, valor)
				return
		
	def getValor(self, dirV):
	#recupera el valor de la direccion dada, en caso de que sea un apuntador primero obtiene la direccion real
			if dirV[1] == '7':
		# si la diereccion es un apuntador se recuperar la direccion actual
				dirV = int(dirV)
				if((dirV-10000) < 10000):
				#valores globales
					dirV = self.globales.leerValor(dirV-10000)
				elif((dirV-20000) < 10000):
				#valores del main
					dirV = self.main.leerValor(dirV-20000)
				elif((dirV-30000) < 10000):
				#valores de funciones
					dirV = self.funciones[self.alcanceActual].leerValor(dirV-30000)
				dirV = str(dirV)
			dirV = int(dirV)
		#imprime la direccion, dirV
			if((dirV-10000) < 10000):
			#valores globales
				dirV = dirV-10000
				return self.globales.leerValor(dirV)
			if((dirV-20000) < 10000):
			#valores del main
				dirV = dirV-20000
				return self.main.leerValor(dirV)
			if((dirV-30000) < 10000):
			#valores de funciones
				dirV = dirV-30000
				return self.funciones[self.alcanceActual].leerValor(dirV)
			if((dirV-40000) < 10000):
			#constantes
				dirV = dirV-40000
				if(dirV < 1000):
					return int(self.constante_entero[dirV])
				elif(dirV < 2000):
					return float(self.constante_flotante[dirV-1000])
				else:
					return str(self.constante_str[dirV-2000])
	
	def escribeValorApuntado(self, dirV, valor, alcance):
	#para almacenar el valor en un apuntador
			dirV = int(dirV)
			if((dirV-10000) < 10000):
			#valores globales
				dirV = dirV-10000
				self.globales.escribeValor(dirV, valor)
				return
			if((dirV-20000) < 10000):
			#valores del main
				dirV = dirV-20000
				self.main.escribeValor(dirV, valor)
				return
			if((dirV-30000) < 10000):
			#valores de funciones
				dirV = dirV-30000
				self.funciones[self.alcanceActual+alcance].escribeValor(dirV, valor)
				return
			
	def getValorApuntado(self, dirV):
	#para leer el valor de un apuntador
			dirV = int(dirV)
			if((dirV-10000) < 10000):
			#valores globales
				dirV = dirV-10000
				return self.globales.leerValor(dirV)
			if((dirV-20000) < 10000):
			#valores del main
				dirV = dirV-20000
				return self.main.leerValor(dirV)
			if((dirV-30000) < 10000):
			#valores de funciones
				dirV = dirV-30000
				return self.funciones[self.alcanceActual].leerValor(dirV)
	
	def imprimeFunciones(self):
			print self.alcanceActual
		
	def imprimePrinc(self):
			self.main.imprimeInfo()
		
	def imprimeGlobales(self):
			self.globales.imprimeInfo()
		
	def imprimeConstantes(self):
			print self.constante_entero, " ", self.constante_flotante
		
	def push_apuntador(self, valor):
			self.apuntador.push(valor)
		
	def pop_apuntador(self):
			return self.apuntador.pop()