class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lastr=None
        maxprofit=0
        singleprofit=0
        r=1
        while r<len(prices):
            while r<len(prices) and prices[r]<=prices[r-1]:
                r=r+1
            if r>=len(prices):
                return maxprofit+singleprofit
            singleprofit=prices[r]-prices[r-1]
            l=r-1
            r=r+1
            while r<len(prices) and prices[r]>=prices[r-1] :
                singleprofit=prices[r]-prices[l]
                r=r+1
            if r>=len(prices):
                return maxprofit+singleprofit
                
            maxprofit=maxprofit+singleprofit
            singleprofit=0
            if  lastr and prices[l]>prices[lastr]:
                maxprofit=maxprofit-prices[lastr]+prices[l]
            lastr=r-1
                
        return maxprofit