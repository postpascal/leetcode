class Solution:
	def canJump(self, nums):
		maxi=0
		for i in range(len(nums)-1):
			if nums[i]==0:
				if nums[maxi]-i+maxi>0:
					continue
				else:
					return False

			if nums[i]+i-maxi>=nums[maxi]:
				maxi=i
		return True

		



a=Solution()
print(a.canJump([2,0,0]))