# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         def recursiver(x):
#             if x<=1:
#                 return 1
#             else:
#                 return recursiver(x-1)+recursiver(x-2)
#         return recursiver(n)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def recursiver(x):
            if x<=1:
                return 1
            else:
                return recursiver(x-1)+recursiver(x-2)
        return recursiver(n)

        
a=Solution()
print(a.climbStairs(7))