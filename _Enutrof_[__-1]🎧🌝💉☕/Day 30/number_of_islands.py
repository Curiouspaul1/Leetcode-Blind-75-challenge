class Solution:
    def get_island(self, grid, i, j):
        queue = deque([(i,j)])
        while queue:
            r, c = queue.pop()
            if (r,c) in self.visited: continue
            self.visited.add((r, c))
            
            for r_offset, c_offset in [[0, 1], [0, -1], [-1,0], [1,0]]:
                row, col = r + r_offset, c + c_offset
                try:
                    assert row >= 0 and col >= 0
                    if grid[row][col] == "1":
                        queue.append((row, col))
                        
                except:
                    continue            
            
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        island = 0
        for i, row in enumerate(grid):
            for j, ele in enumerate(row):
                if ele == "1" and (i,j) not in self.visited:
                    island += 1
                    self.get_island(grid, i, j)
        return island
