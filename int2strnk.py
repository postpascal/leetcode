# n=346
# k=25

def getstr(n,rk):
	sn=str(n)
	m=0
	d="9"
	while int(d)>0:
		if sn[0]<d:
			m=0
			l=len(sn)-1
			for ind in range(l):
				m=m+10**ind
		elif sn[0]==d:
			l=len(sn)-1
			m=n-int(sn[0]+"0"*l)+1
			for ind in range(l):
				m=m+10**ind
		else:
			m=0
			l=len(sn)
			for ind in range(l):
				m=m+10**ind
				
		if rk-m==0:
			return d
		elif rk-m<0:
			break
		else:
			rk=rk-m
			m=0
			d=str(int(d)-1)

	d=d+getstr(n-int(sn[0]+"0"*l),rk)
	return d

n=15
k=4
print(getstr(n,n-k+1))