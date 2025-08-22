class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res=k
        for i in range(len(arr)):
            if arr[i]<=res:
                res+=1
            else:
                break
        return res