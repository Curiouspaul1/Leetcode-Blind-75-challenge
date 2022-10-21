class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp={}
        lis=[[] for i in range(len(nums)+1)]
        
        for num in nums:
            mapp[num]=mapp.get(num, 0)+1
            
        for i,c in mapp.items():
            lis[c].append(i)
        res=[]
        for r in range(len(nums),0,-1):
            for t in lis[r]:
                res.append(t)
            if len(res)==k:
                return res
                
            
        