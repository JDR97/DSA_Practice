import sys

def maxSubarraySum2(arr):
    
    res = arr[0]
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        
        # Find the maximum sum ending at index i by either extending 
        # the maximum sum subarray ending at index i - 1 or by
        # starting a new subarray from index i
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update res if maximum subarray sum ending at index i > res
        res = max(res, maxEnding)
    
    return res

arr = [2, 3, -8, 7, -1, 2, 3]
print(maxSubarraySum2(arr))

###Same but different code
def maxSubarraySum(arr, n):
    maxi = -sys.maxsize-1
    sum = 0

    for i in range(n):
        sum += arr[i]

        if sum > maxi:
            maxi = sum

        if sum < 0:
            sum = 0
    
    return maxi


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)