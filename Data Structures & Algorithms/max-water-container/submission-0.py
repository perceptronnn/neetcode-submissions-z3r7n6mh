class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = -1
        l = 0
        r = len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            print(l, r, heights[l], heights[r], area)
            result = max(result, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result
        