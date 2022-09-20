from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]=1+count[ord(c)-ord("a")]
            result[tuple(count)].append(s)
        return result.values()
        print(ord("b"))
        # result=[]
        # idx = 0
        # while len(strs) != 0:
        #     new=[]
        #     new.append(strs[idx])
        #     temp=strs[idx]
        #     strs.pop(idx)
        #     i=0
        #     while i < len(strs):               
        #         if sorted(temp)==sorted(strs[i]):
        #             new.append(strs[i])
        #             strs.pop(i)
        #         else:
        #             i=i+1
        #     result.append(new)
        # return result
            