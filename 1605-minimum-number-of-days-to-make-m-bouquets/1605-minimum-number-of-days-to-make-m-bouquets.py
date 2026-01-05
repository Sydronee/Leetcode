class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        totalNumFlowers=m*k
        res=-1
        low, high = min(bloomDay), max(bloomDay)

        while low<=high:
            mid=low+(high-low)//2
            
            bouquets = 0
            flowers = 0
            
            for day in bloomDay:
                if day<=mid:
                    flowers+=1
                    if flowers==k:
                        bouquets+=1
                        flowers=0 
                else:
                    flowers=0

            if bouquets>=m:
                res=mid
                high=mid-1
            else:
                low=mid+1

        return res