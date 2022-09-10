class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def dfs(i, j, index):
            if i<0 or i>=rows or j<0 or j>=cols or index>=len(word) or board[i][j] != word[index] or (i,j) in visited:
                return False
            if index == len(word)-1: return True
            visited.add((i,j))
            c1 = dfs(i+1,j,index+1)
            c2 = dfs(i-1,j,index+1)
            c3 = dfs(i,j+1,index+1)
            c4 = dfs(i,j-1,index+1)
            visited.remove((i,j))
            return c1 or c2 or c3 or c4
			
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j,0): return True
        return False