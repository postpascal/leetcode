class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        def recursiver(prerequisites):
            if not prerequisites:
                return True

            a=[]
            print(unpre,prerequisites)
            for i in range(len(prerequisites)):
                # print(unpre[prerequisites[i][1]])

                if sum(unpre[prerequisites[i][1]])==len(unpre[prerequisites[i][1]]):
                    for j in range(len(unpre[prerequisites[i][0]])):
                        if unpre[prerequisites[i][0]][j]==False:
                            unpre[prerequisites[i][0]][j]=True
                            break
                else:
                    a.append(prerequisites[i])

            # print(a)

            if len(a)==len(prerequisites):
                return False

            return recursiver(a)


        unpre=[[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
                unpre[prerequisites[i][0]].append(False)

        for i in range(len(unpre)):
            if len(unpre[i])<1:
                unpre[i]=[True]
        q=recursiver(prerequisites)
        return q
        
# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):
#         from collections import  defaultdict
#         incoming = defaultdict(int)
#         outgoing = defaultdict(set)
#         for i, j in prerequisites:
#             incoming[i] +=1
#             outgoing[j].add(i)
#         stack = [node for node in range(numCourses) if not incoming[node]]
#         while stack:
#             node = stack.pop(0)
#             for neigh in outgoing[node]:
#                 incoming[neigh] -=1
#                 if not incoming[neigh]:
#                     stack.append(neigh)
#             incoming.pop(node)
#         return not incoming


a=Solution()
print(a.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))