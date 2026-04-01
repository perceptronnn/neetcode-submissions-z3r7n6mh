class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct, rightProduct = [1] * len(nums), [1] * len(nums)

        currProd = nums[0]
        for i in range(1, len(nums)):
            leftProduct[i] = currProd 
            currProd = leftProduct[i] * nums[i]
        
        currProd = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            rightProduct[i] = currProd
            currProd = rightProduct[i] * nums[i]
        
        print(leftProduct)
        print(rightProduct)
        product = [1] * len(nums)
        for i in range(len(nums)):
            product[i] = leftProduct[i] * rightProduct[i]
        
        return product
        