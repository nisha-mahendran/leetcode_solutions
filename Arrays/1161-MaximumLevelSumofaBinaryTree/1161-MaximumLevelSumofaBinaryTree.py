# Last updated: 9/22/2026, 6:35:06 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: TreeNode | None) -> int:
9        if root is None:
10            return 0
11
12        maxSum = root.val
13        maxLevel=1
14
15        queue=[root]
16        currentLevel=1
17
18        while queue:
19            currentLevelCount=len(queue)
20            currentLevelSum=0
21
22            for i in range(currentLevelCount):
23                currentNode=queue.pop(0)
24                currentLevelSum+=currentNode.val
25
26                if currentNode.left is not None:
27                    queue.append(currentNode.left)
28                if currentNode.right is not None:
29                    queue.append(currentNode.right)
30            
31            if currentLevelSum > maxSum:
32                maxSum = currentLevelSum
33                maxLevel=currentLevel
34
35            currentLevel+=1
36
37        return maxLevel
38