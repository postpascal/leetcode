# class Solution:
# 	def convert(self, s: str, numRows: int) -> str:
# 		def helper(ll,m):
# 			l=[]
# 			for i in range(len(ll)):
# 				l.append(ll[i])
# 				l.append(ll[i]+m)
# 			if l[-1]>=len(s):
# 				l.pop()
# 			return l


# 		ml=len(s)

# 		if ml<2 or numRows<2 or ml<numRows:
# 			return s
# 		t=2*numRows-2

# 		cs=[]
# 		for i in range(numRows):
# 			if i==0 or i==t/2:
# 				cs.extend(list(range(i,ml,t)))
# 			else:
# 				cs.extend(helper(list(range(i,ml,t)), t-2*i))
# 		r=[s[i] for i in cs]
# 		return ''.join(r)

class Solution:
	def convert(self, s, numRows):
		ml=len(s)
		if ml<2 or numRows<2 or ml<numRows:
 			return s
		ll=['' for i in range(numRows)]
		t=2*numRows-2
		for i in range(len(s)):
			ind=i%t
			if ind>numRows-1:
				ind = t-ind

			ll[ind]=ll[ind]+s[i]

		return ''.join(ll)

a=Solution()

print(a.convert("01234", 3))