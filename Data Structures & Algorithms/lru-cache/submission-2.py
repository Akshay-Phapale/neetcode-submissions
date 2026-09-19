class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = Node(), Node()
        
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, next = self.right.prev, self.right

        prev.next, next.prev = node, node
        node.prev, node.next = prev, next
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] # only reason why we have key in Node 
