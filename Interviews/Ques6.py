###Finding Non duplicate value
def findMissingPacket(accessArr):
    n = len(accessArr)
    missingNum = 0
    for i in range(n-1):
        missingNum = accessArr[i] ^ accessArr[i+1]
    return missingNum