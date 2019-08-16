class Solution:
	def exist(self, board, word):
		r=len(board)
		c=len(board[0])

		def fulladjacent(closed,n,i,j):
			if n>=len(word):
				return True

			if i-1>-1:
				if word[n]==board[i-1][j] and [i-1,j] not in closed:
					if fulladjacent(closed+[[i-1,j]],n+1,i-1,j):
						return True
			if i+1<r:
				if word[n]==board[i+1][j] and [i+1,j] not in closed:
					if fulladjacent(closed+[[i+1,j]],n+1,i+1,j):
						return True
			if j-1>-1:
				if word[n]==board[i][j-1] and [i,j-1] not in closed:
					if fulladjacent(closed+[[i,j-1]],n+1,i,j-1):
						return True
			if j+1<c:
				if word[n]==board[i][j+1] and [i,j+1] not in closed:
					if fulladjacent(closed+[[i,j+1]],n+1,i,j+1):
						return True
			return False


		for i  in range(len(board)):
			for j in range(len(board[0])):
				n=0
				if board[i][j]==word[n]:
					closed=[[i,j]]
					if fulladjacent(closed,n+1,i,j):
						return True
		return False


a=Solution()
print(a.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))