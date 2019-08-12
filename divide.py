class Solution:
	def divide(self, dividend: int, divisor: int):
		absDividend = abs(dividend)
		absDivisor = abs(divisor)
		
		ans = 0
		while absDividend >= absDivisor:
			temp = 0
			while absDividend >= absDivisor << temp:
				absDividend -= absDivisor << temp
				ans += 1 << temp
				temp += 1
				print(ans,temp)
		
		if not ((dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)):
			ans = 0 - ans
			
		maxInt = 2**31 -1
		return ans if ans <= maxInt else maxInt


a=Solution()
print(a.divide(15,3))









	