string minWindow(string s, string t) {
        
        int cnt[128];
        memset(cnt,0,sizeof(cnt));
        for(int i=0;i<t.length();i++) cnt[t[i]]++;
        int rem = t.length();
        int l=0,r=0,minStart = 0, minLen = INT_MAX;
        
        while(r<s.length())
        {
            cnt[s[r]]--;
            if(cnt[s[r]]>=0) rem--;
            r++;
            
            while(rem==0)
            {
                if(r-l<minLen)
                {
                    minLen = r-l;
                    minStart = l;
                }
                
                cnt[s[l]]++;
                if(cnt[s[l]]>0) rem++;
                l++;
            }
        }
        
        return minLen!=INT_MAX ? s.substr(minStart, minLen) : "";
    }
