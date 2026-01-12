class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        n=len(heights)
        for i, h in enumerate(heights):
            while stack and stack[-1][1] > h:
                popI, popH = stack.pop()
                leftBoundary = stack[-1][0] if stack else -1
                width = i - leftBoundary - 1
                maxArea = max(maxArea, popH * width)
            stack.append((i, h))

        while stack:
            popI, popH = stack.pop()
            leftBoundary = stack[-1][0] if stack else -1
            width = n - leftBoundary - 1
            maxArea = max(maxArea, popH * width)
        return maxArea

