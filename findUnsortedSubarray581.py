class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=sorted(nums)
        i=0
        while i<len(nums) and nums[i]==b[i]:
            i=i+1
        j=len(nums)-1
        while j>=0 and nums[j]==b[j]:
            j=j-1
        if i>j:
            return 0
        else:
            return j-i+1