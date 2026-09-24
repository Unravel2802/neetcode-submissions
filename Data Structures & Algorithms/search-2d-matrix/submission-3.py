class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # idea: search for the row that contains the target, then search for the target within the row
        
        # searching for the row 
        low_col = 0
        high_col = len(matrix) - 1
        search = 0

        # binary search 
        while low_col <= high_col:
            mid_col = (low_col + high_col) // 2
            if matrix[mid_col][0] == target:
                return True
            elif matrix[mid_col][0] < target:
                if matrix[mid_col][-1] >= target:
                    search = mid_col
                    break
                low_col = mid_col + 1            
            else:
                high_col = mid_col - 1

        # search within the row 
        print(search)
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