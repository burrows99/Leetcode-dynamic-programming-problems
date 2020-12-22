class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        n=len(a)
        m=len(b)
        dp=[['-1']*(n+1) for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if(i==0 or j==0):
                    dp[i][j]=''
                else:
                    if(a[j-1]==b[i-1]):
                        dp[i][j]=a[j-1]+dp[i-1][j-1]
                    else:
                        s1=dp[i-1][j]
                        s2=dp[i][j-1]
                        if(len(s1)>len(s2)):
                            dp[i][j]=s1
                        else:
                            dp[i][j]=s2
        return(len(dp[-1][-1]))
