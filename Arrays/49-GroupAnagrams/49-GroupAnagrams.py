# Last updated: 11/24/2026, 8:30:33 AM
1class Solution:
2    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
3        dic={}
4        for word in strs:
5            label = "".join(sorted(word))
6            if label not in dic:
7                dic[label]=[]
8            dic[label].append(word)
9        return list(dic.values())