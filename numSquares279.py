
### Lagrange's four-square theorem

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        a1 = math.floor(math.sqrt(n))+1
        sqrt_map = {}
        for i in range(int(a1)):
            sqrt_map[i*i] = []
        count  = 0
        ans = []
        if n in sqrt_map:
            return 1
        else:
            for i in sqrt_map:
                for j in sqrt_map:
                    res = n - j - i
                    if res in sqrt_map:
                        count = (i != 0) + (j != 0) + (res != 0)
                        if count == 2:
                            return 2    
        if count == 0:
            count = 4
        return count


a=Solution()
print(a.numSquares(13))