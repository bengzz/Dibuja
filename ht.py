class HashTable():

"""Inicializar la tabla.........."""
        def _init_(self):
                self.size = 4
                self.table = [None]*self.size
                self.numVar = 0
        
"""Agregar a la tabla............"""    
        def put(self, key, value):
                if(self.numVar > self.size/2):
                        self.size *= 2
                        pastTable = self.table
                        self.table = [None]*self.size
                        self.numVar = 0
                        
        """Rehash con llamada recursiva.........."""    
                        for var in pastTable
                                if(var != None):
                                        self.put(var.key(),var.value())
                                else:
                                        pass
                                        
         """Detectar si el key es un string y que no sea 0"""
                code = 0
                if (type(key) is str and len(key) > 0):
                        code = ord( key[0])
                i = code % self.size
                
                while self.table[i] != None and self.table[i].key != key:
                        i = (i + 1) % self.size
                
                if (self.table[i] == None):
                        self.numVar +=1
                
                self.table[i].Input(key,value)

"""Obtener de la tabla............"""
        def get(self, key):
        """Detectar si el key es un string y que no sea 0"""
                code = 0
                if (type(key) is str and len(key) > 0):
                        code = ord( key[0])
                i = code % self.size
                auxi = i
                w = False

                while self.table[i] != None and self.table[i].key != key and not w:
                        i = (i + 1) % self.size
                        if(i == aux):
                                w = True

                if (self.table[i] != None or w):
                        rt = self.table[i].value()
                else:
                        rt = None
                return rt

        def has(self, key):
                code = 0
                if (type(key) is str and len(key) > 0):
                    code = ord( key[0])
                i = code % self.size
                auxi = i
                w = False
                    
                while self.table[i] != None and self.table[i].key != key and not w:
                        i = (i + 1) % self.size
                        if(i == aux):
                                w = True
                        if (self.table[i] != None or w):
                                rt = False
                        else:
                                rt = True
                        return rt

        def entry(self):
				return self._table
				
		def total(self):
				return self._numEntries


#---------Input------
class Input():
		def __init__(self, aKey, aValue):
				self._key = aKey
				self._value = aValue

		def key(self):
				return self._key

		def value(self):
				return self._value