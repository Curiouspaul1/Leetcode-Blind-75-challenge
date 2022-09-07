class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_length = len(matrix)
        column_length = len(matrix[0])
        
        store = [[row, column] for column in range(column_length) 
                                 for row in range(row_length) 
                                 if matrix[row][column] == 0]
        seen_r = set()
        seen_c = set()
        for r, c in store:
            if r not in seen_r:
                seen_r.add(r)
                matrix[r] = [0] * column_length
            if c not in seen_c:
                seen_c.add(c)
                for row in range(row_length):
                    matrix[row][c] = 0
                
