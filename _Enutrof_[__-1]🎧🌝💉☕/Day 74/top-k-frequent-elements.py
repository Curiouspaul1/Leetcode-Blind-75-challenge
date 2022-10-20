class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] +=1
        return [i[0] for i in sorted(counter.items(), key=lambda x: x[1])[-k:]]
