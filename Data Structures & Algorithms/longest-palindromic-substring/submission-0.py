class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        
        startIdx = 0
        endIdx = len(s) - 1
        while startIdx < endIdx:
            if s[startIdx] == s[endIdx]:
                startIdx += 1
                endIdx -= 1
                continue
            
            return False
        return True

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        prev = 1
        curr_max = 1
        curr_ans = s[0]

        for i in range(1, len(s)):
            print("i", i)
            temp_max = 1
            temp_ans = s[i]
            for j in range(i - prev - 1, i):
                print(" j", j)
                if j < 0:
                    continue
                if self.isPalindrome(s[j:i+1]):
                    print(" len", len(s[j:i+1]))
                    print(" ans", s[j:i+1])
                    temp_max = len(s[j:i+1])
                    temp_ans = s[j:i+1]
                    break
                
            prev = temp_max
            print(i, temp_max, temp_ans)
            print()
            if curr_max < temp_max:
                curr_max = temp_max
                curr_ans = temp_ans 
        return curr_ans