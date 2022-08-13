INT_MAX = 1e10
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        self.visited = [0 for i in range(n+1)]
        self.distances = [INT_MAX for i in range(n+1)]
        self.distances[n] = 0
        self.outdegrees = [[] for i in range(n+1)]
        hq = []
        heapq.heappush(hq,[0,n])
        
        for edge in edges:
            self.outdegrees[edge[0]].append([edge[1],edge[2]])
            self.outdegrees[edge[1]].append([edge[0],edge[2]])
            
        while len(hq)>0:
            [distance,node] = heapq.heappop(hq)
            for neighbor in self.outdegrees[node]:
                if(distance + neighbor[1]<self.distances[neighbor[0]]):
                    self.distances[neighbor[0]] = distance + neighbor[1]
                    heapq.heappush(hq,[self.distances[neighbor[0]],neighbor[0]])
                
        
        self.memo = [-1 for i in range(n+1)]
        self.memo[n] = 1
        
        return int(self.dfs(1)) 
    
        
    def dfs(self, i:int):
        ans = 0
        if self.visited[i]==1 :
            return 0 
        if self.memo[i]>-1:
            return self.memo[i]
        
        self.visited[i] = 1
        for neighbor in self.outdegrees[i]:
            if self.distances[i]> self.distances[neighbor[0]]: 
                ans += self.dfs(neighbor[0])
                ans %=  1e9+7
        self.memo[i] = ans
        self.visited[i] = 0
        return self.memo[i] 
