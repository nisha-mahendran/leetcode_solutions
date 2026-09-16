# Last updated: 9/16/2026, 9:26:14 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
8        if k==0 or not head or not head.next:
9            return head
10
11        length=1
12
13        tail=head #just like temp
14
15        while tail.next:
16            length+=1
17            tail=tail.next #to find length 
18
19        finalK=k%length 
20
21        tail.next=head #circular 
22
23        breakingIndex=length-finalK-1
24
25        current=head #traversing 
26
27        for i in range(breakingIndex):
28            current=current.next
29
30        newHead=current.next
31        current.next=None #remove the link
32
33        return newHead
34        