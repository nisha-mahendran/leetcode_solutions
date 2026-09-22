# Last updated: 9/22/2026, 6:07:33 AM
1class Solution:
2    def subsets(self, nums: list[int]) -> list[list[int]]:
3        res=[[]]
4        for num in nums:
5            tempRes=[]
6            for subset in res:
7                newSubset=subset+[num]
8                tempRes.append(newSubset)
9            res+=tempRes
10        return res