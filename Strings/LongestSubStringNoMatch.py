##Find the longest substring without repeated characters
##We have three approaches here. 

#1. Naive, maintaining an array of size 26 to check if the character is visited or not
def longestUniqueSubstr(s):
    n = len(s)
    res = 0

    for i in range(n):
        vis = [False] * 26

        for j in range(i,n):
            if vis[ord(s[j]) - ord('a')] == True:
                break
            else:
                res = max(res, j-i+1)
                vis[ord(s[j]) - ord('a')] = True

    return res

### 2. Using Two Pointer
def longestUniqueSubstr2(s):
    if len(s)==0 or len(s)==1:
        return len(s)
    
    res = 0
    n = len(s)

    vis = [False] * 26
    left = 0
    right = 0

    while right < n:
        while vis[ord(s[right])-ord('a')] == True:
            vis[ord(s[left])-ord('a')] = False
            left += 1

        vis[ord(s[right])-ord('a')] = True

        res = max(res, right-left+1)
        right += 1

    return res

##3. Keeping the track of last index of every character
def longestUniqueSubstr3(s):
    n = len(s)
    res = 0

    lastIdx = [-1] * 26
    start = 0

    for end in range(n):
        start = max(start, lastIdx[ord(s[end]) - ord('a')] + 1)
        res = max(res, end - start + 1)
        lastIdx[ord(s[end]) - ord('a')] = end

    return res



if __name__ == "__main__":
    s = "geeksforgeeks"
    print(longestUniqueSubstr3(s))
