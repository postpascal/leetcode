class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r=[[1]]
        if numRows==0:
            return []
        for i in range(1,numRows):
            rr=r[-1]+[1]
            for j in range(1,len(rr)-1):
                rr[j]=r[-1][j-1]+rr[j]
            r.append(rr)
        return r