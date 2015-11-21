from Tkinter import *
#from MaquinaVirtual import *
import os, sys
import ply.yacc as yacc
import lex 

mensajeError = ""
mensajeErrorMV = ""
root = Tk()
root.geometry("1000x700")
root.resizable(width=FALSE, height=FALSE)
root.title("Dibuja++")

#menu de muestra grafica, objeto donde se posiciona el texto a abrir y/o el texto que se va a guardar

class NotePad:
	def __init__(self,text):
		self.root = root
		self.text = text
		menubar = Menu(self.root)
		
		#Funciones de los menus
		MenuArchivo = Menu(menubar)
		MenuArchivo = Menu(menubar)
		#MenuArchivo.add_command(label="Abrir", command=self.abrir)
		#MenuArchivo.add_command(laber="Guardar", command=self.guardar)
		menubar.add_cascade(label="Archivo", menu=MenuArchivo)
		self.root.config(menu=menubar)
		
	#guardar
	#abrir
		
	def sobre(self):
		root = Tk()
		root.wm_title("Sobre")
		texto = ("Dibija")
		textOnLabel = Label(root, text=texto)
		textOnLabel.pack()
		
#Boton compilar
def compilar():
	global mensajeError
	print "compilando"
	textoutput = ""
	textoutput = text.get(0.0, END) #Trae el texto del frame txto
	
	l = lex.lex()
	p = yacc.yacc()
	
	textConsola.configure(state='normal')
	textConsola.delete(0.0, END)
	textConsola.insert(0.0, mensajeError)
	textConsola.configure(state='disabled')
	
#Boton de ejecutar y se manda dibujar
def ejecutar():
	global mensajeError
	print "ejecutando"
	compilar()
	
#Boton Borrar
def borrar():
	global mensajeError
	print "borrar"
	
#Se pintan todos los cuadrados y canvas correspondientes a la interfaz grafica

frmBotones = Frame(width=1000,height=100, bd=1, relief=SUNKEN)
frmBotones.pack(side='bottom', fill='both')
btnCompilar= Button(frmBotones, text="Compilar",command=compilar,width=10,height=1).grid(row=0,column=0,padx=100, pady=10)
btnEjecutar= Button(frmBotones, text="Ejecutar",command=ejecutar,width=10,height=1).grid(row=0,column=1,padx=100, pady=10)
btnClear = Button(frmBotones, text="Borrar", command= borrar, width=10, height=1).grid(row=0,column=2, padx=100, pady=10)


frameConsola = Frame(width=500,height=100, bd=3, relief=SUNKEN)
frameConsola.pack(side='bottom')

frmTexto = Frame(bd=3, relief=SUNKEN)
frmTexto.pack(side='left', fill='both')

frmCanvas = Frame(bd=3, relief=SUNKEN)
frmCanvas.pack(side='left', fill='both')

scrollbar = Scrollbar(frmTexto)
scrollbar.pack(side=RIGHT, fill=Y)

text=Text(frmTexto, background = 'ghost white')
text.pack(side='left', fill='both')
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

NotePad(text)

textConsola=Text(frameConsola,width=500, height=6, background = 'LightCyan2')
textConsola.pack(fill='both', expand='no')
textConsola.config(state='disabled')

canvas = Canvas(frmCanvas, width=400)
canvas.pack(side='left',fill='both')
anchoCanvas= int(canvas['width'])   #283
alturaCanvas= int(canvas['height']) #198


root.mainloop()
	