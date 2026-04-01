class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        return -1
"""
-1 0 2 4 6 8
 0 1 2 3 4 5

0 5 2
3 5 4

0 5 2
3 5 4
3 4 3
3 3
"""
        