class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] in d.keys():
                return [i, d[nums[i]]]
            else:
                d[target-nums[i]]=i