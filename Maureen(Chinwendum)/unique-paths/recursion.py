class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        big=max(m,n)
        small=min(m,n)
        row=[1]*big
        for i in range(small-1):
            new_row=[1]*big
            for j in range(big-2,-1,-1):
                new_row[j]=new_row[j+1]+row[j]
            row=new_ro

print(Solution().uniquePaths(2,2))