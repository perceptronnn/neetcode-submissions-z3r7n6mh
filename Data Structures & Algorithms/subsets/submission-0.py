class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, path):
            if i == len(nums):
                res.append(path[:])
                print(res[-1])
                return

            backtrack(i+1, path)
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
            return
        backtrack(0, [])
        return res    