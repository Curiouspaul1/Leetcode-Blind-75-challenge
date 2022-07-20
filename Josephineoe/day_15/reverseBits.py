class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
    #day 14 josephineoe
        for i in range(32):
           # remainder = n % 10 
            remainder = (n >> i) & 1
            reverse = reverse | (remainder << (31 - i)) #reverse*10 + remainder
            
        return reverse
    # n == 123456..didnt work
    # print(str(n)[::-1]) didnt work...