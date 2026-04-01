class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for idx in range(len(nums)):
            if nums[idx] in remainder:
                return sorted([idx, remainder[nums[idx]]]) 
            remainder[target - nums[idx]] = idx

        