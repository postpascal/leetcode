class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = collections.defaultdict(list)
        
        for i in range(len(equations)):
            var1 = equations[i][0]
            var2 = equations[i][1]
            ans = values[i]
            
            g[var1] += [(var2, ans)]
            g[var2] += [(var1, 1/ans)]
        
        def search(s, end, path, v):
            for nei, val in g[s]:
                if nei == end:
                    return path * val
                elif nei not in v:
                    v[nei] = True
                    ans = search(nei, end, path*val, v)
                    if ans:
                        return ans
            return None
        
        rtn = []
        for q in queries:
            var_num = q[0]
            var_den = q[1]
            divisor = search(var_den, var_num, 1, {})
            if divisor:
                rtn += [1/divisor]
            else:
                rtn += [-1]
                
        return rtn