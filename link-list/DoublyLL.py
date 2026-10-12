class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None

# INSERTION AT THE END OF DOUBLE-LINK-LIST
    def inserAttheEnd(self, value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return 
        t = self.head
        while (t.next != None):
            t = t.next

        t.next = temp
        temp.prev = t


# INSERTION AT THE BEGINING 
    def insertAtBB(self, value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp


# INSERTION AT THE MIDDLE 
    def insertInMid(self , value , x):
        t = self.head
        while(t.next != None):
            if(t.data == x):
                break
            else:
                t = t.next

        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

# PRINT THE DOUBLE LINK LIST 
    def prinDLL(self):
        t1 = self.head
        while (t1.next != None):
            print(t1.data, end='<-->')
            t1 = t1.next
        print(t1.data)

# DELETION AT ANY POSITION OF DLL
    def deletionDLL(self, value):
        if self.head == None:
            print("Linked List is empty")
            return

        t = self.head

    # Delete head
        if t.data == value:
            self.head = t.next
            if self.head != None:      # Handle single-node list
                self.head.prev = None
                return

    # Traverse the list
        while t.next != None:
            if t.data == value:
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            t = t.next                 # <-- Missing in your code

    # Check the last node
        if t.data == value:
            t.prev.next = None
            return

    print("Value not found")


obj = DoublyLL()
obj.inserAttheEnd(10)
obj.inserAttheEnd(20)
obj.inserAttheEnd(30)
obj.insertInMid(60 ,20)
obj.insertAtBB(45)
obj.deletionDLL(30)
obj.prinDLL()
