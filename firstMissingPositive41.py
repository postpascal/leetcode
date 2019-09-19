class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        for i in range(l):
            while 0<nums[i]<=l and nums[i]!=i+1 and nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
                
        for i in range(l):
            if nums[i]!=i+1:
                return i+1
        return l+1