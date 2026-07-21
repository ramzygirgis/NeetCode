class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tail = len(digits) - 1
        while tail >= 0 and digits[tail] == 9:
            tail -= 1
        if tail == -1:
            return [1] + [0]*len(digits)
        return digits[:tail] + [digits[tail] + 1] + (len(digits) - 1 - tail) * [0]