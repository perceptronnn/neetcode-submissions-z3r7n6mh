class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        """
        [a, b, c, d, e]
        [0, 1, 2, 3, 4]
        """

        for i in range(len(nums)):

            print("i = " + str(i))
            print("initially")
            print(q)
            if q and q[0] <= i - k:
                q.popleft()
            print("after if")
            print(q)
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            print("after while")
            print(q)
            q.append(i)
            print("finally")
            print(q)

            if i >= k - 1:
                res.append(nums[q[0]])
            print(res)
            
        return res
        