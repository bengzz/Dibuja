from memoria import Memoria
from pila import Pila

class AdminMemoria:

	def _init_(self):
		self.constante_entero = []
		self.constante_flotante = []
		self.constante_str = []
		self.apuntador = Pila()
		self.globales = Memoria()
		self.main = Memoria()
		self.alcanceActual = 0
		self.funciones = dict()
		
	def constSize(self, sizeE, sizeF, sizeS):
	#modifica la memoria necesaria por las constantes
		self.constante_entero = [0] * sizeE
		self.constante_flotante = [0.0] * sizeF
		self.constante_str = [0] * sizeS
		
	def setMemoriaMain(self, strP, enteroP, floatP, boolP, enteroPT, floatPT, pointerP):
	#modifica la memoria del main
		self.main.setMem(int(strP), int(enteroP), int(floatP), int(boolP), int(enteroPT), int(floatPT), int(pointerP)
		
	def setMemoriaGlobales(self, strP, enteroP, floatP, boolP, enteroPT, floatPT, pointerP):
	#modifica la memoria de las globales
		self.globales.setMem(int(strP), int(enteroP), int(floatP), int(boolP), int(enteroPT), int(floatPT), int(pointerP)
		
	def setFunciones(self, strP, enteroP, floatP, boolP, enteroPT, floatPT, pointerP):
	#crea memoria para la nueva funcion, modifica la memoria y la agrega al diccionario de funciones
		funcion = Memoria()
		funcion.setMem(int(strP), int(enteroP), int(floatP), int(boolP), int(enteroPT), int(floatPT), int(pointerP)
		self.funciones[self.alcanceActual+1] = funcion
		
	def cambiaAlcance(self):
	#cambia el alcance actual al siguiente
		self.alcanceActual += 1
		
	def borrar_funcion(self):
	#destruye la memoria asignada para la funcion y regresa al alcance anterior
		self.funciones[self.alcanceActual].releseMem()
		del self.funciones[self.alcanceActual]
		self.alcanceActual -= 1