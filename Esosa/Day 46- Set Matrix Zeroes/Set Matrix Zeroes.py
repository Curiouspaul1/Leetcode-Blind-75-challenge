class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero= False
        
        
        #determine which rows/cols should be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c]=0
                    
                    if r>0:
                        matrix[r][0]=0
                    else:
                        rowZero = True
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix [0][c]==0 or matrix [r][0]==0:
                    matrix[r][c] =0
                    
        if matrix[0][0]==0:
            for r in range(ROWS):
                matrix[r][0]=0
        if rowZero:
            for c in range(COLS):
                matrix[0][c]=0
