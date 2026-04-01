class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        smallerRight = [-1] * len(heights)
        smallerLeft = [-1] * len(heights)

        stack = []
        for idx in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] > heights[idx]:
                smallerRight[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)
            print("stack R", str(stack))


        #print(stack)
        while len(stack) > 0 :
            smallerRight[stack[-1]] = len(heights) - stack[-1]
            stack.pop()
        
        for idx in range(len(heights) - 1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] > heights[idx]:
                smallerLeft[stack[-1]] = stack[-1] - idx
                stack.pop()
            stack.append(idx)
            print("stack L", str(stack))
        
        print(stack)
        while len(stack) > 0:
            smallerLeft[stack[-1]] = stack[-1] + 1
            stack.pop()

        result = 0
        for idx in range(len(heights)):
            result = max((smallerRight[idx] + smallerLeft[idx] - 1) * heights[idx], result)

        return result 
        