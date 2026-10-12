class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

# make to enter the enque time 
    def enqueue(self, value):
        # Queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        # First element
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.items[self.rear] = value

#  make to enter the dequeue time 
    def dequeue(self):
        # Queue is empty
        if self.front == -1:
            print("Queue is empty")
            return

        removed = self.items[self.front]
        self.items[self.front] = None

        # Last element
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Dequeued: {removed}")


# Driver Code
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

print(cq.items)

cq.dequeue()

print(cq.items)

cq.enqueue(60)

print(cq.items)

cq.dequeue()

print(cq.items)