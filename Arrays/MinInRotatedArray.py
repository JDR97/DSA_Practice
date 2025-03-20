import sys

def findMinEle(arr):
    n = len(arr)
    low = 0
    high = n-1

    minEle = sys.maxsize

    while(low <= high):
        mid = (low + high)//2
        
        if arr[low] < arr[mid]:
            minEle = min(minEle, arr[low])
            low = mid + 1
        else:
            minEle = min(arr[mid], minEle)
            high = mid -1

    return minEle



#Optimized 2
def findMinEle2(arr):
    n = len(arr)
    low = 0
    high = n-1

    minEle = sys.maxsize

    while low <= high:
        mid = (low + high)//2

        if(arr[low] <= arr[high]):
            minEle = min(minEle, arr[low])
            break

        if(arr[low] <= arr[mid]):
            minEle = min(arr[low], minEle)
            low = mid + 1
        else:
            minEle = min(minEle, arr[mid])
            high = mid - 1

    return minEle



arr = [4, 5, 6, 7, 0, 1, 2, 3]
ans = findMinEle2(arr)
print( ans )