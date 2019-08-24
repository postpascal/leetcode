class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        a={}
        s=""
        n=""

        if numerator * denominator<0:
            n="-"
        numerator=abs(numerator)
        denominator=abs(denominator)
        l=n+str(numerator//denominator)
        if numerator%denominator==0:
            return l

        numerator=numerator%denominator
        while numerator%denominator !=0:
            numerator=numerator*10
            if numerator in a:
                d=a[numerator]
                s=s[:d]+"("+s[d:]+")"
                return l+"."+s

            a[numerator]=len(s)
                
            while numerator<denominator:
                numerator=numerator*10
                s=s+"0"
                a[numerator]=len(s)
                
            t=numerator//denominator
            s=s+str(t)

            numerator=numerator%denominator

        return l+"."+s


a=Solution()
print(a.fractionToDecimal(-50,8))