class Stack:
    def __init__(self):
        self.stack = []
        self.top = None
        self.length = 0
        self.bottom = None

    def push(self,value):
        if self.length == 0:
            self.stack.append(value)
            self.top = value
            self.bottom = value
            self.length += 1
            return self.stack
        self.stack.append(value)
        self.top = value
        self.bottom = self.stack[0]
        self.length += 1
        return self.stack

    def pop(self):
        if self.length == 0:
            return 'Under Flow'
        if self.length == 1:
            self.bottom == None
        deleted = self.stack.pop()
        self.length -= 1
        return deleted

    def peek(self):
        if self.length:
            print(self.stack[-1])
        else:
            print("Under Flow")

    def printStack(self):
        print(self.stack)

if __name__ == "__main__":
    stack = Stack()
    stack.push("Google")
    
    stack.push("Udemy")
    stack.push("Youtube")
    stack.printStack()
    stack.pop()
    stack.printStack()
    stack.pop()
    stack.printStack()
    stack.pop()
    stack.printStack()
    stack.peek()