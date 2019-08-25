class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        closed=[[False for _ in range(n)] for _ in range(m)]
        opened=[]
        n=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if closed[r][c]:
                    continue
                if grid[r][c]=="0":
                    closed[r][c]=True
                else:
                    opened.append([r,c])
                    n=n+1
                    while opened:
                        i,j=opened.pop()
                        closed[i][j]=True
                        if grid[i][j]=="1":
                            if i>0:
                                if not closed[i-1][j]:
                                    opened.append([i-1,j])
                            if j>0:
                                if not closed[i][j-1]:
                                    opened.append([i,j-1])
                            if i<len(grid)-1:
                                if not closed[i+1][j]:
                                    opened.append([i+1,j])
                            if j<len(grid[0])-1 :
                                if  not closed[i][j+1]:
                                    opened.append([i,j+1])
        return n

a=Solution()
print(a.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))