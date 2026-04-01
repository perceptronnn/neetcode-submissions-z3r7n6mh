class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cMap = {}
        for c in s:
            cMap[c] = 1 + cMap.get(c, 0)

        for c in t:
            cMap[c] = cMap.get(c, 0) - 1

        for v in cMap.values():
            if v != 0:
                return False
        return True        