class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        dp=[[-1]*(n) for i in range(m)]
        for i in range(m):
            for j in range(n):
                if(i==0 or j==0):
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return(dp[-1][-1])
