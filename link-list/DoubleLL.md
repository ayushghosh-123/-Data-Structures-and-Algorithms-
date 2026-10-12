# Double Link_List

A doubly linked list is a more complex data structure than a singly linked list, but it offers several advantages. The main advantage of a doubly linked list is that it allows for efficient traversal of the list in both directions. This is because each node in the list contains a pointer to the previous node and a pointer to the next node. This allows for quick and easy insertion and deletion of nodes from the list, as well as efficient traversal of the list in both directions.

Representation of Doubly Linked List in Data Structure

### In a data structure, a doubly linked list is represented using nodes that have three fields:

1. Data
2. A pointer to the next node (next)
3. A pointer to the previous node (prev)

Now study more detail [https://www.geeksforgeeks.org/dsa/doubly-linked-list/]

### Explain the algorithm : 

1. INSERTION AT THE END OF DOUBLE-LINK-LIST
2. INSERTION AT THE BEGINING
3. INSERTION AT THE MIDDLE
4. DELETION AT ANY POSITION OF DLL
5. PRINT THE DOUBLE LINK LIST

### 1. INSERTION AT THE END OF DOUBLE-LINK-LIST -

A. AT FIRST MAKLE A TEMPORARY NODE 
B. THEN CHECK IF THE HEAD IS NONE SO ASSING SELF.HEAD = TEMP 
C. IF NOT STORE SELF.NODE IN POINTER 
D. AND THE POINTER TRAVEL AT THE LAST AT THE POINT THE LOOP SATISFIED T.NEXT = NONE AND STORE IT ONE BY ONE 
E. THEN THE POINTER NEXT VALUE IN TEMP
F. AND TEMP PREV VALUE IN PONTER 
```PYTHON
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
```
### 2. INSERTION AT THE BEGINING -

A. MAKE A TEMPORARY NODE 
B. IF SELF.HEAD = NONE THEN THE SELF.HEAD ASSIGN THE TEMP 
C. ELSE THE TEMP.NEXT = SELF.HEAD
D. SELF.HEAD.PREV = TEMP
E. SELF.HEAD = TEMP

 ```PYTHON 
    def insertAtBB(self, value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
 ```

### 3. INSERTION AT THE MIDDLE-

A. POINTER TO STORE THE HEAD
B. TRAVERSE THE END OF THE ARRAY 
C. CHECK THE POSITION IN IF MATCH THE VALUE, SO BREAK
D. ELSE TRAVESRSE NEXT NODE 
E. MAKE A TEMPORARY NODE temp = Node(value)
F. THEN TEMP NODE FILE NEXT ADRESS WITH T.NEXT
G. T.NEXT.PREV STORE TEMP
H. T.NEXT STORE TEMP NODE ADDRESS
I. TEMP.PREV STORE THE T ADDRESS

```PYTHON
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
```

### 4. DELETION AT ANY POSITION OF DLL
A. CHECK THE HEAD IS NONE IF THAT THEN LIST IS EMPTY 
B. IF NOT THEN THE POINTER STORE THE HEAD POSITION
C. AT FIRST CHECK THE HEAD POSITION IF THAT THE NONE SHIFT NOT THE THE HEAD POINT PREVIOUS
D. AT ANY POSTION THEN TRAVERSE THROUGH THE LIST IF MATCH THE VALUE POINTER NEXT NEXT NODE VALUE AND NEXT NODE PREVIOUS STORE PREVIOUS NODE ADDRESS . 
E.  AT THE LAST POSITTION OF LIST THEN THE NEXT NODE MAKE THE NONE 

```PYTHON 
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
```

### 5. PRINT THE LINK-LIST -

AS SAME AS SINGLE LINK-LIST 