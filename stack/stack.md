# stack concept 

1. Calculate the lenghth of the stack 
```python
 def length(self):
        return len(self.s)
```
2. make the push function which insert last position 
        a. insert at the o th position with value 
```python 
    def push(self, value):
        self.s.insert(0, value)
```
3. Address the pointer of the stack 
    a. at first check if the s == 0 then it's empty
    b. else it denote the index 0 of stack 
```python
    def peek(self):
        if (self.s) == 0:
            raise Exception('stack is empty')
        else:
            return self.s[0]
```
4. Pop from the stack

    a. if the stack is fully empty then stack have no value 
    b. else popm from the last input element 

```python 
        def pop(self):
        if (self.s) == 0:
            raise Exception('stack is empty')
        else:
            return self.s.pop(0)
```