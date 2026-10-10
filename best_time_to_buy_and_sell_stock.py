# Given an array prices where prices[i] is the price of a given stock on day i, 
# find the maximum profit you can achieve. 
# You may only complete one transaction (i.e., buy one and sell one share of the stock).

"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
"""

# edge cases: will prices ever contain less than 2 elements

"""
window = [7]
"""

def max_profit(prices: list[int]) -> int:
  max_profit = 0
  min_price = float('inf')

  for price in prices:
    max_profit = max(max_profit, price - min_price)
    min_price = min(min_price, price)

  return max_profit


assert max_profit([7,1,5,3,6,4]) == 5
assert max_profit([7,6,4,3,1]) == 0
assert max_profit([1,2,3,4,5]) == 4
