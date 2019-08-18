# class Solution:
# 	def numDecodings(self, s: str) -> int:
# 		def recurser(ind):
# 			if s[ind]=="0":
# 				return 0
# 			if ind>=len(s)-1:
# 				return 1

# 			if int(s[ind:ind+2])<= 26:

# 				if ind+2>len(s)-1:
# 					s1=1
# 				else:
# 					s1=recurser(ind+2)
# 			else:
# 				s1=0
# 			s2=recurser(ind+1)
# 			return s1+s2

# 		r=recurser(0)
# 		return r



class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		sol = [0,int(not s[0]=='0')]
		if len(s)<2:
			return sol[len(s)]
		sol = [1,1]
		if '00' in s or s[0]=='0':
			return 0
		for i in range(1,len(s)):
			if s[i]=='0':
				if int(s[i-1])>2 :
					return 0
				sol[1] = sol[0]
				continue
			if 0<int(s[i-1])<2 or (int(s[i-1])==2 and int(s[i])<7):
				sol[0] = sol[0]+sol[1]
				sol[0],sol[1] = sol[1],sol[0]
			else:
				sol[0] = sol[1]
		return sol[1]


		
a=Solution()
print(a.numDecodings("12"))