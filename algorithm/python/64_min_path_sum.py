# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        pathsum = [[[] for j in range(col)] for i in range(row)]
        tmpsum = 0
        for i in range(col):
            tmpsum += grid[0][i]
            pathsum[0][i] = [tmpsum]
        tmpsum = 0
        for i in range(row):
            tmpsum += grid[i][0]
            pathsum[i][0] = [tmpsum]
        for i in range(1,row):
            for j in range(1,col):
                pathsum[i][j] = [[x + grid[i][j]] for x in pathsum[i-1][j]] + [[x + grid[i][j]] for x in pathsum[i][j-1]]
                pathsum[i][j] = min(pathsum[i][j])
        return min(pathsum[row-1][col-1])
