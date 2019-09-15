class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic=collections.defaultdict(int)
        for i in nums:
            dic[i]=dic[i]+1
            
        return sorted(dic,key=lambda x:dic[x],reverse=True)[:k]