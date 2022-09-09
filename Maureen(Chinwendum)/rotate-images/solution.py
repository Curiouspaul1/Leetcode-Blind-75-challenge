import itertools
import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rotated = np.rot90(np.array(matrix), -1)
        for i, j in itertools.product(range(rotated.shape[0]), range(rotated.shape[1])):
            matrix[i][j] = rotated[i][j]