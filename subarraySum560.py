class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic={0:1}
        s=0
        r=0
        for i in range(len(nums)):
            s=s+nums[i]
            if s-k in dic:
                r=r+dic[s-k]
            if s in dic:
                dic[s]=dic[s]+1
            else:
                dic[s]=1
        return r