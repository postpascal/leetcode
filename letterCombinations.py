class Solution:
	def letterCombinations(self, digits: str):
		nd={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
		re=[]
		if len(digits)<1:
			return ""
		def mixd(h,ind):
			if ind>len(digits)-1:
				return h
			return mixd([i+j for i in h for j in nd[digits[ind]]],ind+1)
		return mixd(nd[digits[0]],1)



a=Solution()
print(a.letterCombinations('23'))

