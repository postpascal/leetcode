#a=int[], a[i]<a[i+1]
#find x,y in a which make x+y=K


a=[1,3,5,6,8,9,12,23,44,67,90]



def sumk(a,k):
	l=0
	r=len(a)-1
	while l<r:
		if a[l]+a[r]<k:
			l=l+1
		elif a[l]+a[r]>k:
			r=r-1
		else:
			return l, r

	return -1
print(sumk(a,90))
