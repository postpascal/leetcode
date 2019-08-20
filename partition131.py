# import copy
# class Solution:
#     def __init__(self):
#         self.res = []

#     def is_palindrome(self, s):
#         if s and s == s[::-1]: return True
#         return False
    
#     def get_palindromes(self, s, list_s):
#         if not s: 
#             self.res.append(copy.deepcopy(list_s))
#             return list_s
#         for i in range(1,len(s)+1):
#             if self.is_palindrome(s[:i]):
#                 list_s.append(s[:i])
#                 self.get_palindromes(s[i:], list_s)
#                 del list_s[-1]
#         return self.res
    
#     def partition(self, s):
#         return self.get_palindromes(s,[])

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def dfs(nums, path, res):
            # print(path)
            if not nums:
                res += path,            
            for i in range(len(nums)):
                if nums[:i+1] == nums[:i+1][::-1]:
                    dfs(nums[i+1:], path + [nums[:i+1]], res)
        ans = []
        dfs(s, [], ans)
        return ans

a=Solution()
print(a.partition("aab"))





