class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longestStreak=0

        for num in nums:
            if (num-1) not in nums:
                currentStreak=1
                currentNumber=num
                while (currentNumber+1) in nums:
                    currentNumber+=1
                    currentStreak+=1

                longestStreak=max(longestStreak, currentStreak)

        return longestStreak