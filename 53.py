class Solution:
    def maxSubArray(self, array: List[int]) -> int:
        i=1
        s=array[0]
        result=array[0]
        n=len(array)
        while(i<n):
            p1=s+array[i]
            p2=array[i]
            s=max(p1,p2)
            result=max(result,s)
            i=i+1
        return(result)
