"""
121. Best Time to Buy and Sell Stock
------------------------------------

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
---------
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
----------
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    """
    [7,1,5,3,6,4]
        7 < 1 , No
        1 < 5 , yes profit = 4
        1 < 3 , yes profit = 2 , max = 4
        1 < 6 , yes profit = 5 , max = 5
        1 < 4 , yes profit = 3 , max = 5
    
    """
    Max = 0
    left, right = 0, 1  # start with index 0 and 1
    while right < len(prices):
        if prices[left] < prices[right]:  # when the current price was greater than prev then calculate max_profit
            max_profit = prices[right] - prices[left]
            Max = max(Max, max_profit)
        else:
            left = right  # if not
        right += 1  # always increment right value
    return Max


Prices = list(map(int, input().rstrip().split()))
print(maxProfit(Prices))
