class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.pre = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.front = Node()
        self.rear = Node()
        self.front.next = self.rear
        self.rear.pre = self.front

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        self.front.next.pre = node
        node.next = self.front.next
        self.front.next = node
        node.pre = self.front
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        self.rear.pre.next = node
        node.pre = self.rear.pre
        self.rear.pre = node
        node.next = self.rear
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front.next.next.pre = self.front
        self.front.next = self.front.next.next
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear.pre.pre.next = self.rear
        self.rear.pre = self.rear.pre.pre
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.pre.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.cap == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()