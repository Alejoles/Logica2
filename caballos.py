#Problema de los 3 caballos
print("importando librerias...")
print("...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
print("...")
print("Listo!")

Pila = []
Conectivos = ['O','Y','>']
Negacion= ['-']
LetrasProposicionales = [str(i) for i in range(1,10)] #Crear las letras proposicionales
Conjunciones = ' ' #Para guardar las conjunciones de trios de disyunciones de literales
Inicial = True
interps = [] #Lista de todas las posibles interpretaciones(diccionarios)
aux = {} #Primera interpretacion
listainterpsverdad = []
#-----------------------------------Clase Tree---------------------------

class Tree:
	def __init__(self,l,iz,der):
		self.label = l
		self.left = iz
		self.right = der
#-------------------------------------------------------------------------------------------------
#					Dibujar tablero


def dibujar_tablero(f, n):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step = 1./3
    tangulos = []
    # Creo los cuadrados claros en el tablero
    tangulos.append(patches.Rectangle(\
                                    (0, step), \
                                    step, \
                                    step,\
                                    facecolor='cornsilk')\
                                    )
    tangulos.append(patches.Rectangle(*[(step, 0), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step, step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step, 2 * step), step, step],\
            facecolor='cornsilk'))
    # Creo los cuadrados oscuros en el tablero
    tangulos.append(patches.Rectangle(*[(2 * step, 2 * step), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(0, 2 * step), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(2 * step, 0), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(step, step), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(0, 0), step, step],\
            facecolor='lightslategrey'))

    # Creo las líneas del tablero
    for j in range(3):
        locacion = j * step
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],\
                facecolor='black'))
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],\
                facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    # Cargando imagen de caballo
    arr_img = plt.imread("caballo.png", format='png')
    imagebox = OffsetImage(arr_img, zoom=0.1)
    imagebox.image.axes = axes

    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.165, 0.835]
    direcciones[2] = [0.5, 0.835]
    direcciones[3] = [0.835, 0.835]
    direcciones[4] = [0.165, 0.5]
    direcciones[5] = [0.5, 0.5]
    direcciones[6] = [0.835, 0.5]
    direcciones[7] = [0.165, 0.165]
    direcciones[8] = [0.5, 0.165]
    direcciones[9] = [0.835, 0.165]

#    for l in f:
#        if '-' not in l:
#            ab = AnnotationBbox(imagebox, direcciones[int(l)], frameon=False)
#            axes.add_artist(ab)

    for key in f:
        if f[key]==1:
            ab = AnnotationBbox(imagebox, direcciones[int(key)], frameon=False)
            axes.add_artist(ab)


    #plt.show()
    fig.savefig("tablero_" + str(n) + ".png")




#-----------------------------------------------------------------------------------
#					DEFINICION DE LA FUNCION VI

def mayor(a, b):
	mayor = b
	if(a>b):
		mayor = a
	return mayor

def VI(A,i):
	if A.label in LetrasProposicionales:
		return i[A.label]
	elif A.label in Negacion:
		return 1 - VI(A.right,i)
	elif A.label == 'Y':
		return VI(A.left,i) * VI(A.right,i)
	elif A.label == 'O':
		return mayor(VI(A.left,i), VI(A.right,i))
	elif A.label == '>':
		return mayor(1 - VI(A.left,i) , VI(A.right,i))

#----------------------------------------------------------------------------------- Polaco inverso = osrevni ocalop
#					String2Tree
# Nos pasa el literal que formamos en la instrucción anterior y la vuelve un arbol

# Vamos a crear las formulas en notacion polaca inversa

A1 = "8-6-Y1>"
A2 = "9-7-Y2>"
A3 = "8-4-Y3>"
A4 = "9-3-Y4>"
A6 = "7-1-Y6>"
A7 = "6-2-Y7>"
A8 = "3-1-Y8>"
A9 = "4-2-Y9>"

A = "8-6-Y1>9-7-Y2>Y8-4-Y3>Y9-3-Y4>Y7-1-Y6>Y6-2-Y7>Y3-1-Y8>Y4-2-Y9>Y"


A = A + "2" + "6" + "Y" + "Y"

# Acá terminamos de definir las formulas en notacion polaca inversa
def String2Tree(A, LetrasProposicionales):
	#A = Lista de caracteres con una formula escrita en notacion polaca inversa
	Conectivos = ['O','Y','>']
	for c in A:
		if c in LetrasProposicionales:
			Pila.append(Tree(c,None,None))
		elif c=='-':
			FormulaAux = Tree(c,None,Pila[-1])
			del Pila[-1]
			Pila.append(FormulaAux)
		elif c in Conectivos:
			FormulaAux = Tree(c,Pila[-1],Pila[-2])
			del Pila[-1]
			del Pila[-1]
			Pila.append(FormulaAux)
	return Pila[-1]
			
			
#-----------------------------------------------------------------------------------
#		Definimos los literales que necesitamos para el problema REGLA 1


for p in LetrasProposicionales:
	Aux1 = [x for x in LetrasProposicionales if x!=p] #todas las LetProp excepto p
	for q in Aux1:
		Aux2 = [x for x in Aux1 if x!=q] # excepto p y q
		for r in Aux2:
			Literal = r + q + p + 'Y' + 'Y'
			Aux3 = [x + '-' for x in Aux2 if x!=r]
			for k in Aux3:
				Literal = k + Literal + 'Y'
			if Inicial:
				Conjunciones = Literal
				Inicial = False
			else:
				Conjunciones = Literal + Conjunciones + 'O'





#-----------------------------------------------------------------------------------
#				Todas las posibles interpretaciones


for a in LetrasProposicionales:
	aux[a] = 1 #incializamos la primera interpretacion con todo verdadero ...

interps.append(aux) #... y la incluimos en interps

for a in LetrasProposicionales:
	interps_aux = [i for i in interps] #lista auxiliar de nuevas interpretaciones

	for i in interps_aux:
		aux1 = {} # Diccionario auxiliar para crear nueva interpretacion
	
		for b in LetrasProposicionales:
			if a==b:
				aux1[b] = 1 - i[b] # Cambia el valor de verdad para b
			else:
				aux1[b] = i[b] # ... Y matiene el valor de verdad para las otras letras
		interps.append(aux1) # Incluye la nueva interpretacion en la lista
	



#-------------------------------------------------------------------------------------------------
#		Acá determinamos el valor de verdad de los literales en la conjuncion

Arbol = String2Tree(A, LetrasProposicionales)
cont = 1
for j in interps:
	if(VI(Arbol,j) == 1):
		listainterpsverdad.append(j)
		dibujar_tablero(j,cont)
		cont += 1


# TOCA ASIGNARLE EL VALOR EN STRING SI ES 0 ENTONCES -'STRING' Y SI ES 1 APENAS EL STRING

listaliterales = []	
'''for interps in listainterpsverdad:

	cont += 1
	if(interps in listainterpsverdad):
		listaliterales.append(interps)
		dibujar_tablero(listaliterales, cont)
	else:
		listaliterales.append('-' + interps)
'''
	
	
	
	
	
	
