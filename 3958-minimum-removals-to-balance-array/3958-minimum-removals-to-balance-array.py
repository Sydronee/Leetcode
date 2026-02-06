class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        max_kept = 0
        
        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1
            current_window_size = right - left + 1
            max_kept = max(max_kept, current_window_size)
        return n - max_kept