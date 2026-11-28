# Last updated: 11/28/2026, 9:41:52 AM
1class Solution:
2    def majorityElement(self, nums: list[int]) -> int:
3        ans=nums[0]
4        count=0
5        for num in nums:
6            if count == 0:
7                ans=num
8            if num == ans:
9                count+=1
10            else:
11                count-=1
12        return ans 
13
14