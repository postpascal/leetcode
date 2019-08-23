class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict={}
        self.capacity=capacity
        self.head=None
        self.tail=None
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # z=self.head
        # while z:
        #     print(z.key, z.value,"get")
        #     z=z.next
        # print("----get{}---".format(key))

        if key in self.dict:
            self.__dictouch(self.dict[key])
            return self.dict[key].value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # z=self.head
        # while z:
        #     print(z.key, z.value,"set")
        #     z=z.next
        # print("---set{}---".format(key))

        if key in self.dict:
            self.__dictouch(self.dict[key])

        node=ListNode(key,value)
        if len(self.dict)<self.capacity:
            self.dict[key]=node
            if not self.head:
                self.head=self.dict[key]
                self.tail=self.dict[key]
            elif self.head==self.tail:
                node.prev=self.head
                self.head.next=node
                
                self.tail=node
            else:
                self.tail.next=node
                node.prev=self.tail
                
                self.tail=node
        else:
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
            self.dict.pop(self.head.key)
            self.head=self.head.next
            self.dict[key]=node


    def __dictouch(self,node):
        p=node.prev
        n=node.next
        if len(self.dict)==1:
            return
        if n==None:
            return
        elif not p:
            node.prev=self.tail
            self.tail.next=node
            node.next=None
            self.tail=node

            self.head=n
            self.head.prev=None
        else:
            p.next=n
            n.prev=p
            node.prev=self.tail
            node.next=None
            self.tail=node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)