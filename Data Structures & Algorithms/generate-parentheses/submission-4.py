class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def backtrack(left, right, curr):
            if left == right == n:
                results.append(curr)
                return
            
            if left < n:
                backtrack(left + 1, right, curr + "(")
            
            if right < left:
                backtrack(left, right + 1, curr + ")")
        
        backtrack(0, 0, "")
        return results