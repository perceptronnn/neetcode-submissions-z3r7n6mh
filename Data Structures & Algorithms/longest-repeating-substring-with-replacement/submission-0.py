class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        l, r = 0, 0
        result = 0
        while r < len(s):
            if s[r] not in charMap:
                charMap[s[r]] = 1
            else:
                charMap[s[r]] += 1

            while l <= r and r - l + 1 - self.mostFrequent(charMap) > k:
                charMap[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
            r += 1
        return result
    
    def mostFrequent(self, mp):
        mx = 0
        for k in mp:
            mx = max(mx, mp[k])
        return mx