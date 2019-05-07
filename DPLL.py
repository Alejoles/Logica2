
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
            if(Unidad in i):
                S.remove(i)
            elif(Complemento(Unidad) in i):
                i.remove(UnidadComp)
            I[LetraFromLit(Unidad)] = 1
            I[Complemento(Unidad)] = 0

        l = ClausulaUni(S)
    Unit = [S,I]
    return Unit

S = [['p', '-s'], ['q', 'r'], ['-p'],['q', 't'], ['s']]
I = {}
print(unitP(S,I))


def DPLL(S,I):
    #S, Conjunto de clausulas
    #I, Interpretacion parcial
    unitP(S,I)
    for i in S:
        if(len(i) == 0):
            return "Insatisfacible" , '{}'
        elif(len(S) == 0):
            return "Satisfacible" , I











print(DPLL(S,I))
