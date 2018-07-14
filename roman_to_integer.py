class Solution:
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		roman_dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
		c=0
		for i in range(len(s)-1):
			if roman_dic[s[i]] < roman_dic[s[i+1]]:
				c= c -roman_dic[s[i]]
			else:
				c=c+roman_dic[s[i]]
		return c+roman_dic[s[-1]]
				
				
		