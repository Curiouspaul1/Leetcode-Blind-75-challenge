class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for nxt, prev in prerequisites:
            graph[nxt].append(prev)
            
        def is_cyclic(node):
            seen[node] = True
            recstack[node] = True
            
            for nei in graph[node]:
                if not seen[nei]:
                    if is_cyclic(nei):
                        return True
                elif recstack[nei]:
                    return True
                
            recstack[node] = False
            return False
                
        seen, recstack = [False] * numCourses, [False] * numCourses
        for node in range(numCourses):
            if not seen[node]:
                if is_cyclic(node):
                    return False
                
        return True
