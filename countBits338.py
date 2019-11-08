class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num<=1:
            return list(range(num+1))
        else:
            r=[0,1]
        i=0
        m=1
        while len(r)<=num:
            r.append(1+r[i])
            if i<2**m-1:
                i=i+1
            else:
                m=m+1
                i=0
        return r