class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
            
        k = k % n
        rotated_nums = nums[-k:] + nums[:-k]
        nums[:] = rotated_nums