class Solution:
    def maxProfit(self, prices: List[int]) -> int: 

        minPrice = prices[0]  # Minimum Price 
        maxProfit = 0         # Maximum Profit 

        for price in prices:
            if price < minPrice:   # Current Price less then MinPrice 
                minPrice = price   # Store value of price in MinPrice 

            profit = price - minPrice   # Profit = currentPrice - MinPrice 

            if profit > maxProfit:   # TO maximize profit store it in MaxProfit 
                maxProfit = profit 

        return maxProfit 
