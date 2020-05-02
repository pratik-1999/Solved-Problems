import numpy as np
import time


def main(A1, A2):

    wins = 0
    if max(A1)<min(A2):
        return 0
        
    for a1 in A1:
        
        roi = [a2 for a2 in A2 if a2<a1]

        if roi:
            to_pop = max(roi)
            i = A2.index(to_pop)
            A2.pop(i)
            wins += 1
         
    return wins


def main_2(A1, A2): # Vectorized to increase speed
    A2 = np.array(A2)
    
    wins = 0
    if max(A1)<min(A2):
        return 0
        
    for a1 in A1:
        
        roi = A2[A2<a1]
        # print (type(roi))
        if len(roi)>0:                
            to_pop = np.max(roi)
            i = np.where(A2 == to_pop)[0][0]
            A2 = np.concatenate([A2[:i],A2[i+1:]])
            
            wins += 1
    
    return wins


if __name__=="__main__":
    start = time.time()
    T=int(input())
    for _ in range(T):
        N = int(input())
        A1 = list(map(int, input().split()))
        A2 = list(map(int, input().split()))
        print(main_2(A1, A2))
    print(time.time() - start)

# Test
# 1
# 10
# 3 6 7 5 3 5 6 2 9 1 
# 2 7 0 9 3 6 0 6 2 6
# ans - 7