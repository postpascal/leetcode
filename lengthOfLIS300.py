class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)




print(a.lengthOfLIS('23'))