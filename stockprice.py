# stock_prices = [7, 2, 3, 5, 6] return 4
#									0  1  2  3  4
#							day 1  2  3  4  5

# [2,7,1,3] len(stock) = 4 - 1 = 3
# day = 2
# lowestStock = 1
#	highestPrice = 3 - 1
# return 2


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # always get the combination and see whats remains max
        # return max sum
        maxProfit = 0
        minimumPrice = float('inf')

        for i in range(len(prices)):
            if prices[i] < minimumPrice:
                minimumPrice = prices[i]

            elif prices[i] > minimumPrice and prices[i] - minimumPrice > maxProfit:
                maxProfit = prices[i] - minimumPrice

        return maxProfit
