class Solution:
	def maxArea(self, height: List[int]) -> int:
		
		left = maxVal = 0
		dist = right = len(height)-1
		
		while left < right:
			curVal = dist * min(height[left],height[right])
			if maxVal < curVal:
				maxVal = curVal
			if height[left] < height[right]:
				left+=1
			else:
				right-=1
			dist-=1
			
		return maxVal

### 排除法：从最左和最右边界向中间靠，对于左右两个边界来说，
###短的那个已经达到了其参与的最大面积。因为随着向中间靠的过程中，
###其距离只会变小，即使另外一个高变得更高也不会增加其面积

a=Solution()
print(a.maxArea([8,10,14,0,13,10,9,9,11,11]))



 
