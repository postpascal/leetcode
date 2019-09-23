class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i]!=i and nums[i]<len(nums):
                nums[nums[i]],nums[i]=nums[i],nums[nums[i]]
                
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)