# from itertools import permutations
from random import shuffle
import numpy as np

def p_smallest(N, K, P):
    shuf_list = np.arange(1,N+1)
    shuffle(shuf_list)
    rem_list = list(map(int, input().split()))
    
    shuf_k = [i for i in shuf_list if i not in rem_list]
    
    if P > N-K:
        print(-1)
    else:
        print(sorted(shuf_k)[P-1])


if __name__ == "__main__":
    test_case = int(input())
    
    for t in range(test_case):
        N, K, P = map(int, input().split())
        p_smallest(N,K,P)