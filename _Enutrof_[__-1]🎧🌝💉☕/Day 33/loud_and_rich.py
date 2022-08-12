class Solution:
    def search(self, cur):
        for p in self.richer[cur]: 
            if p in self.visited:
                if self.visited[p] < self.q:
                    self.q = self.visited[p]
                    self.person = self.ans[p]
                
                continue
                
            if self.quiet[p] < self.q:
                self.q = self.quiet[p]
                self.person = p
            
            self.search(p)
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n_persons = len(quiet)        
        self.richer = defaultdict(list)
        self.quiet = quiet
        self.ans = [i for i in range(n_persons)]
        
        for i, j in richer:
            self.richer[j].append(i)

        self.visited = defaultdict(int)
    
        for i in range(n_persons):
            self.q, self.person = self.quiet[i], i

            self.search(i)
            self.ans[i] = self.person
            self.visited[i] = self.q

        return self.ans
      
