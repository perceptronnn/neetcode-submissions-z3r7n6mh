class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        l, r = 0, len(nums) - 1
        ans = float("inf")
        while l <= r:
            mid = l + (r - l) // 2
            print(l, mid, r)
            print(nums[l], nums[mid], nums[r])
            #ml = mid - 1 if mid != 0 else r
            #mr = mid + 1 if mid != r else l
            #if nums[ml] > nums[mid] and nums[mr] > nums[mid]:
            #    return nums[mid]
            #else:
            ans = min(ans, nums[mid])
            if nums[mid] < nums[r]:                
                r = mid - 1
            else:
                l = mid + 1
        return ans




"""
[8 9 1 2 3 4 5 6 7]
[3 4 5 6 7 8 9 1 2]
""" 
        