class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        res = 1
        maxf = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            
            maxf = max(maxf, counts[s[r]])
            
            while (r - l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return (res)
