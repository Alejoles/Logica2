#Lista de hojas de un arbol
#Si cada hoja se ve en sí misma como una lista de formulas se desarrolla el algoritmo de construccion de tableaux es una lista de listas de formulas

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

def imprime_hoja(H):
	cadena = "["
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "]"


def imprime_tableau(tableau):
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


def Par_Complementario(ListaC):
	#ListaC es una lista de Arboles
	for i in range(len(ListaC)):
		for j in range (i+1,len(ListaC)):
			II = ListaC[i]
			JJ = ListaC[j]
			print("1: " + Inorder(II))
			print('2: ' + Inorder(JJ))
			if(JJ.label == '-'):
				if (JJ.right.label == II.label):
					return 0
			elif(II.label == '-'):
				if(II.right.label == JJ.label):
					return 0
	return 1
	
def Ver_Lit(A):
	#A es una formula, chequeamos si A es un literal
	if(A.label in letrasProposicionales):
		return 0
	elif(A.label == '-'):
		if(A.right.label in letrasProposicionales):
			return 0
		else:
			return 1
	else:
		return 1

def Ver_Formula(H):
	#H lista de formulas, verificar si hay alguna formula que no es literal
	for i in range(len(H)):
		if(Ver_Lit(H[i]) == 0):
			return 1
		else:
			return 0
	

		
P = StringtoTree('p', letrasProposicionales)
Q = StringtoTree('q', letrasProposicionales)
noQ = StringtoTree('q-', letrasProposicionales)
B = StringtoTree('qpO-', letrasProposicionales)
C = StringtoTree('p-qYpY', letrasProposicionales)
#t = [[Q, A], [B, P]]
F = [P,Q]
#H = [A,B]
PRR = [C]

#print(imprime_hoja(F))

print(Par_Complementario(PRR))
print(Ver_Lit(B))
print(Ver_Formula(F))




