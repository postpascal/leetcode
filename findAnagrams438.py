class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        r=[]
        l=[0]*26
        samp=[0]*26
        k=len(p)
        for i in p:
            samp[ord(i)-97]=samp[ord(i)-97]+1
        for i in s[:len(p)]:
            l[ord(i)-97]=l[ord(i)-97]+1
        if l==samp:
            r.append(0)
            
        for i in range(k,len(s)):
            l[ord(s[i])-97]=l[ord(s[i])-97]+1
            l[ord(s[i-k])-97]=l[ord(s[i-k])-97]-1
            if l==samp:
                r.append(i-k+1)
        return r