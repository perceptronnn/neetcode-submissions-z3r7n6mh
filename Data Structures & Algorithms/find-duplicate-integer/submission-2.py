class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        copy = list(nums)
        for i in range(len(nums)):
            print(nums)
            if copy[nums[i]-1] == -1:
                return nums[i]
            copy[nums[i] - 1] = -1
        return
        