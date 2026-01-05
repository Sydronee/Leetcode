class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high=1, max(piles)
        result=0

        while low<=high:
            mid= low+(high-low)//2      

            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours<=h:
                result=mid
                high=mid-1

            else:
                low=mid+1

        return result