class Solution:
	def myPow(self, x: float, n: int):
		if n==0:
			return 1
		if n<0:
			n=-n
			x=1/x

		def logpower(x,n):
			t=1
			r=x
			if n==1:
				return x
			while t<n:
				if 2*t<=n:
					r=r*r
					t=t*2
				else:
					r=r*logpower(x,n-t)
					break
			return r
		return logpower(x,n)


a=Solution()
print(a.myPow(-3,3))