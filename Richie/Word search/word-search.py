class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        
        
        word_length = len(word)
        h, w = len(board), len(board[0])
        
        
        def dfs(r,c,point=0):
            if point >= word_length:
                return True
            
            if r<0 or c<0 or c>= w or r>=h or board[r][c] != word[point]:
                return False
            char = board[r][c]
            board[r][c] = "#"
            
            result = dfs(r+1,c , point + 1) or dfs(r-1, c, point +1)  or dfs(r,c +1 , point + 1) or dfs(r, c-1, point +1)
            if result:
                return result
            board[r][c] = char
            return result 
        
        for r in range(h):
            for c in range(w):
                if board[r][c] == word[0]:
                    if dfs(r, c):
                        return True
        return False
