class Solution:
    def canCompleteCircuit(self, gas, cost):
        s=0
        n=0
        c=-1
        while c<len(gas):
            c=c+1
            i=n%len(gas)
            s=s+gas[i]-cost[i]

            if s<0:
                s=0
                c=-1
            n=n+1
            if n > 2*len(gas):
                return -1
            
        return i


a=Solution()
print(a.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))