class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = 0
        l = len(heights) - 1
        res = 0
        while (r < l):
            area = (l - r) * (min(heights[r], heights[l]))
            res = max(area, res)
            if (heights[r] < heights[l]):
                r += 1
            else:
                l -= 1
        return res

            
            