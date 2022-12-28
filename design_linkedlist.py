class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head == None:
            return -1
        else:
            curr = self.head
            idx = 0
            while curr:
                if idx == index:
                    return curr.data
                curr = curr.next
                idx += 1

        return -1

    def addAtHead(self, val: int) -> None:
        n = Node(val)
        if self.head == None:
            self.head = n

        else:
            n.next = self.head
            self.head = n

    def addAtTail(self, val: int) -> None:
        n = Node(val)
        if self.head == None:
            self.head = n
        else:
            curr = self.head
            while curr:
                if curr.next == None:
                    curr.next = n
                    break
                curr = curr.next

    def addAtIndex(self, index: int, val: int) -> None:
        n = Node(val)
        idx = 0

        if index == 0:
            if self.head:
                tempN = self.head
                self.head = n
                n.next = tempN
            else:
                self.head = n
        else:
            i = 1
            curr = self.head

            while curr:
                if i == index:
                    tempN = curr.next
                    curr.next = n
                    curr.next.next = tempN
                    break
                i += 1
                curr = curr.next

    def deleteAtIndex(self, index: int) -> None:
        idx = 0

        if self.head:
            curr = self.head
            if index == 0:
                self.head = curr.next
            else:
                while curr:
                    if idx + 1 == index and curr.next:
                        curr.next = curr.next.next
                    idx += 1
                    curr = curr.next


class Node:
    def __init__(self, data: int):
        self.next = None
        self.data = data

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)