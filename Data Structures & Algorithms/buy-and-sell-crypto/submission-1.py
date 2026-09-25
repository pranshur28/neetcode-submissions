class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        min_price = smallest price we have seen up to the current day
        prices[i] - min_price
        max_profit
        min_price

        prices = [10,1,5,6,7,1]
'''

        if len(prices) < 2:
            return 0

        min_price = prices[0]

        max_profit = 0

        i = 1
        while i < len(prices):
            price_today = prices[i]

            profit_if_sell_today = price_today - min_price

            if profit_if_sell_today > max_profit:
                max_profit = profit_if_sell_today
            if price_today < min_price:
                min_price = price_today

            i += 1

        return max_profit

        
