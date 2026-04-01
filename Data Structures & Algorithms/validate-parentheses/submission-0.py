class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
                continue
            
            if len(stack) == 0:
                return False

            top = stack[-1]
            if c == ")" and top != "(" or c == "}" and top != "{" or c == "]" and top != "[":
                return False
            stack.pop()
        return len(stack) == 0
            
        