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





# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         l=len(nums)
#         for i in range(1,len(nums)):
#             if nums[i]<nums[i-1]:
#                 l=i
#                 break

#         r=-1
#         for i in range(len(nums)-2,-1,-1):
#             if nums[i]>nums[i+1]:
#                 r=i
#                 break

#         if r==-1: return 0
#         if r<l:
#             l,r=r,l
#         ma=nums[l]
#         mi=nums[l]
#         for i in range(l,len(nums)):
#             if nums[i]<mi:
#                 mi=nums[i]
#         for i in range(r+1):
#             if nums[i]>ma:
#                 ma=nums[i]
#         li=l
#         ri=r
                
#         for i in range(0,l+1):
            
#             if nums[i]>mi:
#                 li=i
#                 break
#         for i in range(len(nums)-1,r-1,-1):
#             if nums[i]<ma:
#                 ri=i
#                 break
#         return ri-li+1