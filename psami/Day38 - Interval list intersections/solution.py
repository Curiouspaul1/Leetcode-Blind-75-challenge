from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output_list = []
        aptr = 0
        bptr = 0
        la = len(firstList)
        lb = len(secondList)

        if la == 0 or lb ==0:
            return []
        while aptr < la and bptr < lb:
            a1 = firstList[aptr][0]
            a2 = firstList[aptr][1]
            b1 = secondList[bptr][0]
            b2 = secondList[bptr][1]
   
            if b2 >= a1 and a2 >= b1:
                output_list.append([max(a1,b1),min(a2,b2)])
            if firstList[aptr][1] > secondList[bptr][1]:
                bptr +=1
            else: 
                aptr += 1
        
        return output_list


b = Solution()
print(b.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))