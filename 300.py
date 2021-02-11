import sys
class Solution:
    def lengthOfLIS(self, array: List[int]) -> int:
        def f(array,index,n,memo):
            if(memo[index]!=-1):
                return(memo[index])
            elif(index>n-1):
                memo[index]=1
                return(memo[index])
            else:
                possibilities=list()
                for i in range(index+1,n):
                    if(array[index]<array[i]):
                        possibilities.append(1+f(array,i,n,memo))
                if(possibilities!=[]):
                    memo[index]=max(possibilities)
                else:
                    memo[index]=1
                return(memo[index])
        array.insert(0,-sys.maxsize)
        n=len(array)
        index=0
        memo=[-1]*n
        return(f(array,index,n,memo)-1)
