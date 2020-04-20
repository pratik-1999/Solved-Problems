class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        print(self.top.value)

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = self.top
            self.length += 1
        else:
            prevTop = self.top
            self.top = newNode
            newNode.next = prevTop
            self.length += 1

    def pop(self):
        if self.length == 0:
            print("Under Flow")
        if self.length == 1:
            self.bottom = None
        else:
            delNode = self.top
            self.top = delNode.next
            self.length -= 1
            return delNode

    def printStack(self):
        curNode = self.top
        arr = []
       
        for _ in range(self.length):
            arr.append(curNode.value)
            curNode = curNode.next
        print(*arr)



if __name__ == "__main__":
    stack = Stack()
    stack.push("Google")
    # stack.printStack()
    stack.push("Udemy")
    stack.push("Youtube")
    stack.printStack()
    stack.peek()
    stack.pop()
    stack.printStack()
    stack.pop()
    stack.printStack()
    stack.pop()
    stack.printStack()
    print(stack)
    stack.pop()
    stack.printStack()
    # print(stack)