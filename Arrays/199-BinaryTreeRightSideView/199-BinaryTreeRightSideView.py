# Last updated: 9/22/2026, 6:25:03 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: TreeNode | None) -> list[int]:
9        if root is None:
10            return []
11
12        result=[]
13        queue=[root]
14        while queue:
15            currentLevelCount=len(queue)
16            for index in range(currentLevelCount):
17                currentNode = queue.pop(0)
18                if index==currentLevelCount-1:
19                    result.append(currentNode.val)
20                if currentNode.left is not None:
21                    queue.append(currentNode.left)
22                if currentNode.right is not None:
23                    queue.append(currentNode.right)
24        return result
25        