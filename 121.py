class Solution:
    def maxProfit(self, stocks: List[int]) -> int:
        buy=0
        sell=0
        time=0
        profit=0
        n=len(stocks)
        while(time<n):
            if(stocks[time]>stocks[sell]):
                sell=time
            if(stocks[time]<stocks[buy]):
                buy=time
                sell=time
            if(stocks[sell]-stocks[buy]>profit):
                profit=stocks[sell]-stocks[buy]
            time=time+1
        return(profit)
