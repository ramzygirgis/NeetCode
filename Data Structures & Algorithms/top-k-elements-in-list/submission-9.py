class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        pullback = defaultdict(set)
        for n in nums:
            pullback[counts[n]].add(n)
        
        l = len(nums)
        res = []
        while l > 0 and len(res) != k:
            res.extend(list(pullback[l]))
            l -= 1
        return res