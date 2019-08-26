class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        from collections import  defaultdict
        incoming = defaultdict(int)
        outgoing = defaultdict(set)
        for i, j in prerequisites:
            incoming[i] +=1
            outgoing[j].add(i)
        stack = [node for node in range(numCourses) if not incoming[node]]
        a=stack[:]

        while stack:
            node = stack.pop(0)
            for neigh in outgoing[node]:
                incoming[neigh] -=1
                if not incoming[neigh]:
                    stack.append(neigh)
                    a.append(neigh)
            incoming.pop(node)
        if not incoming:
        	return a
        else:
        	return []
        return not incoming


a=Solution()
print(a.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))