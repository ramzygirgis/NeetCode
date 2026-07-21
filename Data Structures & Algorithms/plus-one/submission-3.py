class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tail = len(digits) - 1
        while tail >= 0 and digits[tail] == 9:
            digits[tail] = 0
            tail -= 1
        if tail == -1:
            return [1] + digits
        digits[tail] += 1
        return digits