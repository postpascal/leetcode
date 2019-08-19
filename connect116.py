class Solution:
    def connect(self, root) :
        def recursiver(root):
            if root:
                if root.left:
                    root.left.next=root.right
                if root.next and root.right:
                    root.right.next = root.next.left
                recursiver(root.left)
                recursiver(root.right)

        recursiver(root)
        return root