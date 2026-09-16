# Last updated: 9/16/2026, 4:43:40 PM
1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        vowels={'a','e','i','o','u'}
4
5        count=0
6        maxCount=0
7
8        for i in range(0,k):
9            if s[i] in vowels:
10                count+=1
11
12        maxCount=count
13
14        for end in range(k,len(s)):
15            start=end-k+1
16
17            if s[end] in vowels:
18                count+=1
19
20            if s[start-1] in vowels:
21                count-=1
22
23            maxCount=max(count,maxCount)
24            
25        return maxCount