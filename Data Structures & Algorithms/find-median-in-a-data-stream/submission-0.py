class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            if len(self.right) == 0 or num <= self.right[0]:
                heapq.heappush(self.left, -num)
                return
            else:
                rTop = heapq.heappop(self.right)
                heapq.heappush(self.left, -rTop)
                heapq.heappush(self.right, num)
                return
        
        if len(self.left) < len(self.right):
            if num <= self.right[0]:
                heapq.heappush(self.left, -num)
                return
            else:
                rT = heapq.heappop(self.right)
                heapq.heappush(self.left, -rT)
                heapq.heappush(self.right, num)
                rT = heapq.heappop(self.right)
                heapq.heappush(self.left, -rT)
                return
        
        if len(self.left) > len(self.right):
            if num >= -1 * self.left[0]:
                heapq.heappush(self.right, num)
                return
            else:
                lT = heapq.heappop(self.left)
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, -1 * lT)
                return

    def findMedian(self) -> float:
        if not self.left and not self.right:
            return 0
        if len(self.left) == len(self.right):
            return ((-1 * self.left[0]) + self.right[0]) / 2
        return -1 * self.left[0]
        
        