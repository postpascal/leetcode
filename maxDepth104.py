class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node,n):
            a=n
            b=n
            if node.left:
                a=helper(node.left,n+1)
            if node.right:
                b=helper(node.right,n+1)
            return max(a,b)
        
        return helper(root,1) if root else 0