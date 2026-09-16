# Last updated: 9/16/2026, 4:53:37 PM
1class Solution:
2    def longestSubarray(self, nums: List[int]) -> int:
3        start=0
4        end=0
5        zero=0
6        maxCount=0
7
8        while end<len(nums):
9            if nums[end]==0:
10                zero+=1
11
12            while zero>1:
13                if nums[start]==0:
14                    zero-=1
15
16                start+=1
17
18            count=end-start
19            maxCount=max(maxCount,count)
20
21            end+=1
22
23        return maxCount
24        