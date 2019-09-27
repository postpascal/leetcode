class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            l = root.left
            r = root.right
            l = self.flatten(l)
            r = self.flatten(r)
            root.left = None
            root.right = l
            head = root
            while head.right:
                head = head.right
            head.right = r
            return root