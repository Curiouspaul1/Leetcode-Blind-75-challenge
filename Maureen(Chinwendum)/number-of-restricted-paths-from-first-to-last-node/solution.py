class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
	    #relaxed distances of all nodes from node n
        dist={i:sys.maxsize for i in range(1,n+1)}
        dist[n]=0
        mod=10**9+7
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((w,v))
            graph[v].append((w,u))
        pq=[]
        heapq.heappush(pq,(0,n))
        while pq:
            wt,node=heapq.heappop(pq)
            for new_wt,nei in graph[node]:
                if wt+new_wt<dist[nei]:
                    dist[nei]=wt+new_wt
                    heapq.heappush(pq,(wt+new_wt,nei))
		#simple memoized dp function to check if there exists a path with strictly decreasing dist from 1 to n
        @lru_cache(None)
        def dp(node):
            if node==n:
                return 1
            ans=0
            for _,nei in graph[node]:
                if dist[nei]<dist[node]:
                    ans+=dp(nei)
            return ans
        return dp(1)%mod