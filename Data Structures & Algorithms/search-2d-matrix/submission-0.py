class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1

        while top <= bottom: 
            mid = top + (bottom - top) // 2

            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else: 
                break

        if top > bottom: 
            return False
        
        row = matrix[top + (bottom - top) // 2]
        
        r, l = 0, len(row) - 1

        while r<=l:
            mid = l + (r-l) // 2

            if row[mid] > target:
                l = mid - 1
            elif row[mid] < target:
                r = mid + 1
            else:
                return True
        return False