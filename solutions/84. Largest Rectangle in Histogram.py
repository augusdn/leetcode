class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            """
            if current height is smaller than previous stack,
            cut the current cycle and calculate maxArea
            stack is sorted in increasing order
            all the previous blocks should be smaller
            """
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start,h))
​
        """
        remaining blocks in stack is in equal or increasing order
        calculae previous maxArea with current maxArea
        """
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights) - i))
        return maxArea
