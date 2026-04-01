class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for idx in range(len(nums) - k + 1):
            currentMax = nums[idx]
            for j in range(k):
                currentMax = max(currentMax, nums[idx + j])
            res.append(currentMax)
            idx += 1
        return res
        