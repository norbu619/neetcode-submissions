class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) -1

        while left <= right:
            mid = (left + right) // 2
            ml = 0

            mr = len(matrix[mid]) -1
            while ml <= mr:
                mmid = (ml + mr) //2
                if target > matrix[mid][mmid]:
                    ml = mmid + 1
                elif target < matrix[mid][mmid]:
                    mr = mmid - 1
                else:
                    return True

                    
            if target > matrix[mid][0]:
                left = mid +1
            elif target < matrix[mid][0]:
                right = mid -1 
            else:
                return True
        return False