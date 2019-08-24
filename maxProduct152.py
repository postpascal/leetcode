class Solution:
    def maxProduct(self, nums):
        if len(nums) == 1: return nums[0]
        pos = neg = 0
        ans = -sys.maxsize-1
        for n in nums:
            if n > 0:
                pos, neg = max(n, n*pos), min(0, n*neg)
            else:
                pos, neg = max(0, n*neg), min(n, n*pos)
            ans = max(pos, ans)
        return ans

a=Solution()
print(a.maxProduct([-2,1,3,-3]))