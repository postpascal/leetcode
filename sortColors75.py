class Solution:
	def sortColors(self, nums):
		i1=len(nums)
		l=0
		r=len(nums)-1
		while l<=r:
			if nums[l]==2:
				while nums[r]==2 and l<r:
					r-=1
				nums[r],nums[l]=nums[l],nums[r]

			if nums[l]==1:
				if l<i1:
					i1=l

			if nums[l]==0 and i1<len(nums):
				nums[l],nums[i1]= nums[i1],nums[l]
				i1+=1
			l+=1
		return nums


a=Solution()

print(a.sortColors([0,0,2,1,1,0]))