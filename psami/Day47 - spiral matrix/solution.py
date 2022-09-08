from re import L
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        output_list = []

        left, right = 0, COLS
        top, bottom = 0, ROWS

        while left < right and top < bottom:
            for i in range(left,right):
                output_list.append(matrix[top][i])
            top+=1

            for i in range(top,bottom):
                output_list.append(matrix[i][right-1])
            right -= 1

            if not(left < right and top < bottom):
                break

            for i in range(right -1, left-1, -1):
                output_list.append(matrix[bottom-1][i])
            bottom -=1

            for i in range(bottom-1, top-1,-1):
                output_list.append(matrix[i][left])

            left +=1

        return output_list

him = Solution()
print(him.spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))

