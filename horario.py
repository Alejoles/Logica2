#Horario logica

Pila = []
Conectivos = ['O','Y','>']
Negacion= ['-']
LetrasProposicionales = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","P","Q"] #Crear las letras proposicionales
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

R1 = "P-M>" + "M-P>" + "Y"
R2 = "Q-N>" + "N-Q>" + "Y"
R= R1 + R2 + "Y"

#REGLA2 LOGICA1 EXACTAMENTE 2 SESIONES
for Z in LetrasProposicionales:
	Aux1 = [x for x in LetrasProposicionales if x!=Z] #todas las LetProp excepto A
	for W in Aux1:
		Literal = Z + W + 'Y'
		Aux2 = [x + '-' for x in Aux1 if x!=W]
		for k in Aux2:
			Literal = k + Literal + 'Y'
			if Inicial:
				Conjunciones = Literal
				Inicial = False
			else:
				Conjunciones = Literal + Conjunciones + 'O'
				
for U in LetrasProposicionales:
	Aux1 = [x for x in LetrasProposicionales if x!=U] #todas las LetProp excepto A
	for V in Aux1:
		Literal = V + U + 'Y'
		Aux2 = [x + '-' for x in Aux1 if x!=V]
		for k in Aux2:
			Literal = k + Literal + 'Y'
			if Inicial:
				Conjunciones = Literal
				Inicial = False
			else:
				Conjunciones = Literal + Conjunciones + 'O'


					

#--------------------------------------------------------------------------------
#REGLA3

K1 = "D-A>" + "G-A>" + "J-A>" + "Y" + "Y"
K11 = "A-D>" + "G-D>" + "J-D>" + K1 + "Y" + "Y" + "Y"
K2 = "E-B>" + "H-B>" + "K-B>" + "Y" + "Y"
K22 = "B-E>" + "H-E>" + "K-E>" + K2 + "Y" + "Y" + "Y"
K3 = "F-C>" + "I-C>" + "L-C>" + "Y" + "Y"
K33 = "C-F>" + "I-F>" + "L-F>" + K3 + "Y" + "Y" + "Y"
K4 = "J-G>" + "A-G>" + "D-G>" + "Y" + "Y"
K44 = "G-J>" + "D-J>" + "A-J>" + K4 + "Y" + "Y" + "Y"
K5 = "K-H>" + "E-H>" + "B-H>" + "Y" + "Y"
K55 = "H-K>" + "E-K>" + "B-K>" + K5 + "Y" + "Y" + "Y"
K6 = "L-I>" + "F-I>" + "C-I>" + "Y" + "Y"
K66 = "I-L>" + "F-L>" + "C-L>" + K6 + "Y" + "Y" + "Y"
K = K11 + K22 + K33 + K44 + K55 + K66 + "Y" + "Y" + "Y" + "Y" + "Y"
#----------------------------------------------------------------------------------
#REGLA4

J1 = "FLODJOO-NMO>"
J2 = "HEOFLOO-PQO>"
J = J1 + J2 + "Y"


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
RRR = R + J + K + "Y" + "Y"

A = String2Tree(RRR, LetrasProposicionales)
for j in interps:
	if(VI(A,j) == 1):
		listainterpsverdad.append(j)

print(len(listainterpsverdad))

