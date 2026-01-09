class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=sorted(nums,key=int)
        return nums[-k]