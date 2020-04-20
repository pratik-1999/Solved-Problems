import numpy as np

row, col = map(int, input().split())

mind = np.zeros(shape = (row,col))

for i in range(row):
    ins = list(map(int, input().split()))
    for j in range(col):
        mind[i][j] = ins[j]
    
def mind_palace():
    cases = int(input())
    for i in range(cases):
        find = int(input())
        if find in mind:
            x,y = np.where(mind == find)
            l = [int(x), int(y)]
            print(*l)
            
        else:
            l = [-1,-1]
            print(*l)

            
if __name__ == "__main__":
    mind_palace()