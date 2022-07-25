class Solution:
    def wordBreak(self, s: str, wordDict):
        wordDict = set(wordDict)
        memo = {}
        return self.dfs(s,memo,wordDict)
    
    def dfs(self,s,memo,wordDict):
        if s in memo:
            return memo[s]
        res = False
        for i in range(len(s)):
            prefix = s[:i+1]
            suffix = s[i+1:]
            
            if prefix in wordDict:
                if prefix == s:                   
                    return True
                if self.dfs(suffix,memo,wordDict):
                    return True 
            memo[s] = res
        return False
