class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits is None:
            return [1]
        elif (len(digits)==0): 
            return [1]
        elif (digits[len(digits)-1] == 9):
            return self.plusOne(digits[0:-1])+[0]
        else:
            return digits[:-1]+[(digits[-1]+1)]