class Solution(object):
	def permute(self, nums):
		def rehelper(s):
			if(len(s) == 0):
				return [[]]
			else:
				r=[]
				for i in range(len(s)):
					for j in rehelper(s[:i]+s[i+1:]):
						r.append(j+[s[i]])
			return r
		return rehelper(nums)

a=Solution()
print(a.permute([1,2,3]))