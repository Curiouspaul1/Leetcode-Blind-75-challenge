class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = defaultdict(int)
        minLength = float("inf")
        res = ""
        for char in t:
            counter[char] -= 1
            
        left  = 0
        
        for right in range(len(s)):
            if s[right] in counter:
                counter[s[right]] += 1
            while min(counter.values()) >= 0:
                if (right - left + 1) < minLength:
                    res = s[left:right+1]
                    minLength = (right-left)+1
                if s[left] in counter:
                    counter[s[left]] -= 1
                left +=1

        return res
