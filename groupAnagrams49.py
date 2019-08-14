from collections import defaultdict
class Solution:
	def groupAnagrams(self, strs):
		dic=defaultdict(list)

		for i in strs:
			bs=''.join(sorted(i))
			dic[bs].append(i)
		return dic.values()

### Frequency Solution
# class Solution:
# 	def groupAnagrams(strs):
# 		ans = collections.defaultdict(list)
# 		for s in strs:
# 			count = [0] * 26
# 			for c in s:
# 				count[ord(c) - ord('a')] += 1
# 			ans[tuple(count)].append(s)
# 		return ans.values()
		
a=Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))