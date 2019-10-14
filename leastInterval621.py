class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic={}
        for i in tasks:
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        
        d=dic.values()
        d.sort()
        ws=sum(d)
        lm=d.pop()
        s=(lm-1)*(n+1)+1
        while d and lm==d.pop():
            s=s+1
            
        return ws if ws>s else s