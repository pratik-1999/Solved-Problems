class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue():
    def __init__(self):
        self.rear = None
        self.front = None
        self.length = 0

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.front = newNode
            self.rear = self.front
            self.length += 1
            return
        rearNode = self.rear
        rearNode.next = newNode
        self.rear = newNode
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return "Under Flow"
        if self.length == 1:
            self.rear =None

        frontNode = self.front
        self.front = frontNode.next
        self.length -= 1
        return frontNode
        

    def peek(self):
        if self.length:
            print(self.front.value)
        else:
            print("Under Flow")

            
    def printQ(self):
        curNode = self.front
        arr = []
        for _ in range(self.length):
            arr.append(curNode.value)
            curNode = curNode.next
        print(arr)

if __name__ == "__main__":
    q = Queue()
    q.enqueue('Praxx')
    q.enqueue('Vish')
    q.enqueue('Sharry')
    q.printQ()
    q.dequeue()
    q.printQ()

    q.dequeue()
    q.printQ()
    q.dequeue()
    q.printQ()
    q.peek()
