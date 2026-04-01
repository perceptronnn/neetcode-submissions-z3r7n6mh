import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        #speeds = list(range(1, mx + 1))
        #print(speeds)
        l, r = 1, mx
        res = mx
        while l <= r:
            mid = (l + ((r-l) // 2))
            print(l, r, mid)
            if self.isOk(piles, h, mid):
                print(mid)
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res

    def isOk(self, piles, h, k):
        totalTime = 0
        for pile in piles:
            totalTime += math.ceil(pile / k)
        return totalTime <= h

        