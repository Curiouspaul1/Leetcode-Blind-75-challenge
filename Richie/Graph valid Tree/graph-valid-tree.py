def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
        adj_list = collections.defaultdict(set)
        visited = set()
        
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
        

        
            
        k = self.checkCycle(adj_list, 0, None, visited)
        
        if len(visited) == n:
            if k == False:
                return True
            
        return False
    
    
    def checkCycle(self, adj_list, source, parent, visited):

        visited.add(source)

        for v in adj_list[source]:
            
            if v not in visited:
                if self.checkCycle(adj_list, v, source, visited):
                    return True
            else:
                if v != parent:
                    return True
        
        return False
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
        adj_list = collections.defaultdict(set)
        visited = set()
        
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
        
        

            
        k = self.checkCycle(adj_list, 0, None, visited)
        
        if len(visited) == n:
            if k == False:
                return True
            
        return False
    
    
    def checkCycle(self, adj_list, source, parent, visited):

        visited.add(source)

        for v in adj_list[source]:
            
            if v not in visited:
                if self.checkCycle(adj_list, v, source, visited):
                    return True
            else:
                if v != parent:
                    return True
        
        return False
