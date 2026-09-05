class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        i, j = 0, len(heights) - 1

        while i<j:

            height = min(heights[i], heights[j])
            length = j - i
            res = max(res, height * length)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return res