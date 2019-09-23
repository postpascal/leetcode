class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=0
        for i in range(len(nums)):
            if nums[i]==0:
                n=n+1
                continue
            nums[i-n]=nums[i]
            if n>0:nums[i]=0