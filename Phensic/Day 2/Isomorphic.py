class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}
        
        for c1, c2 in zip(s, t):
            if((c1 in map1 and map1[c1] != c2 ) or (c2 in map2 and map2[c2] != c1)):
                return False
            map1[c1] = c2
            map2[c2] = c1
        return True 