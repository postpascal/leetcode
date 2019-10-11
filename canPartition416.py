# class Solution(object):
#     def canPartition(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         s=0
#         for i in nums:
#             s=s+i
#         if s%2==1:
#             return False
#         else:
#             k=s/2
		
#         def helper(sk,ind):
#             if sk==0:
#                 return True
#             elif sk<0:
#                 return False
				
#             for i in range(ind,len(nums)):
#                 if helper(sk-nums[i],i+1):
#                     return True
#             return False
		
#         return helper(k,0)

class Solution:
    def canPartition(self, nums):
        if sum(nums)%2: return False
        target = int(sum(nums) / 2)
        vallist = [True] + [False] * target
        for num in nums:
            for v in range(target, num-1, -1):
                vallist[v] = vallist[v] or vallist[v - num]
            if vallist[target]: return True
        return False