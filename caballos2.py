#Caballos logica para ciencias de la computacion

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage

#---------------------------------------------------------------------------------NOTACION POLACA Y POLACO INVERSO------------------------------------------------------------------------------------------#

conectivos=['Y','O','-','>']

niveles = []
def main(formula):
        if(len(formula)>1):
                contador = 0
                for a in range(0,len(formula)):
                        if(formula[a]=='('): contador += 1
                        elif(formula[a]==')'): contador -= 1
                        niveles.append(contador)
                
                for b in range(0, len(niveles)):
                        if((niveles[b]==0) and (formula[b] in conectivos)):
                                if((formula[b]=='-')):
                                        if(not(formula[b+1]=='(')): continue
                                        else:
                                                niveles.clear()
                                                return b
                                else:
                                        niveles.clear()              
                                        return b

                for c in range(0, len(formula)):
                        if(formula[c] in conectivos):			
                                niveles.clear()
                                return c
        return 0	
        

def polaco(formula):
        if(len(formula)<=2): return formula
        elif(not(main(formula))):
                derecha = ""
                for b in range(2, len(formula)-1):
                        derecha+=formula[b]

                return formula[main(formula)] + polaco(derecha)
            
        else:
                izquierda = ""
                derecha = ""
			
                for a in range(0, main(formula)):
                        izquierda+=formula[a]		

                for b in range(main(formula)+1, len(formula)):
                        derecha+=formula[b]

                izquierda_nueva = izquierda
                derecha_nueva = derecha

                if(izquierda[0]=='(' and izquierda[len(izquierda)-1]==')'):
                        izquierda_nueva = ""
                        for a in range(1, len(izquierda)-1):
                                izquierda_nueva+=izquierda[a]		

                if(derecha[0]=='(' and derecha[len(derecha)-1]==')'): 
                        derecha_nueva = ""
                        for b in range(1, len(derecha)-1):
                                derecha_nueva+=derecha[b]		

                return formula[main(formula)] + polaco(izquierda_nueva) + polaco(derecha_nueva)
        


def polacoInverso(Polaco):
	PolacoInverso = ""
	for a in range(1, len(Polaco) + 1):
		PolacoInverso += Polaco[-a]

	return PolacoInverso

#-------------------------------------------------------------------------------------------STRING TO TREE--------------------------------------------------------------------------------------------------#

letrasProposicionales=['1','2','3','4','5','6','7','8','9']

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label


def StringtoTree(stringChain):
        print(stringChain)
        pila = []
        for c in stringChain:
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


def Inorder(f):
        if f.right == None:
                return f.label
        elif f.label == '-':
                return f.label + Inorder(f.right)
        else:
                return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

#-------------------------------------------------------------------------------------------RULES GENERATION AREA-------------------------------------------------------------------------------------------#

#HORSES CASE
#REGLA 1(DEBEN HABER EXACTAMENTE TRES(3) CABALLOS EN EL TABLERO)
conjunciones = [""]
def regla1(recolector, limite, lista):
        if(limite == 0):
                for a in range(0,len(lista)-1):
                        recolector = '(' + recolector + 'Y' + '-' + lista[a] + ')'
                recolector+= 'Y' + '-'+lista[len(lista)-1]
                #print(recolector)
                if(conjunciones[0]==""): conjunciones[0] = recolector
                else: conjunciones[0] = '(' + conjunciones[0] + ')' + 'O' + '(' + recolector + ')'
        else:
                for a in range(0, len(lista)):
                        elemento = lista[a]
                        lista.pop(a)
                        if(recolector==""): regla1(elemento,(limite-1),lista)
                        else: regla1(('(' + recolector+ 'Y' + elemento + ')'),(limite-1),lista)
                        lista.insert(a,elemento)


#REGLA 2(NINGUN CABALLO DEBE ATACAR A OTRO)
regla2 = "((((((((1>-8)Y(1>-6))Y((2>-7)Y(2>-9)))Y((3>-4)Y(3>-8)))Y((4>-3)Y(4>-9)))Y((6>-1)Y(6>-7)))Y((7>-2)Y(7>-6)))Y((8>-1)Y(8>-3)))Y((9>-2)Y(9>-4))"

