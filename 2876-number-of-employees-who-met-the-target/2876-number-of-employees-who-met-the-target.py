class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        n=len(hours)
        count=0
        for i in hours:
            if i>=target:
                return n-count
            count+=1
        return 0