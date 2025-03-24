from typing import List

class Solution:
    def combinationSum(self, cand, tg):
        ans = []
        ds = []

        def findCombination(ind, tg):
            if ind == len(cand):
                if tg == 0:
                    ans.append(ds[:])
                return
            
            if cand[ind] <= tg:
                ds.append(cand[ind])
                findCombination(ind, tg - cand[ind])
                ds.pop()
            findCombination(ind + 1, tg)
            
        findCombination(0, tg)
        return ans

if __name__ == "__main__":
    obj = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    ans = obj.combinationSum(candidates, target)
    print("Combinations are: ")
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()