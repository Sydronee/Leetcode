class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        test=Counter(nums)
        n=len(nums)/2

        for i in test.keys():
            if test[i]==n:
                return i