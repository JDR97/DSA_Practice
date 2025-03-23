#Memorization Approach (Top Down)
def fibonacci(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibonacci(n-1, dp) + fibonacci(n-2, dp)
    return dp[n]

    
#Tabulation Approach (Bottom Up)
def fibonacci2(n, dp):
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

n = 7
dp = [-1] * (n+1)
print(fibonacci2(n, dp))