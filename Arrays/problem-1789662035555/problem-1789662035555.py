# Last updated: 9/17/2026, 9:50:35 PM
1class Solution:
2    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
3        intervals.sort(key=lambda x:x[0])
4
5        result=[intervals[0]]
6
7        for start,end in intervals[1:]:
8            prevInterval=result[-1]
9
10            if start<=prevInterval[1]:
11                result[-1][1]=max(end,prevInterval[1])
12            else:
13                result.append([start,end])
14        return result 