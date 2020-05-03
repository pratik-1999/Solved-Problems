
# You have to help Jawa to decide the minimum number of toffees he need to buy
# to satisfy his friends conditions. This minimum number of toffees in any
# possible distribution should satisfy his friends condition.
#
# Input:
# First line contains a single integer T denoting number of test cases.
# First line of each test case contains a single integer N denoting number of
# his friends.
# Second line of each test case contains N space separated integers denoting the
# least number of toffees his each friend want.
#
# Output:
# For each test case output single integer denoting minimum number of toffees
# he needs to buy to satisfy the condition.

import time
import numpy as np

def min_toffees(N, req_toffees):
    if N == 1:
        return sum(req_toffees)
    else:
        n_toff = [x-1 for x in req_toffees]
        return sum(n_toff)+1

def min_toffees_2(N, req_toffees): # vectorized approach
    req_toffees = np.array(req_toffees)
    one_less = np.ones((len(req_toffees)), dtype=int)
    if N == 1:
        return sum(req_toffees)
    else:
        return sum(req_toffees-one_less)+1


if __name__=="__main__":
    start = time.time()
    T= int(input())
    for _ in range(T):
        N = int(input())
        req_toffees = list(map(int, input().split()))
        print(min_toffees_2(N, req_toffees))
    print(time.time()-start)
