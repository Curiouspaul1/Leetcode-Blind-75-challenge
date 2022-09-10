from copy import deepcopy
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)

        new = deepcopy(matrix)
        
        for r in range(ROWS):
            for c in range(ROWS):
                new[c][ROWS-r-1] = matrix[r][c]
                
        
        for r in range(ROWS):
            for c in range(ROWS):
                matrix[r][c] = new[r][c]
        