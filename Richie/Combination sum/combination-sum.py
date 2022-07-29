class Solution:
    def combinationSum(self, candidates):
        result = []
        
        def combination(remain, comb, index):
            if remain == 0:
                result.append(list(comb))
            elif remain < 0:
                return
            
            for i in range(index, len(candidates)):
                comb.append(candidates[i])
                combination(remain - candidates[i], comb, i)
                comb.pop()
        
        
        
        combination(target, [], 0)
        return result
