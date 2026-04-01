class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = nums[0]

        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l = mid + 1
            else:
                r = mid - 1
                ans = min(ans, nums[mid])
        return ans
        