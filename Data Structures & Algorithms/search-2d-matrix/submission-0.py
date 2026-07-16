class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) -1

        while left <= right:
            mid = (left + right) // 2

            for i in matrix[mid]:
                if target == i:
                    return True
                    
            if target > matrix[mid][0]:
                left = mid +1
            elif target < matrix[mid][0]:
                right = mid -1 
            else:
                return True
        return False