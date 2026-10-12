class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def insert(self, value):
        self.items.append(value)

    def delete(self):
        if(self.isempty()):
            raise('queue is empty')
        else:
            return self.items.pop(0)

q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
print(q.items)

print(q.delete())
print(q.delete())
print(q.delete())
# q.delete()