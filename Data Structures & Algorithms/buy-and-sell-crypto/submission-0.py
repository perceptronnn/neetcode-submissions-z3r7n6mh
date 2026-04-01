class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        l, r = 0, 0
        result = 0
        while r < len(prices):
            if l != r:
                print(prices[r], prices[l])
                result = max(result, prices[r] - prices[l])
            if r < len(prices) - 1 and prices[l] >= prices[r+1]: 
                l = r + 1
            r += 1
        return result
        