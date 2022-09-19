class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for word in strs:
            grouped[tuple(word.count(i) for i in string.ascii_lowercase)].append(word)
        return grouped.values()
                    
        
