class Solution:            
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        count_t = defaultdict(int)
        for i in t:
            count_t[i] += 1
        need = len(count_t)
        
        count_s = defaultdict(int)
        i = 0
        j = 0
        have = 0
        res = [-1, -1]
        resLen = 10**5
        while i < len(s) and j < len(s):
            count_s[s[j]] += 1
            
            if s[j] in count_t and count_s[s[j]] == count_t[s[j]]:
                have += 1
            
            while have == need:
                if  j -i+1 < resLen:
                    res = [i, j]
                    resLen = j - i + 1
                
                count_s[s[i]] -= 1
                if count_t[s[i]] > 0 and count_s[s[i]] < count_t[s[i]]:
                    have -= 1
                i += 1
                    
            j += 1
        return s[res[0]: res[1] + 1] if resLen < 10**5 else ""
                
            
