class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        rowIdx = -1
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid, rowIdx)
            if target == matrix[mid][0] or target == matrix[mid][-1]:
                return True
            print(matrix[mid][0], matrix[mid][-1])
            if target > matrix[mid][0] and target < matrix[mid][-1]:
                rowIdx = mid
                print(rowIdx)
                break
            if target > matrix[mid][-1]:
                l = mid + 1
            if target < matrix[mid][0]:
                r = mid - 1
        
        if rowIdx == -1:
            return False
        
        l, r = 0, len(matrix[rowIdx]) - 1
        while l < r:
            mid = (l + r) // 2
            if target == matrix[rowIdx][mid]:
                return True
            if target < matrix[rowIdx][mid]:
                r = mid
            else:
                l = mid + 1
        return False

            
        