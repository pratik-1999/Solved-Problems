import numpy as np
from collections import defaultdict

num_stats = defaultdict(list)

def is_prime(n):
    end = int(np.ceil(np.sqrt(n)))
    for div in range(2, end+1):
        if n%div==0 & div!=n:
            return 0
        elif div==end:
            return 1
        
        
def get_divisors(n):
    divs = [n]
    end = int(n//2)
    for i in range(1, end+1):
        if n%i==0:
            divs.append(i)
    return list(set(divs))

def strange_num(X, K, num_stats, start, limit):
    # Pre-Check 
    for k, v in num_stats.items():
        if (len(v[0]) == X) & (v[1][0] == K):
            return (k, v)

    for i in range(start, limit):
        num_stats[i].append(get_divisors(i))

    for i in range(start, limit):
        primes = 0
        for div in num_stats[i][0]:
            if is_prime(div):
                primes += 1
        num_stats[i].append([primes])
    # Post-Check
    for k, v in num_stats.items():
        if (len(v[0]) == X) & (v[1][0] == K):
            return (k, v)
    
        
    return 0



if __name__ == "__main__":
    T = int(input())
    start = 1
    limit = 100
    for _ in range(T):
        X, K = map(int, input().split())
        
        ans = strange_num(X, K, num_stats, start, limit)
        if ans == 0: 
            start = limit
            limit += 100
            print(strange_num(X, K, num_stats, start, limit)) 
        else:
            print(ans)