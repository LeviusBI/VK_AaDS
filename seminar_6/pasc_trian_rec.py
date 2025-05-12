n = 6
def pascal_rec(row, col):
  if (col == 0) or (row == col):
    return 1
  else:
    return pascal_rec(row - 1, col - 1) + pascal_rec(row - 1, col)

dp = []
for row in range(n):
  curr_row = []
  for col in range(row + 1):
    curr_row.append(pascal_rec(row, col))
  dp.append(curr_row)
dp
