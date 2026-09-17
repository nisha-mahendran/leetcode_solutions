# Last updated: 9/17/2026, 10:02:11 PM
1class Solution:
2    def permute(self, nums: list[int]) -> list[list[int]]:
3        finalOp=[]
4
5        def backtrack(current,rem):
6            if len(rem)==0:
7                finalOp.append(current)
8                return
9
10            for i in range(len(rem)):
11                newCurrent=current+[rem[i]]
12                newRem=rem[:i]+rem[i+1:]
13                backtrack(newCurrent,newRem)
14
15        backtrack([],nums)
16        return finalOp