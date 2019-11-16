
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def helper(l,r):
            if not l and not r:
                return True
            elif not (l and r):
                return False
            elif l.val==r.val:
                return helper(l.left,r.left) and helper(l.right,r.right)
            else:
                return False
        
        return helper(p,q)