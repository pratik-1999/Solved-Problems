class Difference:
    def __init__(self, a):
        self.__elements = a

# Add your code here

    def computeDifference(self):
        b = self.__elements.sort()
        return b
    
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()
