def maxProductSubArray(nums):
    n = len(nums)
    result = nums[0]

    for i in range(n):
        mul = 1

        for j in range(i, n):
            mul *= nums[j]

            result = max(result, mul)

    return result

#Optimized - 1
def max_product(nums):
    n = len(nums)
    maxCurr = nums[0]
    minCurr = nums[0]
    maxProd = nums[0]

    for i in range(1,n):
        temp = max(nums[i], maxCurr * nums[i], minCurr * nums[i])
        minCurr = min(nums[i], maxCurr * nums[i], minCurr * nums[i])
        maxCurr = temp

        maxProd = max(maxProd, maxCurr)

    return maxProd

#Optimized - 2
def max_product2(nums):
    n = len(nums)
    maxProd = float('-inf')

    leftToRight = 1
    rightToLeft = 1

    for i in range(n):
        if leftToRight == 0:
            leftToRight = 1
        if rightToLeft == 0:
            rightToLeft = 1

        leftToRight *= nums[i]

        j = n-i-1
        rightToLeft *= nums[j]
        maxProd = max(maxProd, leftToRight, rightToLeft)

    return maxProd

if __name__ == "__main__":
    nums = [1, 2, -3, 0, -4, -5]
    print("The maximum product subarray:", max_product2(nums))