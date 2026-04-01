class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cMap = {}
        for c in s:
            if c not in cMap:
                cMap[c] = 1
            else:
                cMap[c] += 1

        for c in t:
            if c not in cMap:
                return False
            else:
                cMap[c] -= 1

        for v in cMap.values():
            if v != 0:
                return False
        return True        