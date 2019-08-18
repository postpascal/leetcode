from collections import defaultdict
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        d=defaultdict(list)
        def recursiver(root,i):
            if root:
                d[i].append(root.val)
                recursiver(root.left,i+1)
                recursiver(root.right,i+1)
        recursiver(root,0)
        for k,v in d.items():
            if k%2==1:
                d[k]=d[k][::-1]
        return d.values()