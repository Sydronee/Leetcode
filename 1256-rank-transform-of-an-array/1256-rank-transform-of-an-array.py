class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sList=sorted(set(arr))

        rank={num: rank+1 for rank, num in enumerate(sList)}

        sList=[rank[num] for num in arr]
        return sList