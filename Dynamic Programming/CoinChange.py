def countRecur(coins, n, sum):
    if sum == 0:
        return 1
    if sum < 0 or n==0:
        return 0
    
    return countRecur(coins, n, sum - coins[n-1]) + countRecur(coins, n-1, sum)


def count(coins, sum):
    return countRecur(coins, len(coins), sum)

##Tabulation approach
def count1(coins, sum):
    n = len(coins)

    dp = [[0]*(sum+1) for i in range(n+1)]

    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(sum+1):
            ##Without using the current coin
            dp[i][j] += dp[i-1][j]

            if (j - coins[i-1]) >= 0:
                ##Using the current coin
                dp[i][j] += dp[i][j - coins[i-1]]

    return dp[n][sum]


##Space optimization
def count2(coins, sum):
    n = len(coins)

    dp = [0] * (sum+1)

    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], sum+1):
            dp[j] += dp[j - coins[i]]

    return dp[sum]



if __name__ == "__main__":
    coins = [1, 2, 3]
    sum = 5
    print(count2(coins, sum))