class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        unrolled = []

        while matrix:
            try:
                unrolled.extend(matrix[0]) # right
                unrolled.extend([row[-1] for row in matrix[1:]]) # down
                if len(matrix) > 1:
                    unrolled.extend(matrix[-1][-2::-1]) # left
                if len(matrix[0]) > 1:
                    unrolled.extend([row[0] for row in matrix[-2:0:-1]]) # up
                matrix = [row[1:-1] for row in matrix[1:-1]]
            except:
                break
        return unrolled
            
