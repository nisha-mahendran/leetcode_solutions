# Last updated: 9/17/2026, 10:12:19 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def isPalindrome(self, head: ListNode | None) -> bool:
8        slow=head
9        fast=head
10
11        while fast and fast.next:
12            fast=fast.next.next
13            slow=slow.next
14
15        dummy=None
16        while slow:
17            temp=slow.next
18            slow.next=dummy
19            dummy=slow
20            slow=temp
21
22        first=head
23        second=dummy
24
25        while first and second:
26            if first.val!=second.val:
27                return False
28
29            first=first.next
30            second=second.next
31
32        return True