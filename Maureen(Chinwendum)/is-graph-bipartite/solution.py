class Solution:
     def isSafe(self,node,graph,color):
        q=deque()
        q.append(node)
        color[node]=0
        while(len(q)):
            crnt=q.popleft()
            for node in graph[crnt]:
                if node in color:
                    if color[crnt]==color[node]:
                        return False
                else: 
                    color[node]=1-color[crnt]
                    q.append(node)      
        return True
     def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color={}
        for i in range(n):
            if i not in color:
                if not self.isSafe(i,graph,color):
                    return False
        return True