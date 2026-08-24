class Solution:
    def occurences(self, s):
        L = [0 for i in range(26)]
        for c in s:
            L[ord(c)-ord("a")] += 1
        return tuple(L)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[self.occurences(s)].append(s)
        return list(d.values())