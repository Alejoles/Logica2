


def Tseitin(A, LetrasProposicionalesA):
	LetrasProposicionalesB = [str(x) for x in range(1,100)]
	L = [] # Conjunciones
	Pila = []
	I = -1
	s = A[0]
	while(len(A)>0):
		if(s in LetrasProposicionalesA and len(Pila)>0 and Pila[-1] == '-'):
			I+=1
			Atomo = LetrasProposicionalesB[I]
			Pila = Pila[:-1]
			Pila.append(Atomo)
			L.append(Atomo + '>' + '-' + s + 'Y' + '-' + s + '>' + Atomo)
			A = A[:1]
			s = A[0]
		elif(s == ')'):
			w = Pila[-1]
			O = Pila[-2]
			v = Pila[-3]
			Pila = Pila[len(Pila)-4]
			I+=1
			Atomo = LetrasProposicionalesB[I]
			L.append(Atomo + '>' + (vOw) + 'Y' + (vOw) + '>' + Atomo)
			s = Atomo
		else:
			Pila.append(s)
			A = A[:1]
			s = A[0]
	B = ''
	if(I<0):
		Atomo = Pila[-1]
	else:
		Atomo = LetrasProposicionalesB[I]
	for X in L:
		Y = X
		B += 'Y' + Y
	B = Atomo + B
	return B
			
LetrasProposicionalesA = ['p']
A = 'p'

print(Tseitin(A, LetrasProposicionalesA))


def Tclausulas(C):
	# C una clausula como lista de caracteres
	L = []
	s = C[0]
	while(len(C)>0):
		if(s == 'O'):
			C = C[1:]
		elif(s == '-'):
			literal = s + C[1]
			L.append(literal)
			C = C[2:]
		else:
			L.append(s)
			C = C[1:]
		s = C[0]
	return L

def ObtClausal(A):
	#A, una formula en FNC como cadena de caracteres
	l = []
	i = 0
	while(len(A)>0):
		if(A[i] == 'Y'):
			L.append(Tclausulas(A[:i]))
			A = A[i+1:]
		else:
			i+=1
	return L
			


"""
a = 'pOqY--aOb->kOl'

def negacion(a):
	a = a.replace('--', '')
	return a
	
negacion(a)

print(negacion(a))

"""
