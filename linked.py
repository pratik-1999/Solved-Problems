class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None

    def prin(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

l1 = Linkedlist()
l1.head = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

l1.head.next = n2
n2.next = n3
n3.next = n4

l1.prin()
