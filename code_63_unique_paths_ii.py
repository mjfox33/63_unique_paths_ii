class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) # assuming every row has the same number of columns
        result = [ [0]*n for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    result[i][j] = 1
                if i == 0 and j > 0:
                    result[i][j] = 1 if obstacleGrid[i][j-1] == 0 and result[i][j-1] == 1 else 0
                if i > 0 and j == 0:
                    result[i][j] = 1 if obstacleGrid[i-1][j] == 0 and result[i-1][j] == 1 else 0
                if i>0 and j>0:
                    result[i][j] = result[i][j-1] + result[i-1][j]
                if obstacleGrid[i][j] == 1:
                    result[i][j] = 0
                
        return int(result[-1][-1])