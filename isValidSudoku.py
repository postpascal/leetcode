# class Solution:
# 	def isValidSudoku(self, board):
# 		for i in board:
# 			s=""
# 			for j in i:
# 				if j!=".":
# 					if j in s:
# 						return False
# 					else:
# 						s=s+j

# 		for i in range(9):
# 			s=""
# 			for j in range(9):
# 				if board[j][i]!=".":
# 					if board[j][i] in s:
# 						return False
# 					else:
# 						s=s+board[j][i]

# 		for r in range(0,9,3):
# 			for c in range(0,9,3):
# 				s=""
# 				for i in range(3):
# 					for j in range(3):
# 						if board[j+c][i+r]!=".":
# 							if board[j+c][i+r] in s:
# 								return False
# 							else:
# 								s=s+board[j+c][i+r]


# 		return True

class Solution(object):
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		rows  = [set() for _ in range(9)]
		cols  = [set() for _ in range(9)]
		dices = [[set() for _ in range(3)] for _ in range(3)]


		for i in range(9):
			for j in range(9):
				e = board[i][j]
				if e == '.': continue
				if e in rows[i] or e in cols[j] or e in dices[i//3][j//3]: return False
				rows[i].add(e)
				cols[j].add(e)
				dices[i//3][j//3].add(e)
		return True
		

a=Solution()

print(a.isValidSudoku([
	["5","3",".",".","7",".",".",".","."],
	["6",".",".","1","9","5",".",".","."],
	[".","9","8",".",".",".",".","6","."],
	["8",".",".",".","6",".",".",".","3"],
	["4",".",".","8",".","3",".",".","1"],
	["7",".",".",".","2",".",".",".","6"],
	[".","6",".",".",".",".","2","8","."],
	[".",".",".","4","1","9",".",".","5"],
	[".",".",".",".","8",".",".","7","9"]]))

