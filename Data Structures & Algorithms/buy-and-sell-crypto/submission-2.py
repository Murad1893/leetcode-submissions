class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                result = max(result, prices[j] - prices[i])
        
        return result