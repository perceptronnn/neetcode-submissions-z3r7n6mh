class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Find the number of days until a warmer temperature for each day.
        
        Uses a monotonic decreasing stack to track indices of days waiting
        for warmer temperatures.
        
        Time: O(n), Space: O(n)
        """
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stack of indices with decreasing temperatures
        
        for i in range(n):
            # Process all days that found their warmer day
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            
            stack.append(i)
        
        return result