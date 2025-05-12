def max_profit(prices):
  profit = 0
  min_price = prices[0]
  for current_price_index in range(1, len(prices)):
    profit = max(profit, prices[current_price_index] - min_price)
    min_price = min(prices[current_price_index], min_price)
  return profit

print(max_profit([8, 9, 3, 7, 4, 16, 12]))
