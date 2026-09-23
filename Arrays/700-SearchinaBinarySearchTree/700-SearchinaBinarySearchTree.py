# Last updated: 9/23/2026, 4:55:23 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
9        if root is None:
10            return None
11
12        if root.val==val:
13            return root 
14
15        elif root.val>val:
16            return self.searchBST(root.left,val)
17
18        else:
19            return self.searchBST(root.right,val)