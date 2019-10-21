# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if not node:
                return 0,0
            else:
                l,ml=helper(node.left)
                r,mr=helper(node.right)
                return 1+max(l,r), max(ml,mr, l+r)
        _,y =helper(root)
        
        return y