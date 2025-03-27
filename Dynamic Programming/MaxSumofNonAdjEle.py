def solveUtil(arr, idx, dp):
    if dp[idx] != -1:
        return dp[idx]
    
    if idx == 0:
        return arr[idx]
    
    if idx < 0:
        return 0
    
    pick =  arr[idx] + solveUtil(arr, idx-2, dp)
    not_pick = 0 + solveUtil(arr, idx-1, dp)

    dp[idx] = max(pick, not_pick)

    return dp[idx]

#Bottom Up solution
def solveUtil2(arr, idx, dp):
    dp[0] = arr[0]

    for i in range(1, n):
        pick = arr[i]

        if i > 1:
            pick += dp[i-2]
        not_pick = 0 + dp[i-1]

        dp[i] = max(pick, not_pick)

    return dp[n-1]

#Space Optimization
def solve2(arr, n):
    prev = arr[0]
    prev2 = 0

    for i in range(1, n):
        pick =  arr[i]

        if i>1:
            pick += prev2
        not_pick = 0 + prev

        cur_i = max(pick, not_pick)
        prev2 = prev
        prev = cur_i

    return prev
        

def solve(arr , n):
    dp = [-1 for i in range(n)]
    #return solveUtil(arr, n-1, dp)
    return solveUtil2(arr, n, dp)

arr = [2, 1, 4, 9]
n = len(arr)
res = solve2(arr, n)

print("Maximum Result:", res)