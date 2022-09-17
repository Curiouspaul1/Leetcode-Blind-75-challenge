class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        for i in s:
            count_s[i] += 1

        for i in t:
            count_s[i] -= 1  
        return all(map(lambda i: i==0, count_s.values()))
    
