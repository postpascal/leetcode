class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def hepler(s,sl,sr):
            d=0
            while sl>=0 and sr<len(s):
                if s[sl]!=s[sr]: break
                sl-=1
                sr+=1
                d=d+1
            return d

        c=0
        for i in range(1,len(s)):
            odd = hepler(s, i-1, i+1)
            even = hepler(s, i-1, i)
            c=c+odd+even
        return c+len(s)