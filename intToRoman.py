class Solution:
	def intToRoman(self, num: int) -> str:
		dg={0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
		ds={0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
		db={0:'',1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}

		# d={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
		q=num//1000
		b=(num%1000)//100
		s=(num%100)//10
		g=(num%10)
		s=q*'M'+db[b]+ds[s]+dg[g]
		return s



a=Solution()
print(a.intToRoman(1994))