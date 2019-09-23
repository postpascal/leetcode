class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        maxPower = 3**(int(math.log(2**31-1, 3)))
    
        return n > 0 and maxPower % n == 0