import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window={}
        have=0
        dict_t={}
        res=[-1,-1]
        resLen=sys.maxsize
        l=0
        for i in t:
            dict_t[i]=1+dict_t.get(i, 0)
        need=len(dict_t)
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r], 0)
            
            if s[r] in dict_t and window[s[r]]==dict_t[s[r]]:
                have=have+1
            
            while have == need:
                print('here')
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=len(s[l:r+1])
                window[s[l]]=window[s[l]]-1
                if s[l] in dict_t and window[s[l]]<dict_t[s[l]]:
                    have=have-1
                l=l+1
        
        if resLen==sys.maxsize:
            return ""
        else:
            l,r=res
            return s[l:r+1]
                
            
        