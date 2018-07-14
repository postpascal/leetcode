class Solution:
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if strs==[] or strs[0]==[]:
			return ""
		for i in range(len(strs[0])):
			s=strs[0][i]

			for j in range(len(strs)):
				if len(strs[j])-1<i:
					return strs[0][:i]
				if strs[j][i] != s:
					return strs[0][:i]
		return strs[0]
		