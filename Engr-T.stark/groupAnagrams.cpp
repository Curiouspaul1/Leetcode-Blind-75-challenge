vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> map;
        for(auto &el:strs) {
            string tmp = el;
            sort(tmp.begin(), tmp.end());
            map[tmp].push_back(el);
        }
        vector<vector<string>>ans;
        for(auto &pair:map) {
            ans.push_back(pair.second);
        }
        return ans;
    }
