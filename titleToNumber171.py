class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        c=1
        for i in s[::-1]:
            l=ord(i)-64
            ans=ans+l*c
            c=c*26
        return ans