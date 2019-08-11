class Solution:
	def threeSum(self, nums):
		nums.sort()
		re=[]

		if len(nums)<3:
			return []
		i0=nums[0]-1
		for i in range(len(nums)):
			if nums[i]>0:break
			if i0==nums[i]:
				continue
			i0=nums[i]

			l,r=i+1,len(nums)-1
			while l<r:
				s=nums[i]+ nums[l]+nums[r]
				if s>0:
					m=nums[r]
					while nums[r]==m and l<r:
						r=r-1
				elif s<0:
					m=nums[l]
					while nums[l]==m and l<r:
						l=l+1
				else:
					re.append([nums[i],nums[l],nums[r]])
					m=nums[r]
					while nums[r]==m and l<r:
						r=r-1

		return re



a=Solution()
print(a.threeSum([-2,0,0,2,2]))