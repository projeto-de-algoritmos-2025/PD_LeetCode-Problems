from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k >= n // 2:
            # Resolve como problema sem limite de transações
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
        
        # DP[i][j][0 ou 1] → dia i, j transações, 0=sem ação, 1=com ação
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        
        for j in range(k + 1):
            dp[0][j][1] = -prices[0]  # Comprar no dia 0

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])  # Vender
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])  # Comprar

        return max(dp[n-1][j][0] for j in range(k + 1))