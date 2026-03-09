class Solution:
    def hIndex(self, citations: List[int]) -> int:
        nums=sorted(citations, reverse=True)
        for i in range(len(nums)):
            if i>=nums[i]: 
                return i
        return len(nums)