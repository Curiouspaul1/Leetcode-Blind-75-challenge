class Solution:
    def search(self, r, c, i):
        if i == len(self.word):
            return True
        if (
            min(r, c) < 0
            or r >= self.row_length
            or c >= self.col_length
            or self.word[i] != self.board[r][c]
            or (r, c) in self.path
        ):
            return False
        self.path.add((r, c))
        res = (
            self.search(r + 1, c, i + 1)
            or self.search(r - 1, c, i + 1)
            or self.search(r, c + 1, i + 1)
            or self.search(r, c - 1, i + 1)
        )
        self.path.remove((r, c))
        return res
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.board = board
        self.row_length, self.col_length = len(board), len(board[0])
        self.path = set()

        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
            
        for r in range(self.row_length):
            for c in range(self.col_length):
                if self.search(r, c, 0):
                    return True
        return False
