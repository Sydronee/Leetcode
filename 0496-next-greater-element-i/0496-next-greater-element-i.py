class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreatest = {}
        stack = []
        
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            nextGreatest[num] = stack[-1] if stack else -1
            stack.append(num)
        
        return [nextGreatest[num] for num in nums1]