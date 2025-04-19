###Find the max length of substring of same characters, replace any character to another
#character. Allowed to do K operations

##Naive Approach
def getMaxFreq(s, l, r):
    mdir = {}
    n = r-l+1
    for i in range(l, r+1):
        mdir[s[i]] = mdir.get(s[i], 0) + 1

    res = max(mdir.values())
    return res

def longestSubstr(s, k):
    n = len(s)
    res = 1

    for l in range(n):
        for r in range(l,n):
            f = getMaxFreq(s, l, r)
            ##Length of the substring minus the max freq = number of characters need to be changed
            if (r - l + 1 - f) <= k:
                res = max(res, r-l+1)

    return res

#Window Sliding
def longestSubstr2(s,k):
    res = 0
    n = len(s)

    for c in range(ord('A'), ord('Z')+1):
        l, r, count = 0, 0, 0

        while r < n:
            ##Incase of the matches are continuing
            if s[r] == chr(c):
                r += 1
            #Incase of match broke but still operations are left
            elif count < k:
                count += 1
                r += 1
            #Unmatching character occurred and no operation left, so we modify the substring by increasing left
            #here we need to calculate res for different substring
            elif s[l] == chr(c):
                l += 1
            #New substring, now count needs to decrease as starting char does no match this new char. (Example: ABABBAC)
            else:
                l += 1
                count -= 1

            res = max(res, r-l)

    return res

##Slide the window with Hashmap
def longestSubstr3(s, k):
    n = len(s)
    freq = {}
    res = 0 
    maxFreq = 0

    left=0
    right=0

    while(right<n):
        freq[s[right]] = freq.get(s[right], 0) + 1
        #To hold the count of most frequent character in the current window
        maxFreq = max(maxFreq, freq[s[right]])
        #Enters only when k operations are exhuasted
        if (right - left + 1 - maxFreq) > k:
            freq[s[left]] -= 1
            left += 1

        res = max(res, right-left+1)
        right += 1

    return res



if __name__ == "__main__":
    k = 1
    s = "ABABBAC"
    print("Maximum length =", longestSubstr3(s, k))