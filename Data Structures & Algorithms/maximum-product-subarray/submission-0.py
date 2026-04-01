class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #prevProduct = nums[0]
        maxProduct = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == 0:
                if maxProduct < 0:
                    maxProduct = 0
                continue
            currProduct = nums[i]
            currMaxProduct = nums[i]
            for j in reversed(range(i)):
                if nums[j] == 0:
                    break
                currProduct *= nums[j]
                if currProduct > currMaxProduct:
                    currMaxProduct = currProduct
            if currMaxProduct > maxProduct:
                maxProduct = currMaxProduct
            #prevProduct = currProduct
        return maxProduct
        