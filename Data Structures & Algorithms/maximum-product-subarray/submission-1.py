class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevMaxProd = nums[0]
        prevMinProd = nums[0]
        maxProd = nums[0]
        for i in range(1, len(nums)):
            currMaxProd = max(prevMaxProd * nums[i], prevMinProd * nums[i], nums[i])
            currMinProd = min(prevMaxProd * nums[i], prevMinProd * nums[i], nums[i])
            if currMaxProd > maxProd:
                maxProd = currMaxProd
            prevMaxProd = currMaxProd
            prevMinProd = currMinProd
        return maxProd