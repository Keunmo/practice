class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        strgrid = str(grid)
        rotten=[]
        if not '1' in strgrid:
            return count
        def updaterotten(grid):
            row = len(grid)
            col = len(grid[0])
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 2:
                        rotten.append((i,j))
        row = len(grid)
        col = len(grid[0])
        updaterotten(grid)
        while '1' in strgrid:
            bfstrgrid = str(grid)
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 2:
                        print(i,j)
                        if (i,j) in rotten:
                            if i-1 >= 0 and grid[i-1][j]==1:
                                grid[i-1][j] = 2
                            if i+1 <= row-1 and grid[i+1][j]==1:
                                grid[i+1][j] = 2
                            if j-1 >= 0 and grid[i][j-1]==1:
                                grid[i][j-1] = 2
                            if j+1 <= col-1 and grid[i][j+1]==1:
                                grid[i][j+1] = 2
                        print(grid)
            count += 1
            strgrid = str(grid)
            updaterotten(grid)
            if bfstrgrid == strgrid:
                return -1
        return count
                    
       
    

# 1 2 1 1 2 1 1
# 2 2 2 2 2 2 1
# 2 2 2 2 2 2 2
    
#           c   
#         2 2 2     00 01 02
#       r 0 2 2     10 11 12
#         1 0 2     20 21 22

# 2 1 1    2 2 1  2 2 2  2 2 2  
# 1 1 0    2 1 0  2 2 0  2 2 0
# 0 1 1    0 1 1  0 1 1  0 2 1