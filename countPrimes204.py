#https://www.zhihu.com/question/29580448/answer/45218281
class Solution:
    def countPrimes(self, n: int) -> int:
        n -= 1
        if n < 2:
            return 0
        r = int(n ** 0.5)
        V = [n//d for d in range(1, r + 1)]
        V += list(range(V[-1] - 1, 0, -1))
            
        S = {v: v - 1 for v in V}
        for p in range(2, r + 1):
            if S[p] == S[p - 1]:
                continue
            p2 = p * p
            sp_1 = S[p - 1]
            for v in V:
                if v < p2:
                    break
                S[v] -= S[v//p] - sp_1
        return S[n]