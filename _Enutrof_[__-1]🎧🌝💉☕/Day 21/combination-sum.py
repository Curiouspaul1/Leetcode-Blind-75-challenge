class Solution:
    def dfs(self, i, cur, total):
        if total == self.target:
            self.res.append(cur.copy())
            return
        if i >= len(self.candidates) or total > self.target:
            return
        cur.append(self.candidates[i])
        self.dfs(i, cur, total+self.candidates[i])
        cur.pop()
        self.dfs(i+1, cur, total)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.candidates = candidates
        self.target = target
        
        self.dfs(0, [], 0)
        return self.res
      
