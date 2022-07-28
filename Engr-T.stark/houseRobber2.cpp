class Solution {
public:
    int robLinear(int l , int r , vector <int> &a)
    {
        int inc = 0 , exc = 0 , temp;
        for(int i = l ; i <= r ; i++)
        {
            temp = max(inc , exc);
            inc = exc + a[i];
            exc = temp;
        }
        return max(inc , exc);
    }
    int rob(vector <int> &a)
    {
        int n = a.size();
        if(n == 0)
            return 0;
        if(n == 1)
            return a[0];
        return max(robLinear(0 , n - 2 , a) , robLinear(1 , n - 1 , a));
    }
};
