def helper(s,c):
	if not s:
		print(c)
		return 
	for i in range(len(s)):
		helper(s[:i]+s[i+1:],c+s[i])

helper('abcd','')