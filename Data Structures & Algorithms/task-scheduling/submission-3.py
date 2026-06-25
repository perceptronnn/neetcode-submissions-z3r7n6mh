class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        t = 0
        q = deque()
        while maxHeap or q:
            t += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, t + n])
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        return t


