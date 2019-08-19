class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        l=len(board)
        if l <3:
            return board
        c=len(board[0])
        if c<3:
            return board
        closed=[]

        openl=[[0,i] for i in range(c)] +[[l-1,i] for i in range(c)]
        v=[[i,0] for i in range(1,l-1)] +[[i,c-1] for i in range(1,l-1)]
        openl.extend(v)

        while openl:
            i,j=openl.pop()

            if board[i][j]=="O":
                board[i][j]="Z"
                closed.append([i,j])

                if i>0 and [i-1,j] not in openl and [i-1,j] not in closed:
                    openl.append([i-1,j])

                if i+1<l and [i+1,j] not in openl and [i+1,j] not in closed:
                    openl.append([i+1,j])

                if j>0 and [i,j-1] not in openl and [i,j-1] not in closed:
                    openl.append([i,j-1])

                if j+1<c and [i,j+1] not in openl and [i,j+1] not in closed:
                    openl.append([i,j+1])

        for i in range(l):
            for j in range(c):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="Z":
                    board[i][j]="O"

        return board




a=Solution()
print(a.solve([["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]))