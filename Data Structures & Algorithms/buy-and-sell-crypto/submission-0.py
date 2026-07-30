class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        l, r = 0, len(prices)
        while l<r:
            while l<r:
                c = prices[r-1] - prices[l]
                if c>pro:
                    pro = c
                r-=1
            l+=1
            r = len(prices)
        return pro
