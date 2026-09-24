class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # idea: search for the row that contains the target, then search for the target within the row
        
        # searching for the row 
        low_col = 0
        high_col = len(matrix) - 1
        search = -1

        # binary search 
        while low_col <= high_col:
            mid_col = (low_col + high_col) // 2
            if matrix[mid_col][0] <= target <= matrix[mid_col][-1]:
                search = mid_col
                break
            elif matrix[mid_col][0] < target:
                low_col = mid_col + 1            
            else:
                high_col = mid_col - 1

        if search == -1:
            return False

        # search within the row 
        low = 0
        high = len(matrix[0]) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[search][mid] == target:
                return True
            elif matrix[search][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False