#---------------------------------------------------------------------------------------INTERPRETATIONS GENERATOR-------------------------------------------------------------------------------------------#

interps = []
aux = {}

def findInterpretations():
        for a in letrasProposicionales:
                aux[a] = 1 
        interps.append(aux)
        
        for a in letrasProposicionales:
                interps_aux = [i for i in interps]
                
                for i in interps_aux:
                        aux1 = {}
                        for b in letrasProposicionales:
                                if a== b: aux1[b] = 1 - i[b]
                                else: aux1[b] = i[b]
                        interps.append(aux1)

#--------------------------------------------------------------------------------------TRUTH VALUES EVALUATION----------------------------------------------------------------------------------------------#

def mayor(a, b):
	mayor = b
	if(a>b):
		mayor = a
	return mayor

def VI(A,i):
	if A.label in letrasProposicionales:
		return i[A.label]
	elif A.label == '-':
		return 1 - VI(A.right,i)
	elif A.label == 'Y':
		return VI(A.left,i) * VI(A.right,i)
	elif A.label == 'O':
		return mayor(VI(A.left,i), VI(A.right,i))
	elif A.label == '>':
		return mayor(1 - VI(A.left,i) , VI(A.right,i))


"""¿¿¿WHATS THE BUG???

def TruthValues(Tree,diccionary):
        if(Tree.right == None): 
                print(diccionary[Tree.label])		
                return diccionary[Tree.label]  
        elif(Tree.label == '-'): return 1 - TruthValues(Tree.right,diccionary)
        elif(Tree.label == 'Y'): return TruthValues(Tree.right,diccionary) * TruthValues(Tree.left,diccionary)
        elif(Tree.label == 'O'):
                if(TruthValues(Tree.right,diccionary) > TruthValues(Tree.left,diccionary)): return TruthValues(Tree.right,diccionary)
                else: return TruthValues(Tree.left,diccionary)
        elif(Tree.label == '>'):
                if(TruthValues(Tree.right,diccionary) > TruthValues(Tree.left,diccionary)): return TruthValues(Tree.right,diccionary)
                else: return 1 - TruthValues(Tree.left,diccionary)
        else: print("¡ERROR!")
"""

#-----------------------------------------------------------------------------GRAFICACION DE CABALLOS SOBRE EL TABLERO-------- -----------------------------------------------------------------------------#

def dibujar_tablero(f, n):
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    step = 1./3
    tangulos = []
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

    for j in range(3):
        locacion = j * step
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],\
                facecolor='black'))
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],\
                facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    arr_img = plt.imread("caballo.png", format='png')
    imagebox = OffsetImage(arr_img, zoom=0.1)
    imagebox.image.axes = axes

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

    for key in f:
        if f[key]==1:
            ab = AnnotationBbox(imagebox, direcciones[int(key)], frameon=False)
            axes.add_artist(ab)

    fig.savefig("tablero_" + str(n) + ".png")


#------------------------------------------------------------------------------------------BEGINNING OF EXECUTION------------------------------------------------------------------------------------------#

numCaballos = 3
regla1("",numCaballos,letrasProposicionales)

conjunciones[0] = '(' + conjunciones[0] + ')' + 'Y' + '(' + regla2 + ')' 
conjunciones[0] = '(' + conjunciones[0] + ')' + 'Y' + '2'
conjunciones[0] = '(' + conjunciones[0] + ')' + 'Y' + '6'


print(conjunciones[0])

formula = conjunciones[0]

polaco = polaco(formula)

polacoInverso = polacoInverso(polaco)

#print("INPUT Formula: " + formula)
print("Notacion polaca: " + polaco)
print("Notacion polaca inversa: " + polacoInverso)

GeneratedTree = StringtoTree(polacoInverso)
OriginalFormula = Inorder(GeneratedTree)
#print("OUTPUT Formula: " + OriginalFormula)

findInterpretations()
#print(interps)

cont = 0
for i in interps:
        if(VI(GeneratedTree, i)):
                dibujar_tablero(i, cont)
                cont+=1
                #print(VI(GeneratedTree, i))        

print(cont)
print("¡DONE!")

