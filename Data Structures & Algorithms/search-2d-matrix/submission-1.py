class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        
        if top > bottom:
            return False
        row = matrix[mid]
        left, right = 0, len(row) - 1

        while left <= right:
            mid = (left + right) // 2

            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        
        return False