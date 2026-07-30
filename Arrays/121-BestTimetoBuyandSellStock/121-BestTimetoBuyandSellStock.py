# Last updated: 30/07/2026, 18:04:05
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        buy=prices[0]
4        profit=0
5        for price in prices:
6            if price<buy:
7                buy=price
8            if profit<(price-buy):
9                profit=price-buy
10        return profit 
11            