# min_freq是目前最小频次，更新只有两种情况：满了之后删除元素，新增之后min_freq=1；频次+1且当前频次的链表为空，更新min_freq+1.
class LFUCache:

    def __init__(self, capacity: int):
        self.data = {}
        self.cap = capacity
        self.lists = {}
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key]
            self.lists[node.cnt].remove(node)
            if self.lists[node.cnt].isEmpty() and node.cnt == self.min_freq:
                self.min_freq += 1
            node.cnt += 1
            if node.cnt not in self.lists or self.lists[node.cnt] is None:
                self.lists[node.cnt] = DoubleLinkedList()
            self.lists[node.cnt].insert_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.data:
            node = self.data[key]
            node.val = value
            self.lists[node.cnt].remove(node)
            if self.lists[node.cnt].isEmpty() and node.cnt == self.min_freq:
                self.min_freq += 1
            node.cnt += 1
            if node.cnt not in self.lists or self.lists[node.cnt] is None:
                self.lists[node.cnt] = DoubleLinkedList()
            self.lists[node.cnt].insert_head(node)
        else:
            if len(self.data) == self.cap:
                node = self.lists[self.min_freq].remove_tail()
                self.data.pop(node.key)
            new_node = Node(key, value, 1)
            self.data[key] = new_node
            if 1 not in self.lists or self.lists[1] is None:
                self.lists[1] = DoubleLinkedList()
            self.min_freq = 1
            self.lists[1].insert_head(new_node)


class Node:
    def __init__(self, key=0, val=0, cnt=0):
        self.key = key
        self.val = val
        self.cnt = cnt
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_tail(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node

    def insert_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def isEmpty(self):
        return self.head.next == self.tail
