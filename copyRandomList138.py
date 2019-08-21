class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        self.dict = collections.defaultdict(Node)
        return self.dfs(head)

    def dfs(self, node):
        if node in self.dict:
            return self.dict[node]
        if not node:
            return
        clone = Node(node.val, None, None)
        self.dict[node] = clone
        clone.next = self.dfs(node.next)
        clone.random = self.dfs(node.random)
        return clone






# a=Solution()
# print(a.copyRandomList(["eat", "tea", "tan", "ate", "nat", "bat"]))