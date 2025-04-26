##Get the maximum profit
def calProfit(stck):
    n = len(stck)
    buy = stck[0]
    maxProfit = 0
    for i in range(1, n):
        maxProfit = max(maxProfit, stck[i] - buy)
        buy = min(buy, stck[i])

    return maxProfit

stock = [5, 11]
res = calProfit(stock)
print(res)