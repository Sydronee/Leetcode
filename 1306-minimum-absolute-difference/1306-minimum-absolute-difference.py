class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n=len(arr)
        arr.sort()
        result=[]

        minAbs=float('inf')
        for i in range(n-1):
            temp=arr[i+1]-arr[i]
            if temp<minAbs:
                minAbs=temp
        
        for i in range(n-1):
            if arr[i+1]-arr[i] == minAbs:
                result.append([arr[i],arr[i+1]])
        return result