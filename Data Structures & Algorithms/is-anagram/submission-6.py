class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        L = [0 for i in range(26)]
        for c in s:
            L[ord(c) - ord('a')] += 1
        for c in t:
            if L[ord(c)-ord('a')] == 0:
                return False
            L[ord(c)-ord('a')] -= 1
        return True