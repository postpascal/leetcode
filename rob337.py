class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.getRes(root))
    def getRes(self, root):
        if not root:
            return (0, 0)
        leftRes = self.getRes(root.left)
        rightRes = self.getRes(root.right)
        return (max(leftRes) + max(rightRes), root.val + leftRes[0] + rightRes[0])