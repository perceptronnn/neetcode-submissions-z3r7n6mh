class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        minCoins = [-1] * (amount + 1)
        minCoins[0] = 0
        for i in range(1, amount + 1):
            minCoin = float('inf')
            for c in coins:
                if c > i:
                    break
                if i - c >= 0 and minCoins[i - c] != -1 and minCoins[i - c] < minCoin:
                    minCoin = minCoins[i - c]
            if minCoin != float('inf'):
                minCoins[i] = minCoin + 1
        return minCoins[amount]