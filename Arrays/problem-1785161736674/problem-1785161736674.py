# Last updated: 27/07/2026, 19:45:36
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        lastNonZero=0
7        for curr in range(len(nums)):
8            if nums[curr]!=0:
9                (nums[curr],nums[lastNonZero])=(nums[lastNonZero],nums[curr])
10                lastNonZero+=1
11            curr+=1
12        