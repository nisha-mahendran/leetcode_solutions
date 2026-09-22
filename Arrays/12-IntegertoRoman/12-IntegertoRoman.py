# Last updated: 9/22/2026, 6:18:13 AM
1class Solution:
2    def intToRoman(self, num: int) -> str:
3        d={1000:"M",900:"CM",500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
4        output=''
5        for key,value in d.items():
6            count=num//key
7            output+=count*value
8            num%=key
9        return output 