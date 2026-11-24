# Last updated: 11/24/2026, 9:04:13 AM
1class Solution:
2    def longestConsecutive(self, nums: list[int]) -> int:
3        diary=set(nums) 
4        best = 0
5        for x in diary:
6            if x-1 not in diary:
7                length=1
8                while x+length in diary:
9                    length+=1
10                best=max(best,length)
11        return best
12