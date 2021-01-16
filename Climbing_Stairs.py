class Solution:
    def climbStairs(self, s: int) -> int:
        dp=[0,1,2]
        i=3
        while(i-2>=0 and i<s+1):
            dp.append(dp[i-1]+dp[i-2])
            i=i+1
        return(dp[s])
