class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for n in range(len(s)):
            countS[s[n]] = countS.get(s[n], 0) + 1
            countT[t[n]] = countT.get(t[n], 0) + 1

        return countS == countT