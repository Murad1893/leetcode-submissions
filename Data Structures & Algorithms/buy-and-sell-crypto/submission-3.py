class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l, r = 0, 1
        
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                result = max(result, prices[r] - prices[l])
            
            r += 1

        return result