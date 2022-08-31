from typing import List
# x = [[1,4],[2,3],[3,4]]
class Solution:



    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted = []
        n = len(intervals)
        for i in range(n):
            sorted.append([intervals[i], i])
        sorted.sort()

        result = [-1]*n
        def binary_search(x):
            if sorted[n-1][0][0] < x : return -1
            l,r=0,n-1
            while l<=r:
                mid = l + (l-r)//2
                if sorted[mid][0][0] >= x: r =mid -1
                else: l=mid+1
            return sorted[l][1]
        for i in range(n):
            result[i] =binary_search(intervals[i][1])
        
        return result


    




x = Solution()
print(5//2)