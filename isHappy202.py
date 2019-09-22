class Solution:
    def isHappy(self, n: int) -> bool:
        d={}
        while n!=1:
            if n in d:return False
            d[n]=0
            s=0
            while n>0:
                s=(n%10)**2+s
                n=n//10
            n=s
        return True