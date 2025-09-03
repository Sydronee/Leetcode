class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums=Counter(nums)
        nums=[nums.most_common()[0][0],nums.most_common()[1][0]]
        return nums