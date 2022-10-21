class MedianFinder:

    def __init__(self):
        self.queue  = []
        self.counter = 0
    
    def findPosition(self, num):
        left = 0
        right = self.counter
        mid = (left + right) // 2
        while left < right:
            if self.queue[mid] <= num:
                left  = mid + 1
            else:
                right = mid
            mid = (left + right) // 2
        return mid

    def addNum(self, num: int) -> None:
        pos = self.findPosition(num)
        self.queue.insert(pos, num)
        self.counter += 1

    def findMedian(self) -> float:
        #print(self.queue)
        if self.counter % 2 == 0:
            x = self.counter // 2
            return (self.queue[x-1] + self.queue[x]) / 2
        else:
            x = self.counter // 2
            return self.queue[x] / 1.0
