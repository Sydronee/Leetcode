class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        if not nums:
            return 0
            
        maxConsecutive=0
        curConsecutive=1

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]-1:
                curConsecutive+=1
            else:
                maxConsecutive=max(maxConsecutive, curConsecutive)
                curConsecutive=1
        
        return max(maxConsecutive, curConsecutive)