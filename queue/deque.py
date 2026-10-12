class Dequeue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def insertAtEnd(self, value):
        self.items.append(value)

    def deleteAtFront(self):
        if self.isempty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def insertAtFront(self, value):
        self.items.insert(0, value)

    def deleteAtEnd(self):
        if self.isempty():
            raise Exception("Queue is empty")
        return self.items.pop()


dq = Dequeue()

dq.insertAtFront(10)
dq.insertAtEnd(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtEnd(50)

print(dq.deleteAtFront())   # 10
print(dq.items)             # [20, 30, 40, 50]