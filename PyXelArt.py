from PIL import Image, ImageFilter, ImageEnhance, ImageTk
import Tkinter,tkFileDialog
	
def pintar_imagen(image):
	sizeLimiteAlto, sizeLimiteAncho = image.size
	xInf, yInf = image.size
	if sizeLimiteAlto > 500 or sizeLimiteAncho > 500:
		while sizeLimiteAlto > 500 or sizeLimiteAncho > 500:
			sizeLimiteAlto = sizeLimiteAlto / 2
			sizeLimiteAncho = sizeLimiteAncho / 2
			imageThumb = image.resize((sizeLimiteAlto,sizeLimiteAncho), Image.ANTIALIAS)
	else:
		imageThumb = image
	infoLabelX = "X:", xInf
	infoLabelY = "Y:", yInf
	labelXInfo = Tkinter.Label(ventana, text=infoLabelX)
	labelYInfo = Tkinter.Label(ventana, text=infoLabelY)
	labelXInfo.grid(row=0, column=1)
	labelYInfo.grid(row=0, column=2)
	img = ImageTk.PhotoImage(imageThumb)
	panel.configure(image = img,width = sizeLimiteAlto, height = sizeLimiteAncho)
	ventana.mainloop()
		
def establecer_path():
	file = tkFileDialog.askopenfile(parent=ventana,mode='rb',title='Choose a file')
	if file != None:
		global PATH
		PATH = file.name
		global image
		image = Image.open(PATH)
		pintar_imagen(image)

def cargar_imagen():
	global image
	image = Image.open(PATH)
	piXel = image.load()
	#1 es el original
	balancePix = 1
	contrastPix = 1
	brilloPix = 1
	nitiPix = 1
	#Filtro para cada diferencia entre el valor del RGB anterior se necesita para cambiar el color del pixel
	colorPix = 1
	ancho, alto = image.size
	if ancho < alto:
		sizePix = alto / tamPix
	else:
		sizePix = ancho / tamPix
	x1 = 0
	x2 = sizePix
	y1 = 0
	y2 = sizePix			
	#Pinta y colorea
	pinta_pixel(x1, x2, y1, y2, sizePix, ancho, alto, piXel, colorPix)
	convertBalance = ImageEnhance.Color(image)
	convertContrast = ImageEnhance.Contrast(image)
	convertBrillo = ImageEnhance.Brightness(image)
	convertNitidez = ImageEnhance.Sharpness(image)
	image = convertBalance.enhance(balancePix)
	image = convertContrast.enhance(contrastPix)
	image = convertBrillo.enhance(brilloPix)
	image = convertNitidez.enhance(nitiPix)
	pintar_imagen(image)	
	
def pinta_pixel(x1, x2, y1, y2, sizePix, ancho, alto, piXel, colorPix):
	color = 0, 0, 0
	while x2 + sizePix < ancho or y2 + sizePix < alto:
	
		#Hay que tocar colores para que sean mas uniformes, habria que comparar con los pixels de alrededor		
		ra, ga, ba = 0, 0, 0
		x3 = x1 + sizePix / 2
		y3 = y1 + sizePix / 2
		colorA = color
		color = piXel[x3, y3]
		r, g, b = color
		if colorPix > abs(ra-r) and colorPix > abs(ga-g) and colorPix > abs(ba-b):
			#print colorA, colorPix
			color = colorA
			
		#No mili toque
		for x in range(x1, x2):
			for y in range(y1, y2):
				piXel[x,y] = color
				#print x, y

		if x2 + sizePix < ancho:
			x1 = x2
			x2 = x2 + sizePix
			#print "X", x1, x2
	
		elif y2 + sizePix < alto:
			x1 = 0
			x2 = sizePix
			y1 = y2
			y2 = y2 + sizePix	
			#print "Y", y1, y2

def establecer_tamPix():
	#Tamano pixel, menos es mas grande
	#Siendo 1 la imagen normal y el 255 maximo
	global tamPix
	tamPix = int(textTamPix.get())
	cargar_imagen()
	
def redimensionar():
	tamX = int(textX.get())
	tamY = int(textY.get())
	tamRedimension = tamX, tamY
	image.thumbnail(tamRedimension, Image.ANTIALIAS)
	pintar_imagen(image)
	
def guardarImg():
	image.save("prueba" + ".jpg")


#Ventanitas para todos
ventana = Tkinter.Tk()
ventana.maxsize(width=800, height=600)

botonSeleccion = Tkinter.Button(ventana, text="Elegir imagen", command=establecer_path)
botonPixelar = Tkinter.Button(ventana, text="Pixelar", command=establecer_tamPix)
botonRedimensionar = Tkinter.Button(ventana, text="Redimensionar", command=redimensionar)
botonGuardar = Tkinter.Button(ventana, text="Guardar", command=guardarImg)

textTamPix = Tkinter.Entry(ventana)
labelTamPix = Tkinter.Label(ventana, text="Tamano de Pixel")
labelY = Tkinter.Label(ventana, text="Y")
textY = Tkinter.Entry(ventana)
labelX = Tkinter.Label(ventana, text="X")
textX = Tkinter.Entry(ventana)
panel = Tkinter.Label(ventana)
panel.grid(row=0, column=0)
botonSeleccion.grid(row=1, column=0)
labelTamPix.grid(row=1, column=1)
textTamPix.grid(row=1, column=2)
labelX.grid(row=2, column=1)
textX.grid(row=2, column=2)
labelY.grid(row=3, column=1)
textY.grid(row=3, column=2)
botonPixelar.grid(row=4, column=0)
botonRedimensionar.grid(row=4, column=1)
botonGuardar.grid(row=4, column=2)
ventana.mainloop()

"""
panel.pack(side = "bottom", fill = "both", expand = "no")
botonSeleccion.pack(side="right")
textTamPix.pack(side="left")
botonPixelar.pack(side="bottom")
ventana.mainloop()
"""
#Tips
#ancho, alto = image.size
#print(image.format, image.size, image.mode)
#image = image.filter(ImageFilter.BLUR)
#image.save("prueba" + ".jpg")