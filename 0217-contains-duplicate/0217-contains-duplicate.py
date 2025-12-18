class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        nums=set(nums)

        return n>len(nums)