class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sA=sum(aliceSizes)
        sB=sum(bobSizes)

        diff=(sA-sB)/2
        A=set(aliceSizes)
        for b in set(bobSizes):
            if diff+b in A:
                return [diff+b,b]