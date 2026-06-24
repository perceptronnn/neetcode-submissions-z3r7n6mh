import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesHeap = [-i for i in stones]
        heapq.heapify(stonesHeap)
        while len(stonesHeap) > 1:
            s1 = abs(heapq.heappop(stonesHeap))
            s2 = abs(heapq.heappop(stonesHeap))
            if not s1 == s2:
                heapq.heappush(stonesHeap, -1 * (abs(s1 - s2)))
        heapq.heappush(stonesHeap, 0)
        return abs(stonesHeap[0])
