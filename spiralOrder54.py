class Solution:
	def spiralOrder(self, matrix):
		if len(matrix)<1:
			return []
		if len(matrix)<2:
			return matrix[0]
		if len(matrix[0])<1:
			return []
		h=matrix[0]
		matrix=matrix[1:]
		t=matrix.pop()[::-1]
		tt=[]
		hh=[]
		for i in range(len(matrix)):
			tt.append(matrix[i][-1])
			matrix[i].pop()
			if len(matrix[i])>0:
				hh.append(matrix[i][0])
				matrix[i]=matrix[i][1:]
				
		h=h+tt+t+hh[::-1]+self.spiralOrder(matrix)
		return h


a=Solution()
print(a.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))