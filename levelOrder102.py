# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        d=defaultdict(list)
        def recursiver(root,i):
            if root:
                d[i].append(root.val)
                recursiver(root.left,i+1)
                recursiver(root.right,i+1)
        recursiver(root,0)
        return d.values()