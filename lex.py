import ply.lex as lex

reserved = {
   'si' : 'SI',
   'sino' : 'SINO',
   'programa' : 'PROG',
   'var' : 'V',
   'princ' : 'PRINC',
   'entero' : 'ENT',
   'flotante' : 'FLOT',
   'void' : 'VOID',
   'global' : 'GL',
   'funcion': 'FUNCION',
   'rectangulo' :'REC',
   'fondo' :'Fondo',
   'triangulo' :'TRI',
   'circulo' : 'CIR',
   'cuadrado' : 'SQ',
   'poligono' : 'POL',
   'angulo' : 'A',
   'arco' : 'ARC',
   'linea' : 'LS',
   'repetir' : 'RE',
   'regresar' : 'RT',
   'texto' : 'LA',

   'grosor':'GROSOR',
   'contorno':'CONTORNO',
   'relleno':'RELLENO',
  
   'xy':'XY',
   'px': 'PX',
   'py':'PY',
}

#List of token name.
tokens = [
	'LB', 'RB', 'C', 'AP', 'CP', 'IG', 'VALI', 'VALF', 'SEQ', 'D', 'MT', 'LT', 'ADD', 'SUB', 'M', 'DIV', 'STR', 'PC', 'ID', 'AC', 'CC', 'MET', 'LET', 'P'
	] + list(reserved.values())

t_ignore 	= ' \t\n\r'
t_P     	= r'&'
t_IG     	= r'='
t_MT      	= r'>'
t_LT      	= r'<'
t_LET      	= r'<='
t_MET      	= r'>='
t_D             = r'<>'
t_ADD     	= r'\+'
t_SUB    	= r'-'
t_M     	= r'\*'
t_DIV  		= r'/'
t_PC    	= r';'
t_C     	= r'\,'
t_LB    	= r'\{'
t_RB    	= r'\}'
t_AP    	= r'\('
t_CP    	= r'\)'
t_AC      = r'\['
t_CC      = r'\]'
t_VALI  	= r'\d+'
t_VALF  	= r'\d+\.\d+'
t_STR		= r'\'.*\''
t_SEQ		= r'=='

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Error handling rule
def t_error(t):
        if(t.value[0] != None):
	    print "Illegal character ", t.value[0] ,
	    t.lexer.skip(1)

lex.lex()


