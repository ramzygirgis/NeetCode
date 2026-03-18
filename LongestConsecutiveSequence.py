from typing import List

def longestConsecutive1(self, nums: List[int]) -> int:
    num_set = set(nums)
    max_so_far = 0
    for n in num_set:
        if n - 1 not in num_set:
            index = 0
            while n + index + 1 in num_set:
                index += 1
            length = index + 1
            if length > max_so_far:
                max_so_far = length
    return max_so_far

def longestConsecutive2(self, nums: List[int]) -> int:
    max_so_far = 0
    for i in range(len(nums)):
        if nums[i] - 1 in nums:
            continue
        length = 1
        while nums[i] + length in nums:
            length += 1
        if length > max_so_far:
            max_so_far = length
    return max_so_far