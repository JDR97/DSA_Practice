#Rabin Karp algorithm matches the hash value of the pattern with the hash value 
# of the current substring of text, and if the hash values match then only it 
# starts matching individual characters.

#For each character ‘c’ at position ‘i’, calculate its contribution to the hash 
# value as ‘c * (bpattern_length – i – 1) % p’ and add it to ‘hash, where b and p are
#prime number as base and modulus, b is mostly 256

#hash = (hash – (text[i – pattern_length] * (bpattern_length – 1)) % p) * b + text[i], Update the hash

d = 256

def search(pat, txt, q):
    m = len(pat)
    n = len(txt)
    i = 0
    j = 0
    h = 1
    p = 0
    t = 0

    for i in range(m-1):
        h = (h*d) % q
    
    for i in range(m):
        p = (p*d + ord(pat[i])) % q
        t = (t*d + ord(txt[i])) % q

    for i in range(n-m+1):
        if p ==  t:
            for j in range(m):
                if pat[j] != txt[i+j]:
                    break
                else:
                    j += 1

            if j == m:
                print("Found: " + str(i))

        if i < n-m:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+m])) % q
            if t < 0:
                t = t + q

if __name__ == '__main__':
    txt = "GEEKS FOR GEEKS"
    pat = "FOR"

    # A prime number
    q = 101

    # Function Call
    search(pat, txt, q)