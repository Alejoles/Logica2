

S = ['pr', 'qr','-pst' , 'pq-r', 'pst']

def Res(C1,C2):
	# C1, C2, par de clausulas no marcadas que conflictuan
	for i in range(len(C1)):
		for j in range(len(C2)):
			if((C1[i] == C2[j] and C2[j-1] == '-')):
				C2 = C2.replace(C2[j], '')
				C2 = C2.replace(C2[j-1], '')
				return C2
			elif((C1[i]  == C2[j] and C1[i-1] == '-')):
				C1 = C1.replace(C1[i], '')
				C1 = C1.replace(C1[i-1], '')
				return C1
				
				
Res(S[3], S[4])
print(S)
def Conflicto(S):
	x = 0
	for i in S:
		for k in range(len(i)):
			for l in range(len(i)):
				if((i[k] == i[l] and i[l-1] == '-')):
					print(S[l])
					print(i)
					return True
				elif((i[k]  == i[l] and i[k-1] == '-')):
					print(S[l])
					print(i)
					return True
		x+=1

def Resolucion(S):
	# S, conjunto de clausulas(sin clausulas triviales)
	while(Conflicto(S)):
		print()

Conflicto(S)

















	
