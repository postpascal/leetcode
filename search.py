class Solution:
	def search(self, nums, target):
		def refind(l,r,target):
			if (r+l)%2==0:
				t=int((r+l)/2)
			else:
				t=int((r+l+1)/2)
			if nums[t]==target:
				return t

			if r-l<2:
				if nums[l]==target:
					return l
				elif nums[r]==target:
					return r
				else:
					return -1

			if nums[l]<=target and target<nums[t]:

				return refind(l,t,target)
			elif nums[t]<target and target<=nums[r]:
				return refind(t,r,target)
			elif nums[l]>=nums[t]:
				return refind(l,t,target)
			elif nums[t]>=nums[r]:
				return refind(t,r,target)
			return -1
		if len(nums)<1:
			return -1
		e=refind(0,len(nums)-1,target)
		return e

a=Solution()
print(a.search([1,3,5],0))
