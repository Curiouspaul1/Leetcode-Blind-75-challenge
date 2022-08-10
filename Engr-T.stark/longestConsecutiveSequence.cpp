int longestConsecutive(vector<int>& nums) {
    
    int l = nums.size();
    if(l==0)
        return 0;
    set<int ,greater<int>> st;
    
    
    
    for(int i = 0;i<l;i++)
    {
       st.insert(nums[i]);
    }
    if(st.size()==1)
        return 1;
    
    
   set<int,greater<int>> ::iterator it = st.begin();
    int tmp = *it;
    it++;
    int m1 = 0,m2  = INT_MIN;
    for(;it!=st.end();it++)
    {
       if(*it==tmp-1)
            m1++;
        else
            m1 = 0;
        m2 = max(m1,m2);
        tmp  = *it;  
    }
    
    
    return  m2+1;
}
};
