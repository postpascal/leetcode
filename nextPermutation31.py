class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2: return nums
        i=len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i=i-1
        if i==-1:
            nums[:]=nums[::-1]
        else:

            j=len(nums)-1
            while nums[i]>=nums[j]:
                j=j-1
            nums[i],nums[j]=nums[j],nums[i]
            nums[i+1:]=nums[i+1:][::-1]