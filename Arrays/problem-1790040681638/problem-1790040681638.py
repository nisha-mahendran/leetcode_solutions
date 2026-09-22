# Last updated: 9/22/2026, 7:01:21 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
9        leaves1=[]
10        leaves2=[]
11        self.dfs(root1,leaves1)
12        self.dfs(root2,leaves2)
13
14        return leaves1==leaves2
15
16    def dfs(self,node,leaves):
17        if node is None:
18            return 
19
20        if node.left is None and node.right is None:
21            leaves.append(node.val)
22            return
23
24        self.dfs(node.left,leaves)
25        self.dfs(node.right,leaves)
26
27
28
29        