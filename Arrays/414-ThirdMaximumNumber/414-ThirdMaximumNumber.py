# Last updated: 24/07/2026, 13:42:29
1class Solution:
2    def thirdMax(self, nums: List[int]) -> int:
3       firstMax=-inf
4       secondMax=-inf
5       thirdMax=-inf
6       for num in nums:
7           if firstMax==num or secondMax==num or thirdMax==num:
8              continue
9           if firstMax<=num:
10              thirdMax=secondMax
11              secondMax=firstMax
12              firstMax=num
13           elif secondMax<=num:
14              thirdMax=secondMax
15              secondMax=num
16           elif thirdMax<=num:
17              thirdMax=num
18       if thirdMax==-inf:
19           return firstMax
20       return thirdMax