# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(node):
            if not node:
                return None
            node.left,node.right=node.right,node.left
            helper(node.left)
            helper(node.right)
        helper(root)
        return root






class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
            