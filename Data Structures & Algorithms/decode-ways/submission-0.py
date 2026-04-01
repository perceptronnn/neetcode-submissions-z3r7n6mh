class Solution:
    def numDecodings(self, s: str) -> int:
        a = 1
        b = 0 if int(s[0]) == 0 else 1
        for i in range(1, len(s)):
            t1 = b if int(s[i]) != 0 else 0
            t2 = a if 10 <= int(s[i-1:i+1]) and int(s[i-1:i+1]) <= 26 else 0
            a = b
            b = t1 + t2
        return b
        