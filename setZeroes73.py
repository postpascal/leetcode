class Solution:
	def setZeroes(self, matrix):
		c=[]
		f=1
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j]==0:
					f=0
					if j not in c:
						c.append(j)
			if f==0:
				matrix[i]=[0] * len(matrix[0])
				f=1
		for i in range(len(matrix)):
			for ci in c:
				matrix[i][ci]=0
		return matrix


a=Solution()

print(a.setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]))
