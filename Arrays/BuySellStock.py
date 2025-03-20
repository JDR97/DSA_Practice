def buySellStock( arr ):
    n = len(arr)
    minBuy = arr[0]
    maxProfit = 0

    for i in range(1,n):
        profit = arr[i] - minBuy
        if profit > maxProfit:
            maxProfit = profit
        minBuy = min(minBuy, arr[i])

    return maxProfit  


arr = [7,1,5,3,6,4]
value = buySellStock(arr)
print(value)