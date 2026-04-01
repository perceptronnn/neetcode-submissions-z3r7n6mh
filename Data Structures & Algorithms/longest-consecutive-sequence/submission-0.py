class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = {}
        longest = 0
        current = 0
        for num in nums:
            if num not in visited:
                visited[num] = False
        
        for num in nums:
            if visited[num]:
                continue
            curr = num
            currentLeft = 0
            currentRight = 0
            while curr in visited and not visited[curr]:
                currentLeft += 1
                visited[curr] = True  
                curr -= 1
            curr = num + 1
            while curr in visited and not visited[curr]:
                currentRight += 1
                visited[curr] = True
                curr += 1
            current = currentLeft + currentRight
            longest = max(longest, current)
        return longest
        