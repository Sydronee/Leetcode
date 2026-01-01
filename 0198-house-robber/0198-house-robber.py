class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def checkToRob(index):
            if index>=len(nums):
                return 0
            withoutSkip=nums[index]+checkToRob(index+2)
            skipped=checkToRob(index+1)

            return max(withoutSkip, skipped)
        
        return checkToRob(0)