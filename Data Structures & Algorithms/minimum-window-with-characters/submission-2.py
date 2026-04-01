class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            print()
            print(r)
            print(c)
            if c in countT:
                print("c in countT")
                window[c] = window.get(c, 0) + 1
                if window[c] == countT[c]:
                    print(" window[c] == countT[c]")
                    have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    print("reslen" + str(resLen))
                    res = [l, r]
                if s[l] in countT:
                    window[s[l]] = window[s[l]] - 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
                print("l == " + str(l))
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""