class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minp=prices[0]
        maxprofit=-1
        for i in prices:
            if i<minp:
                minp=i
            if i-minp>maxprofit:
                maxprofit=i-minp
        return maxprofit if maxprofit>0 else 0