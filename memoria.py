class Memoria:
	
	def_init_(self):
		self.bloque_str = []
		self.bloque_entero = []
		self.bloque_float = []
		self.temp_bloque_bool = []
		self.temp_bloque_entero = []
		self.temp_bloque_float = []
		self.pointers = []
		
	def setMem(self, strP, enteroP, floatP, boolP, enteroPT, floatPT, pointerP):
		self.bloque_str = [0] * strP
		if enteroP > 0:
			self.bloque_entero = [0] * (enteroP + 1)
		else:
			self.bloque_entero = [0] * enteroP
		if floatP > 0:
			self.bloque_float = [0.0] * (floatP + 1)
		else:
			self.bloque_float = [0.0] * floatP
		if boolP > 0:
			self.temp_bloque_bool = [True] * (boolP + 1)
		else:
			self.temp_bloque_bool = [True] * boolP
		if enteroPT > 0:
			self.temp_bloque_entero = [0] * (enteroPT + 1)
		else:
			self.temp_bloque_entero = [0] * enteroPT
		if floatPT > 0:
			self.temp_bloque_float = [0.0] * (floatPT + 1)
		else:
			self.temp_bloque_float = [0.0] * floatPT
		if pointerP < 0:
			self.pointers = [0] * (pointerP + 1)
		else:
			self.pointers = [0] * pointerP
			
	def imprime(self):
		print "str", self.bloque_str, "entero", self.bloque_entero, "float", self.bloque_float, "Tbooleano", self.temp_bloque_bool, "Tentero", self.temp_bloque_entero, "Tfloat", self.temp_bloque_float
		
	def escribeValor(self, dirV, valor):
		if (dirV >= 1000 and dirV <= 1999):
			self.bloque_str[(dirV-1000)] = str(valor)
		elif (dirV >= 2000 and dirV <= 2999):
			self.bloque_entero[(dirV-2000)] = int(valor)
		elif (dirV >= 3000 and dirV <= 3999):
			self.bloque_float[(dirV-3000)] = float(valor)
		elif (dirV >= 4000 and dirV <= 4999):
			self.temp_bloque_bool[(dirV-4000)] = bool(valor)
		elif (dirV >= 5000 and dirV <= 5999):
			self.temp_bloque_entero[(dirV-5000)] = int(valor)
		elif (dirV >= 6000 and dirV <= 6999):
			self.temp_bloque_float[(dirV-6000)] = float(valor)
		elif (dirV >= 7000 and dirV <= 7999):
			self.pointers[(dirV-7000)] = int(valor)
			
	def leerValor(self, dirV):
		if (dirV >= 1000 and dirV <= 1999):
			return self.bloque_str[(dirV-1000)]
		elif (dirV >= 2000 and dirV <= 2999):
			return self.bloque_entero[(dirV-2000)]
		elif (dirV >= 3000 and dirV <= 3999):
			return self.bloque_float[(dirV-3000)]
		elif (dirV >= 4000 and dirV <= 4999):
			return self.temp_bloque_bool[(dirV-4000)]
		elif (dirV >= 5000 and dirV <= 5999):
			return self.temp_bloque_entero[(dirV-5000)]
		elif (dirV >= 6000 and dirV <= 6999):
			return self.temp_bloque_float[(dirV-6000)]
		elif (dirV >= 7000 and dirV <= 7999):
			return self.pointers[(dirV-7000)]
			
	def releseMem(self):
		del self.bloque_str
		del self.bloque_entero
		del.self.bloque_float
		del.self.temp_bloque_bool
		del.self.temp_bloque_entero
		del.self.temp_bloque_float
		del.self.temp.pointers
		
			