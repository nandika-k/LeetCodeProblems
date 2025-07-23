class Solution:
    def maxProfit(self, prices) -> int:
        maxProfit = 0
        minSell = prices[0]

        for price in prices[1:]:
            maxProfit = max(maxProfit, price - minSell)
            minSell = min(minSell, price)
        return maxProfit
    
sol = Solution()
print(sol.maxProfit([1,4,6,8,2,1,2,6,9,2]))