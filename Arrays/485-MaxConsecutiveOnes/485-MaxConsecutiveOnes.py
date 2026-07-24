# Last updated: 24/07/2026, 11:25:17
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best_streak=0
        curr_streak=0
        for n in nums:
            if n==1:
                curr_streak+=1
            else:
                curr_streak=0
            if best_streak <curr_streak:
                best_streak=curr_streak
        return best_streak
            