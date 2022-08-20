class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        queue = []
        while i < len(firstList) and j < len(secondList):
            first, second = firstList[i], secondList[j]
            
            if first[0] <= second[1] and second[0] <= first[1]:
                queue.append([max(first[0], second[0]), min(first[1], second[1])])
                remainder = [queue[-1][1]+1, max(first[1], second[1])]
            else:
                remainder = first if first[1] > second[1] else second
            
            # update
            if remainder[1] == first[1]:
                firstList[i] = remainder
                j += 1
            elif remainder[1] == second[1]:
                secondList[j] = remainder
                i += 1
            else:
                i += 1
                j += 1
        return queue
