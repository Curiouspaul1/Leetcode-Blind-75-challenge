class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def tuplefy(word):
            res = [0 for _ in range(26)]
            base = ord('a')
            for c in word:
                res[ord(c) - base] += 1
            
            return tuple(res)
        
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[tuplefy(word)].append(word)
        
        return list(anagrams.values())
