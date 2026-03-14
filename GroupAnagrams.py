from typing import List


def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
    counts = {}
    for s in strs:
        L = [0] * 26
        for c in s: # O(nm), where m is maxstringsize
            L[ord(c) - ord('a')] += 1
        counts[s] = L.copy()
    inverse = {}
    for s in strs:
        key = tuple(counts[s])
        inverse.setdefault(key, []).append(s)
    return list(inverse.values())


# **************************************************
      

def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
    dict2 = {}
    for string in strs:
        sorted_string = sorted(string)
        sorted_string = ''.join(sorted_string)
        if sorted_string not in dict2.keys():
            dict2[sorted_string] = [string]
        else:
            dict2[sorted_string].append(string)
    L = [dict2[sorted_string] for sorted_string in dict2.keys()]     
    return L 