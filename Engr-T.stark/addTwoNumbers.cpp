class Solution {
public:
    int getSum(int a, int b) {
        // if(a == 0) return b;
        // if(b == 0) return a;
        // while(b != 0)
        // {
        //     unsigned c = a & b;
        //     a = a ^ b;
        //     b = c << 1;
        // }
        vector<int> c = {a, b};
        a = accumulate(c.begin(), c.end(), 0);
        return a;
    }
};
