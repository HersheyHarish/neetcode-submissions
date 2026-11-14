class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxp = 0
        while l < r:
            if r >= len(prices):
                return maxp
            profit = prices[r] - prices[l]
            if profit > maxp:
                maxp = profit
            elif prices[r] < prices[l]:
                l = r
                r = l+1
            else:
                r+=1

        