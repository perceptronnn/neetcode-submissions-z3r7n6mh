class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        results = set()
        for idx in range(len(nums)):
            left = idx + 1
            right = len(nums) - 1
            needed = 0 - (nums[idx])
            while left < right:
                curr = nums[left] + nums[right]
                if curr > needed:
                    right -= 1
                elif curr < needed:
                    left += 1
                else:
                    results.add(tuple([nums[idx], nums[left], nums[right]]))
                    left += 1
                    right -= 1
        rs = []
        for r in results:
            rs.append(list(r))
        return rs