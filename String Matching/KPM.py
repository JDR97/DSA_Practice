#LPS(Longest Prefix Suffix)
#Create LPS array of pattern and compare that LPS with given string

def createLPS(pat, lps):
    len1 = 0
    m = len(pat)

    lps[0] = 0
    i = 1

    while i<m:
        if pat[i] == pat[len1]:
            len1 += 1
            lps[i] = len1
            i += 1
        else:
            if len1 != 0:
                len1 = lps[len1-1]
            else:
                lps[i] = 0
                i += 1
            

def search(pat, txt):
    n = len(txt)
    m = len(pat)

    lps = [0]*m
    res = []

    createLPS(pat, lps)

    i=0
    j=0

    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1
            
            if j == m:
                res.append(i-j)
                j = lps[j - 1]

        else:
            if j!=0:
                j = lps[j-1]
            else:
                i += 1
    return res



if __name__ == "__main__":
    txt = "aabaacaadaabaaba"
    pat = "aaba"
    res = search(pat, txt)
    for i in range(len(res)):
        print(res[i], end=" ")