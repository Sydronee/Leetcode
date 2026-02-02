class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_element = nums[0]
        remaining_elements = nums[1:]
        remaining_elements.sort()
        return first_element + remaining_elements[0] + remaining_elements[1]