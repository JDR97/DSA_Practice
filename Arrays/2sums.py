def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if(nums[i] + nums[j] == target):
                return True
            
    return False


nums = [0, -1, 2, -3, 1]
target = -2

# Call the two_sum function and print the result
if two_sum(nums, target):
    print("true")
else:
    print("false")