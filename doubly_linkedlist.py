class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class doubly():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)
        
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
        
        else:            
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.length += 1

    def prepend(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length += 1

    def traverse(self, index):
        curNode = self.head
        for _ in range(index):
            curNode = curNode.next
            
        return curNode


    def delete(self,index):
        if index==self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        
        leaderNode = self.traverse(index-1)
        delNode = leaderNode.next
        holdNode = delNode.next
        leaderNode.next = holdNode
        holdNode.prev = leaderNode
        self.length -= 1
        
    def insert(self, index, value):
        newNode = Node(value)
        if index==0:
            self.prepend(value)
            return
        elif index>=self.length:
            self.append(value)
            return
        else:
            leaderNode = self.traverse(index-1)
            holdNode = leaderNode.next
            
            leaderNode.next = newNode
            newNode.prev = leaderNode
            newNode.next = holdNode
            holdNode.prev = newNode
            self.length += 1

    def printList(self):
        curNode = self.head
        arr = []
        for _ in range(self.length):
            arr.append(curNode.value)
            curNode = curNode.next
        print(arr)

if __name__ == "__main__":
    link = doubly()

    link.append(15)
    link.append(16)
    link.append(17)
    link.prepend(0)
    link.printList()
    
    link.insert(4, 21)
    link.printList()
    # link.insert(5, 11)

    link.delete(4)
    link.printList()

    link.delete(2)
    link.printList()
    link.delete(1)
    link.printList()
    # link.delete(0)
    print(link.length)