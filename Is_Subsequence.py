class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def F(a,b):
            n=len(a)
            m=len(b)
            dp=[[-1]*(m+1) for i in range(n+1)]
            for i in range(n+1):
                for j in range(m+1):
                    if(i==0 or j==0):
                        dp[i][j]=''
                    else:
                        if(a[i-1]==b[j-1]):
                            dp[i][j]=a[i-1]+dp[i-1][j-1]
                        else:
                            p1=dp[i-1][j]
                            p2=dp[i][j-1]
                            if(len(p1)>len(p2)):
                                dp[i][j]=p1
                            else:
                                dp[i][j]=p2
            return(dp[-1][-1][::-1])
        ss=F(s,t)
        if(ss==s):
            return(True)
        else:
            return(False)
