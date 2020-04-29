import itertools
import numpy as np

def possible_formations(N, K):
    numbers = np.array(list(range(1,N+1)))
    roi = numbers[numbers>=K] 
    if K>N:
        return 0

    if K>N/2:
        return 1
    results = []
    for i in range(1, (N//K)+1):
        li = [seq for seq in itertools.combinations_with_replacement(roi, i) if sum(seq)==N]
        results.conacat(li)
    return len(results)        



# Write your code here
if __name__ =="__main__":
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        print(possible_formations(N, K))