class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cap = 0
        left, right = 0, len(heights) - 1

        while left < right:
            curr_cap = min(heights[left], heights[right]) * (right - left)
            max_cap = max(curr_cap, max_cap)
            if heights[left] <= heights[right]:
                left += 1
            else:
               right -= 1
        return max_cap