class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        minDiff = float("inf")

        for i in range(len(nums) - k + 1):
            currentDiff = nums[i + k - 1] - nums[i]
            minDiff = min(minDiff, currentDiff)

        return minDiff
