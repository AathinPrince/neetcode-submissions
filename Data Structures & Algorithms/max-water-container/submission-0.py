class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            m = 0
            for j in range(i+1,len(heights)):
                m = min(heights[i],heights[j]) * (j - i)
                if m>res:
                    res = m
        return res