class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(b)>len(a):
            a="0"*(len(b)-len(a))+a
        else:
            b="0"*(len(a)-len(b))+b

        c=0
        r=""
        print(a,b)

        for i in range(-1,-len(a)-1,-1):
            s=int(a[i])+int(b[i])+c
            print(r)
            if s==3:
                c=1
                r="1"+r
            elif s==2:
                c=1
                r="0"+r
            elif s==1:
                c=0
                r="1"+r
            else:
                c=0
                r="0"+r
        if c>0:
            return "1"+r
        else:
            return r

a=Solution()
print(a.addBinary("11","1"))