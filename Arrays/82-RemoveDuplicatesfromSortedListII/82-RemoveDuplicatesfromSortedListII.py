# Last updated: 9/17/2026, 9:44:11 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
8        dummy=ListNode(0,head)
9        current=head
10        prev=dummy
11
12        while current:
13            if current.next and current.val == current.next.val:
14                duplicateVal=current.val
15
16                while current and current.val == duplicateVal:
17                    current=current.next
18
19                prev.next=current
20
21            else:
22                prev=current
23                current=current.next
24
25        return dummy.next