def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    counter = {}

    for ch in str1:
        counter[ch] = counter.get(ch, 0) + 1

    for ch in str2:
        if ch not in counter or counter[ch] == 0:
            return False
        counter[ch] -= 1

    return True

#Another Approach
def isAnagram2(s1, s2):
    if len(s1) != len(s2):
        return False
    
    count = [0] * 26

    for c in s1:
        count[ord(c) - ord('a')] += 1

    for c in s2:
        if count[ord(c) - ord('a')] == 0:
            return False
        count[ord(c) - ord('a')] -= 1

    return True


str1 = "anagram"
str2 = "nagaram"

if(isAnagram2(str1, str2)):
    print("Yes, Anagram")
else:
    print("No, Not an Anagram")
