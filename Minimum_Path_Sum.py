class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1]*m for i in range(n)]

        #initialization
        dp[0][0]=grid[0][0]

        for i in range(1,n):
            dp[i][0]=grid[i][0]+dp[i-1][0]

        for i in range(1,m):
            dp[0][i]=grid[0][i]+dp[0][i-1]
        
        #dp
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=grid[i][j]+min(dp[i][j-1],dp[i-1][j])
        return(dp[-1][-1])
