#Lista de hojas de un arbol
#Si cada hoja se ve en sí misma como una lista de formulas se desarrolla el algoritmo de construccion de tableaux es una lista de listas de formulas

from random import choice

ListaLiterales = []
letrasProposicionales = ['p', 'q']

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def imprime_hoja(H): #Lista de formulas
	cadena = "["
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "]"


def imprime_tableau(tableau): #Lista de listas de formulas
	primero = True
	for H in tableau:
		if primero == True:
			cadena = '[' + imprime_hoja(H)
			primero = False
		else:
		 cadena += ", " + imprime_hoja(H)
	return cadena + "]"

	
def StringtoTree(A, letrasProposicionales):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree
    conectivos = ['O', 'Y', '>']
    pila = []
    for c in A:
        if c in letrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c == '-':
            formulaAux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formulaAux)
        elif c in conectivos:
            formulaAux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formulaAux)
    return pila[-1]


def Par_Complementario(Lista):
	#Lista es una lista de literales
	for i in range(len(Lista)):
		a = Inorder(Lista[i])
		for j in range(i+1,len(Lista)):
			b = Inorder(Lista[j])
			print("primera lista: " + a)
			print(b)
			if('-' + a == b):
				return 1
				break
			elif(a == '-'+b):
				return 1
	return 0
		
	
def Ver_Lit(A):
	#A es una formula, chequeamos si A es un literal
	if(A.label in letrasProposicionales):
		return 1
	elif(A.label == '-'):
		return Ver_Lit(A.right)
	else:
		return 0

def Ver_Formula(H):
	#H lista de formulas, verificar si hay alguna formula que no es literal
	for i in range(len(H)):
		if(Ver_Lit(H[i]) == 0):
			return 1
		else:
			return 0
			
	
def interps_verd(H): #
	#H Lista de listas de literales que devuelve una lista llamada listaInterpsVerdad con las listas en h que no tienen pares complementarios

	

#---------------------------------------------------------------------------
#----------------------------PARAMETROS NECESARIOS-------------------------


		
P = StringtoTree('p', letrasProposicionales)
Q = StringtoTree('q', letrasProposicionales)
noQ = StringtoTree('q-', letrasProposicionales)
noP = StringtoTree('p-', letrasProposicionales)
B = StringtoTree('qpO-', letrasProposicionales)
C = StringtoTree('p-qYpY', letrasProposicionales)
PRR = [B, C]
	

T = [[Q,P], [B,C], [P, noP]]

#---------------------------EJECUCION------------------------------------


while(len(T) != 0):
	#T Lista de listas de formulas
	for i in T:
		
		if(Ver_Formula(i) == 0): #contiene solo literales?
			if(Par_Complementario(i) == 1):
				print(imprime_hoja(i))
				print("Cerrada")
				T.remove(i)
			elif(Par_Complementario(i) == 0):
				print(imprime_hoja(i))
				print("Abierta")
				T.remove(i)
		else: #solo literales
			if(Ver_Formula(i) == 1):
				print(imprime_hoja(i))
				T.remove(i)
			






























