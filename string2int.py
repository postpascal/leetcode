class Solution:
	def myAtoi(self, s: str) -> int:
		si=''
		d=['1','0','2','3','4','5','6','7','8','9','-',' ','+']

		for i in s:
			if i not in d:
				break
			elif i in ['-', ' ','+']:
				si=si+i
				continue
			else:
				si=si+i
				d=['1','0','2','3','4','5','6','7','8','9']

		si=si.strip(" ")
		if si=='-' or si==" " or si=="+":
			return 0
		if len(si)<1:
			return 0
		if len(si)>1 and si[1] not in ['1','0','2','3','4','5','6','7','8','9']:
			return 0
		if int(si)<-2147483648:
			return -2147483648

		if int(si)>2147483648:
			return 2147483648
		return int(si)


a=Solution()

print(a.myAtoi("+1"))
