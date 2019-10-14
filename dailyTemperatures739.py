class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        r=[0]*len(T)
        i=len(T)-2
        
        while i >=0:
            c=i+1
            while T[c]<=T[i] and r[c]>0:
                c=c+r[c]
            if T[c]>T[i]:
                r[i]=c-i
            else:
                r[i]=0
            i=i-1
        return r