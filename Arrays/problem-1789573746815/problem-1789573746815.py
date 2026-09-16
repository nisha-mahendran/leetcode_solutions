# Last updated: 9/16/2026, 9:19:06 PM
1class Solution:
2    def isUgly(self, n: int) -> bool:
3        if n<=0:
4            return False
5
6        while n%2==0:
7            n=n//2
8
9        while n%3==0:
10            n=n//3
11        
12        while n%5==0:
13            n=n//5
14
15        return n==1