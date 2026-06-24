import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesHeap = [-1 * i for i in stones]
        heapq.heapify(stonesHeap)
        while len(stonesHeap) > 1:
            s1 = -1 * heapq.heappop(stonesHeap)
            s2 = -1 * heapq.heappop(stonesHeap)
            if not s1 == s2:
                heapq.heappush(stonesHeap, -1 * (abs(s1 - s2)))
        if len(stonesHeap) == 0:
            return 0
        return -1 * stonesHeap[0]
        