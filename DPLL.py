
def NoEmptyCl(S):
        for i in S:
                if(len(i)<1):
                    return False
        return True

def ClausulaUni(S):
    for i in S:
            if (len(i)==1):
                return i
    return ''

def LetraFromLit(L):
    if(L[0] == '-'):
        return L.replace('-', '')
    else:
        return L

def Complemento(L):
    if(L[0] == '-'):
        return L.replace('-', '')
    else:
        return '-' + L

def unitP(S,I):
    #S, Conjunto de clausulas
    #I, Interpretacion Parcial
	l = ClausulaUni(S)
	while(NoEmptyCl(S) and l!=''):
		Unidad = l[0]
		UnidadComp = Complemento(Unidad)
		for i in S:
			if(Complemento(Unidad) in i):
				i.remove(UnidadComp)
			elif(Unidad in i):
				S.remove(i)
			I[LetraFromLit(Unidad)] = 1
			#I[Complemento(Unidad)] = 0

		l = ClausulaUni(S)
	return S, I

S = [['p','-q','r'], ['-p','q','-r'], ['-p', '-q', '-r']]
I = {}


def DPLL(S,I):
    #S, Conjunto de clausulas
    #I, Interpretacion parcial
	unitP(S,I)
	for i in S:
		if(len(i) == 0):
			return "Insatisfacible" , '{}'
	if(len(S) == 0):
		return "Satisfacible" , I
	L = S[0][0]
	SP = S
	for i in SP:
		if(L in i):
			SP.remove(i)
		elif(Complemento(L) in i):
			i.remove(Complemento(L))
	IP = I
	IP[L] = 1
	#IP[Complemento(L)] = 0
	if(DPLL(SP,IP) == "Satisfacible" , IP):
		return "Satisfacible" , IP
	else:
		SPP = S
		LP = Complemento(L)
		for i in SPP:
			if(LP in i):
				SPP.remove(i)
			elif(Complemento(LP) in i):
				i.remove(Complemento(LP))
		IPP = I
		IPP[LP] = 1
		return DPLL(SPP,IPP)




print(DPLL(S,I))
