###Naive Approach
def isPalindrome(s, i, j):
    while i<j:
        if s[i]!=s[j]:
            return False
        i += 1
        j -= 1
    return True


def countPS(s):
    slen = len(s)
    res = 0

    for i in range(slen):
        for j in range(i+1, slen):
            if isPalindrome(s, i, j):
                res += 1

    return res

#### Dynamic Programming as Optimal substructure and Overlapping subproblems, with 2-D array
###Memorization Method(Top-Down)
def isPalindrome2(s, i, j, mem):
    if i == j:
        return 1
    
    if j == i+1 and s[i] == s[j]:
        return 1
    
    if mem[i][j] != -1:
        return mem[i][j]
    
    if s[i]==s[j] and isPalindrome2(s, i+1, j-1, mem):
        mem[i][j] = 1
    else:
        mem[i][j] = 0

    return mem[i][j]

def countPS2(s):
    n = len(s)
    mem = [[-1 for i in range(n)] for i in range(n)]

    res = 0 
    for i in range(n):
        for j in range(i+1, n):
            if isPalindrome2(s, i, j, mem):
                res += 1

    return res

#Tabulation (Bottom-Up)
def countPS(s):
    n = len(s)
    res = 0

    dp = [[False] * n for i in range(n)]

    ##For length=1 string
    for i in range(n):
        dp[i][i] = True

    ##For length=2 string
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            res += 1

    ##When length is more than 2
    for i in range(2, n):
        for j in range(n-i):
            k = j + i

            if s[k] == s[j] and dp[j+1][k-1]:
                dp[j][k] = True
                res += 1

    return res

##Center expansion
def countPalindromes(s):

    n = len(s)
    count = 0

    # Count odd length palindrome substrings 
    # with str[i] as center.
    for i in range(len(s)):
        left = i - 1
        right = i + 1
        while left >= 0 and right < n:
            if s[left] == s[right]:
                count += 1
            else:
                break
            left -= 1
            right += 1

    # Count even length palindrome substrings
    # where str[i] is first center.
    for i in range(len(s)):
        left = i
        right = i + 1
        while left >= 0 and right < n:
            if s[left] == s[right]:
                count += 1
            else:
                break
            left -= 1
            right += 1

    return count



if __name__ == "__main__":
    s = "abaab"
    print(countPS2(s))
    st = "abbaeae"
    print(countPalindromes(st))