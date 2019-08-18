class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        def woker(pre,ino):
            if len(pre)<1:
                return None
            if len(pre)==1:
                return TreeNode(pre[0])
            i=0
            while pre[0]!=ino[i] and i<len(ino):
                i+=1

            root=TreeNode(pre[0])
            root.left=woker(pre[1:i+1],ino[:i])
            root.right=woker(pre[i+1:],ino[i+1:])
            return root
        w=woker(preorder,inorder)
        return w


from collections import defaultdict

d=defaultdict(list)
def recursiver(root,i):
    if root:
        d[i].append(root.val)
        recursiver(root.left,i+1)
        recursiver(root.right,i+1)

a=Solution()
r=a.buildTree([],[])
# r=a.buildTree([3,9,20,15,7],[9,3,15,20,7])
recursiver(r,0)
print(d.values())


