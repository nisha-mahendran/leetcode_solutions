# Last updated: 27/07/2026, 19:46:03
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero=0
        for curr in range(len(nums)):
            if nums[curr]!=0:
                (nums[curr],nums[lastNonZero])=(nums[lastNonZero],nums[curr])
                lastNonZero+=1
            curr+=1
        