class Solution:
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		a=str(x)
		if x<0:
			d=list(reversed(a[1:]))
			ans = -int(''.join(d))
		else:
			d=list(reversed(a))
			ans = int(''.join(d))
		if x>2147483648 or x<-2147483648:
			return 0
		if ans>2147483648 or ans<-2147483648:
			return 0
		return ans
		