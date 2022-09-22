class Solution {
public:
    string longestPalindrome(string s) {
      
        
        map<int, string>hash;
        hash[0] = ""; //edge case
        int maxi = 0;
        
        for(int x  = 0; x < s.size(); x++){
            int pos = 1;
            for(int y = x; y < s.size(); y++){
                if(s[y] == s[x]){
                string sub = s.substr(x,pos);
                    
                reverse(sub.begin(), sub.end());
                
                if(sub == s.substr(x,pos)){
                    if(sub.size() == s.size())
                        return s;
                    
                    hash[sub.size()] = sub;
                    if(sub.size() > maxi)
                        maxi = sub.size();
                    }
                    
                }

                pos++;
            }
        }
      
        return hash[maxi];
    }
};
