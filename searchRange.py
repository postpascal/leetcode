class Solution:
	def searchRange(self, nums, target):
		def refind(l,r,target):
			if (r+l)%2==0:
				t=int((r+l)/2)
			else:
				t=int((r+l+1)/2)

			if r-l<2:
				if nums[l]==target and nums[r]>target:
					return [l,l]
				elif nums[l]<target and nums[r]==target :
					return [r,r]
				else:
					return [-1,-1]

			if nums[t]==target:
				if nums[l]==target:
					return refind(t,r,target)
				elif nums[r]==target:
					return refind(l,t,target)
				else:
					a,_=refind(l,t,target)
					b,_=refind(t,r,target)

			elif nums[t]>target:
				return refind(l,t,target)
			else:
				return refind(t,r,target)
			return a, b

		if len(nums)<1:
			return [-1,-1]
		if nums[0]>target or nums[-1]<target:
			return [-1,-1]

		e=refind(0,len(nums)-1,target)

		if nums[0]==target:
			e[0]=0
		if nums[-1]==target:
			e[-1]=len(nums)-1

		return e

a=Solution()
print(a.searchRange([1,2,2],2))
