class Solution:
    def average(self, salary: List[int]) -> float:
        total=sum(salary)
        uhh=total-min(salary)-max(salary)
        return uhh/(len(salary)-2)