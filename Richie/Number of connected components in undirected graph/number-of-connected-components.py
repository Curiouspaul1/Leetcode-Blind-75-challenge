class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [-1] * n
        rank = [0] * n
        
        def find(x):
            if parent[x] == -1:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]
            
        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot: return
            elif rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
                rank[yroot] += xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += yroot
        
        for x, y in edges:
            union(x, y)
            
        count = 0
        for p in parent:
            if p == -1:
                count += 1
                
        return count
