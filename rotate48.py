class Solution:
	def rotate(self, matrix):
		lp=[0,0]
		rp=[0,len(matrix)-1]
		ld=[len(matrix)-1,0]
		rd=[len(matrix)-1,len(matrix)-1]
		m=len(matrix)-1
		while m>0:
			for i in range(m):
				matrix[rp[0]+i][rp[1]],matrix[rd[0]][rd[1]-i],matrix[ld[0]-i][ld[1]],matrix[lp[0]][lp[1]+i]=matrix[lp[0]][lp[1]+i],matrix[rp[0]+i][rp[1]],matrix[rd[0]][rd[1]-i],matrix[ld[0]-i][ld[1]]
				
			m-=2
			lp[0]+=1
			lp[1]+=1
			rp[0]+=1
			rp[1]-=1
			ld[0]-=1
			ld[1]+=1
			rd[0]-=1
			rd[1]-=1
		return matrix











a=Solution()
print(a.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]))