class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowestPrice = prices[0]

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - lowestPrice)
            lowestPrice = min(lowestPrice, prices[i])

        return profit 