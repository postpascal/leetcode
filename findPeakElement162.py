# class Solution(object):
#     def findPeakElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums)==1:
#             return 0

#         if nums[0]>nums[1]:
#             return 0
#         elif nums[len(nums)-1]>nums[len(nums)-2]:
#             return len(nums)-1

#         for i in range(1,len(nums)-1):
#             if nums[i]> nums[i-1] and nums[i]> nums[i+1]:
#                 return i 


class Solution:
    def findPeakElement(self, nums):
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[m+1]:
                r=m
            else:
                l=m+1
        return l


a=Solution()
print(a.findPeakElement([5,6,3,1,2]))