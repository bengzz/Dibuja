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
	'LB', 'RB', 'C', 'AP', 'CP', 'IG', 'VALI', 'VALF', 'CI', 'CD', 'MA', 'ME', 'SUM', 'RES', 'MUL', 'DIV', 'STR', 'PC', 'ID', 'AC', 'CC', 'MTH', 'LTH', 'P'
	] + list(reserved.values())

t_ignore 	= ' \t\n\r'
t_P     	= r'&'
t_IG     	= r'='
t_MA      	= r'>'
t_ME      	= r'<'
t_LTH      	= r'<='
t_MTH      	= r'>='
t_CD             = r'!='
t_SUM     	= r'\+'
t_RES    	= r'-'
t_MUL     	= r'\*'
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
t_CI		= r'=='

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


