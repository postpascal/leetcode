# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def helper(t, s):
            if not t: return 0
            return int(t.val == s) + helper(t.left, s-t.val) + helper(t.right, s-t.val)
            
        if not root:
            return 0
        res = int(root.val == sum)
        res = res + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        res = res + helper(root.left, sum-root.val) + helper(root.right, sum-root.val)
        
        return res