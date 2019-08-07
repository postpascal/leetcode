class Solution:
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if nums==[]:
			return 0
		n=-1
		
		while True:
			for j in range(n+1,len(nums)):
				n=j
				if nums[j] in nums[:j]:
					del nums[j]
					n=n-1
					break
			if n+1==len(nums):
				return len(nums)
