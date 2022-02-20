class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k
        self.front, self.end = None, None
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.front is None:
            self.front = Node(value)
            self.end = self.front
        else:
            self.end.next = Node(value)
            self.end = self.end.next
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self.front.next
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.end.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.length
