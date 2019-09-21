class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        for i in range(32):
            s=s+(n&1)
            n=n>>1
        return s