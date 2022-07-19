class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int result=0;
        int num = 0;
        while(num<32) {
            result=result<<1;
            if(n&1) {
                result=result|1;
            }
            n=n>>1;
            num++;
        }
        return result;
    }
};
