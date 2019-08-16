class Solution:
	def subsets(self, nums):
		def traversallist(l):
			r=[]
			if l==0:
				return [[],[nums[0]]]
			for x in traversallist(l-1):
				r.append(x+[])
				pass

			for j in traversallist(l-1):
				r.append(j+[nums[l]])
			return r
		z=traversallist(l=len(nums)-1)
		return z

a=Solution()
print(a.subsets([1,2,3]))