# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         def  recursiver(ss):
#             if ss in wordDict:
#                 return True
#             for i in range(1,len(ss)+1):

#                 if ss[:i] in wordDict:
#                     if recursiver(ss[i:]):
#                         return True
#         return bool(recursiver(s))

class Solution(object):
    def wordBreak(self, s, wordDict):
        if not wordDict:
            return False

        wordDict.sort(key=lambda x:len(x))
        max_len = len(wordDict[-1])
        min_len = len(wordDict[0])

        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(min_len, len(s)+1):
            left = max(0, i-max_len)
            right = i - min_len
            for j in range(left, right+1):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


a=Solution()
print(a.wordBreak("leetcode",["leet", "code"]))