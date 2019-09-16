class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            while 90<ord(s[l])<97 or 57<ord(s[l])<65 or ord(s[l])>122 or ord(s[l])<48:
                l=l+1
                if l>=r:
                    return True
            while 90<ord(s[r])<97 or 57<ord(s[r])<65 or ord(s[r])>122 or ord(s[r])<48:
                r=r-1
                if l>=r:
                    return True
            if ord(s[r])-ord(s[l])==0:
                l=l+1
                r=r-1
            elif ord(s[r])-ord(s[l]) in [32,-32] and ord(s[l])>57 and ord(s[r])>57:
                l=l+1
                r=r-1
            else:
                return False
        return True