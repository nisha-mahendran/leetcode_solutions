# Last updated: 29/07/2026, 18:43:05
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        candidate=0
4        count=0
5        for num in nums:
6            if count==0:
7                candidate=num
8            if candidate==num:
9                count+=1
10            else:
11                count-=1
12        return candidate
13