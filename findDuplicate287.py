class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while True:
            if nums[nums[0]]==nums[0]:
                return nums[0]
            nums[nums[0]],nums[0]=nums[0],nums[nums[0]]


a=Solution()
print(a.findDuplicate([1,3,4,2,2]))