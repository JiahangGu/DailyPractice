class AllOne:

    def __init__(self):
        self.head = Node('', 100000000)
        self.tail = Node('', -1000000)
        self.data = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.data:
            node = self.data[key]
            node.cnt += 1
            self.move_forward(node)
        else:
            self.data[key] = Node(key, 1)
            self.add_tail(self.data[key])

    def dec(self, key: str) -> None:
        node = self.data[key]
        node.cnt -= 1
        if node.cnt > 0:
            self.move_backward(node)
        else:
            self.remove(node)
            self.data.pop(key)

    def getMaxKey(self) -> str:
        return self.head.next.s

    def getMinKey(self) -> str:
        return self.tail.prev.s

    def add_tail(self, node):
        node.next = self.tail
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def move_forward(self, node):
        while node.prev.cnt < node.cnt:
            tmp = node.prev
            tmp.prev.next = node
            node.prev = tmp.prev
            tmp.next = node.next
            node.next.prev = tmp
            tmp.prev = node
            node.next = tmp

    def move_backward(self, node):
        while node.next.cnt > node.cnt:
            tmp = node.next
            node.prev.next = tmp
            tmp.prev = node.prev
            tmp.next.prev = node
            node.next = tmp.next
            node.prev = tmp
            tmp.next = node


class Node:
    def __init__(self, s, cnt):
        self.s = s
        self.cnt = cnt
        self.next = None
        self.prev = None


allOne = AllOne()
allOne.inc("hello")
allOne.inc("hello")
print(allOne.getMaxKey())
print(allOne.getMinKey())
allOne.inc("leet")
print(allOne.getMaxKey())
print(allOne.getMinKey())