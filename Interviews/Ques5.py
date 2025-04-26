#Two Sum: Find the numbers that gives target after addition
def findTarget(arr, target):
    list_ele = []
    n = len(arr)
    for i in range(n):
        second_ele =  target - arr[i]
        if(second_ele in list_ele):
            return [second_ele, arr[i]]
        list_ele.append(arr[i])
        
    return -1



