class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        cleanedS = ''.join(c.lower() for c in s if c.isalnum())

        left = 0
        right = len(cleanedS) - 1
        while left < right:
            if cleanedS[left] != cleanedS[right]:
                return False
            left += 1
            right -= 1
        
        return True
        