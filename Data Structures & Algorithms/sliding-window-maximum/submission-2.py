import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k or len(nums) < k:
            return []
        
        max_heap = []
        results = []

        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))

        results.append(-max_heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))

            while max_heap and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            
            results.append(-max_heap[0][0])
        return results

        