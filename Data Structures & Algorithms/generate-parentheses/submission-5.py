class Solution:
    def generateParenthesis(self, n: int):
        """Generate parentheses with detailed tracing to understand the flow"""
        result = []
    
        def backtrack(current, open_count, close_count, depth=0):
            # Add indentation to visualize recursion depth
            indent = "  " * depth
            print(f"{indent}Called: current='{current}', open={open_count}, close={close_count}")
        
            # BASE CASE: We've built a complete string
            if len(current) == 2 * n:
                print(f"{indent}✓ Complete! Adding '{current}' to result")
                result.append(current)
                return
        
            # CHOICE 1: Add opening parenthesis
            if open_count < n:
                print(f"{indent}→ Trying to add '(' (open_count {open_count} < {n})")
                backtrack(current + "(", open_count + 1, close_count, depth + 1)
                print(f"{indent}← Back from adding '('")
            else:
                print(f"{indent}✗ Cannot add '(' (already used {open_count}/{n})")
        
            # CHOICE 2: Add closing parenthesis  
            if close_count < open_count:
                print(f"{indent}→ Trying to add ')' (close_count {close_count} < open_count {open_count})")
                backtrack(current + ")", open_count, close_count + 1, depth + 1)
                print(f"{indent}← Back from adding ')'")
            else:
                print(f"{indent}✗ Cannot add ')' (close_count {close_count} >= open_count {open_count})")
    
        print(f"=== Generating parentheses for n={n} ===")
        backtrack("", 0, 0)
        print(f"=== Final result: {result} ===")
        return result
        