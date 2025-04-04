def longestPrefix(str):
    len1 = 0
    i = 1
    n = len(str)
    lps = [0]*n

    while(i<n):
        if(str[i] == str[len1]):
            len1 += 1
            lps[i] = len1
            i += 1
        else:
            if len1 != 0:
                len1 = lps[len1-1]
            else:
                lps[i] = 0
                i += 1

    ans = str[0:len1]
    return ans


str  = "ababab"
ans = longestPrefix(str)
print("Answer: " + ans)