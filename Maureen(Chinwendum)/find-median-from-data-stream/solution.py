class MedianFinder:

    def __init__(self):
		# create 2 heaps and keep a count of inserted elements
        self.upper, self.lower = [], []
        self.count = 0

    def addNum(self, num: int) -> None:
        # add elements evenly to both
		# make sure all elements in lower are smaller than upper
        if self.count == 0 or self.upper[0] > num:
            heappush(self.lower, -1 * num)
            
            if self.count % 2 == 0:
                heappush(self.upper, -1 * heappop(self.lower))
        
        else:
            heappush(self.upper, num)
            
            if self.count % 2 == 1:
                heappush(self.lower, -1 * heappop(self.upper))
        
        self.count += 1

    def findMedian(self) -> float:
        # if even elements are added, pop from both and divide by 2
		# else just return the smallest element in upper
        if self.count % 2 == 0:
            return (self.upper[0] + (-1 * self.lower[0])) /2
        
        return self.upper[0]