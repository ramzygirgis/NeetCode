class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tail = len(digits) - 1
        zeros = []
        while tail >= 0 and digits[tail] == 9:
            tail -= 1
            zeros.append(0)
        if tail == -1:
            return [1] + zeros
        return digits[:tail] + [digits[tail] + 1] + zeros