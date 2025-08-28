class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        f=Counter(nums)
        return sorted(nums,key=lambda x: (f[x] ,-x))