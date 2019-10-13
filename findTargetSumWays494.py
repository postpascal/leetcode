class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        k=sum(nums)-S
        if k%2==1 or k<0:
            return 0
        else:
            k=k/2
            
        dp=[1]+[0]*k
        for i in nums:
            for j in range(k,i-1,-1):
                if dp[j]==0 and dp[j-i]!=0:
                    dp[j]=dp[j-i]
                elif dp[j]!=0 and dp[j-i]!=0:
                    dp[j]=dp[j]+dp[j-i]
        return dp[-1]