# class Solution:
# 	def longestPalindrome(self, s: str) -> str:
# 		max_str = -1
# 		st=0
# 		e=0
# 		if len(s)<2 or s==s[::-1]:
# 			return s

# 		for i in range(len(s)):
# 			for j in range(i+1, len(s)+1):
# 				if s[i: j]==s[i: j][::-1]:
# 					if j-i > max_str:
# 						max_str = j-i
# 						st=i
# 						e=j


# 		return s[st:e]

### Time Complexity O(n^2)

class Solution(object):
	def longestPalindrome(self, s):

		def hepler(s,sl,sr):
			while sl>=0 and sr<len(s):
				if s[sl]!=s[sr]: break
				sl-=1
				sr+=1
			return [sl+1, sr]

		maxl=[0,1]
		for i in range(1,len(s)):
			odd = hepler(s, i-1, i+1)
			even = hepler(s, i-1, i)
			maxl = max(maxl,odd, even, key=lambda x: x[1]-x[0])

		return s[maxl[0]:maxl[1]]
		
		
a=Solution()
print(a.longestPalindrome('cfhbbb'))

