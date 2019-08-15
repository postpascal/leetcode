class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		d = {}
		def helper(m,n):
			if 0 in (m,n):
				return 1
			if (m,n) in d:
				return d[(m,n)]
			d[(m,n)] = helper(m-1,n)+helper(m,n-1)
			return d[(m,n)]
		
		res=helper(m-1,n-1)
		return res

a=Solution()
print(a.uniquePaths(7,3))