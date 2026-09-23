# Last updated: 9/23/2026, 4:59:10 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
8        dummy=ListNode(0,head)
9        slow=dummy
10        fast=head
11
12        for i in range(n):
13            fast=fast.next
14
15        while fast is not None:
16            slow=slow.next
17            fast=fast.next
18
19        slow.next=slow.next.next
20
21        return dummy.next
22        