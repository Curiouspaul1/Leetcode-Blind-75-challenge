class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        for i in s:
            count_s[i] += 1

        for i in t:
            count_s[i] -= 1  
        return all(i==0 for i in count_s.values())
    
