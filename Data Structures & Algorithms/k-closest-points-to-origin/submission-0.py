import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointTuples = []
        for point in points:
            pointTuples.append((point[0] ** 2 + point[1] ** 2, point))
        heapq.heapify(pointTuples)
        print(pointTuples)

        kClosest = []
        while k > 0:
            point = heapq.heappop(pointTuples)
            kClosest.append(point[1])
            k = k - 1
        return kClosest

