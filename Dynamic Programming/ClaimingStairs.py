def climbing(n, dp):
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

numStairs = 5
dp = [-1]*(numStairs+1)
print(climbing(numStairs, dp))