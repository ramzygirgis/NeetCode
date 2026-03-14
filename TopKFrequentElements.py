from types import List


def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    length = len(nums)
    
    res = []
    for i in range(len(freq) - 1, 0 , -1):
        for i in freq[i]:
            res.append(i)
        if len(res) == k:
            return res
        

# **************************************************


def topKFrequent2(self, nums: List[int], k: int) -> List[int]:

    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    inverse = {}
    numset = set(nums)
    for n in numset:
        inverse.setdefault(counts[n], []).append(n)
    res = []
    
    m = 0
    for i in range(len(nums), 0, -1):
        if m >=k:
            break
        if i in inverse.keys():
            res += inverse[i]
            m += len(inverse[i])
    return res
        
        
