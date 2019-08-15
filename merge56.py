class Solution:
	def merge(self, intervals):
		if len(intervals)<1:
			return []
		intervals=sorted(intervals,key=lambda x: x[0])
		re=[intervals[0]]
		for i in range(1,len(intervals)):
			if intervals[i][0]>re[-1][1]:
				re.append(intervals[i])
			else:
				re[-1]=[re[-1][0],max(re[-1][1],intervals[i][1])]

		return re



a=Solution()
print(a.merge([[1,3],[2,6],[8,10],[15,18]]))