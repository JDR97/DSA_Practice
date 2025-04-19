## Can a person attend all meeting with the scheduled list. 
# Two approaches, 1. Running inner loop
## 2. Sorting and comparing end time with start time of next meeting
def overlap(meet1, meet2):
    return ((meet1[0] >= meet2[0] and meet1[0] < meet2[1]) or\
            (meet2[0] >= meet1[0] and meet2[0] < meet1[1])) 

def canAttend(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if overlap(arr[i], arr[j]):
                return False
    return True

def canAttend2(arr):
    n = len(arr)
    arr.sort(key= lambda x : x[0])
    
    for i in range(n-1):
        if(arr[i][1] > arr[i+1][0]):
            return False
        
    return True


if __name__ == "__main__":
    arr = [[2, 4], [1, 2], [7, 8], [5, 6], [6, 8]]
    print("true" if canAttend2(arr) else "false")