# Last updated: 29/07/2026, 19:41:45
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        i=0
4        for j in range(0,len(nums)):
5            if nums[i]!=nums[j]:
6                i+=1
7                nums[i]=nums[j]
8        return i+1