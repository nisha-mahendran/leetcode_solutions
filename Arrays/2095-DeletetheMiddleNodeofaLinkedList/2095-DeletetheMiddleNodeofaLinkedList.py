# Last updated: 9/23/2026, 5:01:45 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
8        dummy=ListNode(0,head)
9        slow=dummy
10        fast=head
11
12        while fast is not None and fast.next is not None:
13            slow=slow.next
14            fast=fast.next.next
15        
16        slow.next=slow.next.next
17
18        return dummy.next 