class Solution:
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if x <0:
			return False
		n=10
		c=0
		while x//n:
			
			ind= x%n//(n/10)
			c=c*10 +ind  
			n *=10
		c=c*10+x//(n/10)
		return c==x