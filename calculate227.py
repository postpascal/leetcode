class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        l=[]
        start=0
        ng=1
        for i,v in enumerate(s):
            if v in ['+','-','*','/']:
                l.append(ng*int(s[start:i]))
                ng=1
                if v in ["*","/"]:
                    l.append(v)
                start=i+1
                if v=="-":
                    ng=-1
        l.append(ng*int(s[start:]))


        for i in range(1,len(l)-1):
            if l[i] =="*":
                l[i-1:i+2]=[0,0,l[i-1]*l[i+1]]
            elif l[i]=="/":
                if l[i-1]<0:
                    l[i-1:i+2]=[0,0,-(-l[i-1]//l[i+1])]
                else:
                    l[i-1:i+2]=[0,0,l[i-1]//l[i+1]]

        return sum(l)




a=Solution()
print(a.calculate("3+2*2"))