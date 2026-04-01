class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            temp = max(b, a + nums[i])
            a = b
            b = temp
        
        c = nums[1]
        d = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            temp = max(d, c + nums[i])
            c = d
            d = temp
        return max(b, d)

        