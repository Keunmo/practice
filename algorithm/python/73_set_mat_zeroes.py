# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # m = len(matrix)       #row
        # n = len(matrix[0])    #col
        rmem = set()
        cmem = set()
        for i in range(len(matrix)):      #i th row
            for j in range(len(matrix[0])):  #i th row's j th col
                if matrix[i][j] == 0:
                    rmem.add(i) # row i is 0
                    cmem.add(j) # col j is 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i in rmem) or (j in cmem):
                    matrix[i][j] = 0
                    
        
# rmem = {0}
# cmem = {0,3}

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33