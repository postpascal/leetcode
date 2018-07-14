class Solution:
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		max_str = 1
		if not s :
			return 0
		for i in range(len(s)):
			if max_str > len(s) - i:
				return max_str
			for j in range(i+1, len(s)):
				if s[j] in s[i: j]:
					if j-i > max_str:
						max_str = j-i
					break
				elif j==len(s)-1:
					if j-i+1 > max_str:
						max_str = j-i+1
		return max_str