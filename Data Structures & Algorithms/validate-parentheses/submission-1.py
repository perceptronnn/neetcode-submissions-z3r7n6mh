class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["} # Store mapping of closing to opening brackets

        for char in s:
            if char in mapping.values(): # If it's an opening bracket
                stack.append(char)
            elif char in mapping.keys(): # If it's a closing bracket
                if not stack or mapping[char] != stack.pop(): # Check if stack is empty OR if top doesn't match
                    return False
            # else: # If you had other characters, you'd handle them here (ignore, error, etc.)

        return not stack # True if stack is empty, False otherwise