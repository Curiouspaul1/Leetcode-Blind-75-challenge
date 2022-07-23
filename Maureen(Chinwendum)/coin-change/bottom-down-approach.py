import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        array=[0]*(amount+1)
        
        x=1
        while x <= amount:
            min=sys.maxsize
            for y in coins:
                temp=x-y
                if temp>=0 and array[temp] != -1 and array[temp] < min: 
                    min=array[temp]+1
            if min==sys.maxsize:
                array[x]=-1
            else:
                array[x]=min
            x=x+1
        return array[-1]
                    
                    
                
                
        
        