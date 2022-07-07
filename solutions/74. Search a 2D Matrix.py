class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = 0
        
        while r < len(matrix)-1 and c < len(matrix[r])-1:
            if matrix[r][c] > target:
                return False
            elif matrix[r][c] == target:
                return True
            if matrix[r+1][c] <= target:
                r += 1
            else:
                c += 1
        
        while c < len(matrix[r]):
            if matrix[r][c] > target:
                return False
            elif matrix[r][c] == target:
                return True
            elif c == len(matrix[r])-1 and r < len(matrix)-1:
                r += 1
            else:
                c += 1
​
        return False
