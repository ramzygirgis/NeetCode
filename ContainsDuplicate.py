from typing import List

class Solution1:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for n in set(nums):
            counts[n] = 0
        for n in nums:
            counts[n] += 1
        for n in set(nums):
            if counts[n] >= 2:
                return True
        return False
    
class Solution2:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize counting hashmap
        count = {}
        for num in nums:
            count[num] = 0
        # now, count for duplicates
        for num in nums:
            if count[num] == 1:
                return True
            count[num] += 1
        return False