class Stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    def push(self, value):
        self.s.insert(0, value)

    def peek(self):
        if (self.s) == 0:
            raise Exception('stack is empty')
        else:
            return self.s[0]
    
    def pop(self):
        if (self.s) == 0:
            raise Exception('stack is empty')
        else:
            return self.s.pop(0)
        
stk = Stack()
stk.push(10)
stk.push(20)
stk.push(40)
# print(stk.peek())

print(stk.pop())
print('\n')
print("peek element here: ")
print(stk.peek())

