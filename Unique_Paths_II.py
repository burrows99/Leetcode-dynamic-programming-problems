class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if(grid[-1][-1]==1 or grid[0][0]==1):
            return(0)
        n=len(grid)
        m=len(grid[0])
        dp=[[-1]*m for i in range(n)]

        #initialization
        flag=0
        for i in range(n):
            if(grid[i][0]==1):
                flag=1
            if(flag==1):
                dp[i][0]=0
            elif(flag==0):
                dp[i][0]=1
        flag=0
        for j in range(m):
            if(grid[0][j]==1):
                flag=1
            if(flag==1):
                dp[0][j]=0
            elif(flag==0):
                dp[0][j]=1

        #dp
        for i in range(1,n):
            for j in range(1,m):
                if(grid[i-1][j]!=1 and grid[i][j-1]!=1):
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                elif(grid[i-1][j]==1 and grid[i][j-1]!=1):
                    dp[i][j]=dp[i][j-1]
                elif(grid[i-1][j]!=1 and grid[i][j-1]==1):
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=0
        return(dp[-1][-1])
