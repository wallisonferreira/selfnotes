class Stack:
    def __init__(self):
        self.items = []
        
    def pop(self):
        return self.items.pop()
    
    def push(self, item):
        self.items.append(item)
        
    def items(self):
        return self.items
        
    def items_string(self):
        return "".join(self.items)
    
    def size(self):
        return len(self.items)
        
word = 'yesterday'

stack = Stack()

for w in word:
    stack.push(w)
    
reversed_string = ""
for i in range(stack.size()):
    reversed_string += stack.pop()
    
print(reversed_string)