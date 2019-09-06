class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r=0
        c=0
        if not matrix or not matrix[0]:
            return False

        if matrix[0][0]>target or matrix[-1][-1]<target:
            return False

        mc=len(matrix[0])
        mr=len(matrix)-1
        while r<mr+1 or c<mc:
            while matrix[r][-1]<target:
                r=r+1
                if r>mr:
                    return False
                if matrix[r][0]==target or matrix[r][-1]==target:
                    return True
                if matrix[r][0]>target:
                    return False


            while  matrix[r][c]<target:
                c=c+1
            while target<matrix[r][c]:
                c=c-1
            if matrix[r][c]==target:
                return True

            while matrix[r][c]<target and target<matrix[r][c+1]:
                r=r+1
                if r>mr:
                    return False
                if matrix[r][0]==target or matrix[r][-1]==target:
                    return True
                if matrix[r][0]>target:
                    return False


        return False
        

# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix or not matrix[0]:
#             return False
        
#         m, n = len(matrix), len(matrix[0])
        
#         x, y = 0, n-1
#         while 0<=x<m and 0<=y<n:
#             if matrix[x][y] > target:
#                 y -= 1
#             elif matrix[x][y] < target:
#                 x += 1
#             else:
#                 return True
        
#         return False

a=Solution()
print(a.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))