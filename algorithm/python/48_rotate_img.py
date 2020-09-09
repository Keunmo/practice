# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        start = -1
        end = n+1
        for i in range(0,(n+1)//2):
            # print('s,e',start,end)
            start += 1
            end -= 1
            for j in range(start,end):
                # print('s,e',start,end)
                # print('i,j',i,j)
                # print(i,j,matrix[i][j])
                # print(j,n-i,matrix[j][n-i])
                # print(n-i,n-j,matrix[n-i][n-j])
                # print(n-j,i,matrix[n-j][i])
                matrix[i][j], matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i] = matrix[n-j][i], matrix[i][j], matrix[j][n-i], matrix[n-i][n-j]
                # print(matrix)
                