class Solution

{

public:

    int mod = 1e9 + 7;

    typedef pair<int, int> pi;

    int dfs(vector<vector<pi>> &graph, vector<int> &dist, vector<int> &dp, int u)

    {

        if (u == 1)

            return 1;

        if (dp[u] != -1)

            return dp[u];

        dp[u] = 0;

        for (auto x : graph[u])

        {

            int v = x.first;

            if (dist[v] > dist[u])

                dp[u] = (dp[u] % mod + dfs(graph, dist, dp, v) % mod) % mod;

        }

        return dp[u] % mod;

    }

    void dijkstra(int n, vector<vector<pi>> &graph, int src, vector<int> &dist)

    {

        vector<bool> finalized(n + 1, false);

        priority_queue<pi, vector<pi>, greater<pi>> pq;

        dist[src] = 0;

        pq.push({0, src});

        while (!pq.empty())

        {

            int dist_u = pq.top().first;

            int u = pq.top().second;

            pq.pop();

            if (finalized[u] == true)

                continue;

            finalized[u] = true;

            for (auto x : graph[u])

            {

                int v = x.first;

                int wt = x.second;

                if (dist_u + wt < dist[v])

                {

                    dist[v] = dist_u + wt;

                    pq.push({dist[v], v});

                }

            }

        }

    }

    int countRestrictedPaths(int n, vector<vector<int>> &edges)

    {

        vector<vector<pi>> graph(n + 1);

        for (int i = 0; i < edges.size(); i++)

        {

            auto e = edges[i];

            graph[e[0]].push_back({e[1], e[2]});

            graph[e[1]].push_back({e[0], e[2]});

        }

        vector<int> dist(n + 1, INT_MAX);

        dijkstra(n, graph, n, dist);

        vector<int> dp(n + 1, -1);

        return dfs(graph, dist, dp, n);

    }

};
