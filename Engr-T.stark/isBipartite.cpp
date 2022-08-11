class Solution {
    bool dfs(int node, vector<vector<int>>& graph, vector<int>& color) {
        for(int ad : graph[node]) {
            if(color[ad] == color[node]) return false;
            else if(!color[ad]) {
                color[ad] = color[node] == 1 ? 2 : 1;
                if(!dfs(ad, graph, color)) return false;
            }
        }
        return true;
    }
    
public:
    bool isBipartite(vector<vector<int>>& graph) {
        vector<int> color(graph.size(), 0);
        
        for(int i=0; i<color.size(); i++) {
            if(!color[i]) {
                color[i] = 1;
                if(!dfs(i, graph, color)) return false;
            }
        }
        return true;
    }
};
