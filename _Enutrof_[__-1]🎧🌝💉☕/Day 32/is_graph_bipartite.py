class Solution:
    def recurse(self, index, prev_color=0):
        self.visited[index] = True
        self.color[index] = prev_color
        for i in self.graph[index]:
            if self.visited[i]:
                if self.color[index] == self.color[i]:
                    return False
            else:
                if not self.recurse(i,(prev_color+1) % 2):
                    return False
        return True
    def isBipartite(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        self.graph = graph
        self.visited = [False for i in range(length)]
        self.color = [None for i in range(length)]
        
        
            
        for i in range(length):
            if not self.visited[i]:
                if not self.recurse(i):
                    return False
        
        return True
        
