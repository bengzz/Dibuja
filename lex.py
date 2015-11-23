
# -----------------------------------------------------------------------------
# lex.py
# -----------------------------------------------------------------------------
import ply.lex as lex

reserved = {
	'progama' : 'PR',
	'funcion' : 'FUNCION',
	'princ' : 'PRINC',
	'regresa' : 'REGRESA',
	'entero' : 'ENT',
	'booleano' : 'BOOL',
	'flotante' : 'FLOT',
	'void' : 'VOID',
	'global' : 'GL',
	'local' : 'LC',
	'si' : 'SI',
	'sino' : 'SINO', 
	'mientras' : 'MIENTRAS',
	'para' : 'PARA',
	'cuadrado' : 'CUAD',
	'circulo' : 'CIRC',
	'arco' : 'ARC',
	'triangulo' : 'TRIAN',
	'poligono' : 'POLI',
	'linea' : 'LIN',
	'contorno' : 'CONTORNO',
	'relleno' : 'RELLENO',
	'texto' : 'TEXTO',
	'grosor' : 'GROSOR',
	'xy' : 'XY',
	'rotacion' : 'ROTACION',
}

#lista de tokens con sus respectivos nombres
tokens = [
	'Y', 'O', 'P', 'SUM', 'RES', 'MUL', 'DIV', 'ME', 'MA', 'CI', 'CD', 'IG', 'PC', 'C', 'AC', 'CC', 'AP', 'CP', 'VALI', 'VALF', 'STR', 'ID'
] + list(reserved.values())


t_Y		= r'y'
t_O		= r'o'
t_P     = r'&'
t_SUM	= r'\+'
t_RES 	= r'-'
t_MUL	= r'\*'
t_DIV	= r'/'
t_ME	= r'<'
t_MA	= r'>'
t_CI	= r'=='
t_CD	= r'!='
t_IG	= r'='
t_PC	= r';'
t_C		= r'\,'
t_AC	= r'\['
t_CC	= r'\]'
t_AP	= r'\('
t_CP	= r'\)'
t_VALI	= r'\d+'
t_VALF	= r'\d+\.\d+'
t_STR 	= r'\'.*\''

def t_ID(t):
	r'[a-zA-Z][a-zA-Z0-9]*'
	t.type = reserved.get(t.value, 'ID')
	return t

def t_error(t):
	if(t.value[0] != None):
		print "Caracter invalido ", t.value[0] ,
		t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()