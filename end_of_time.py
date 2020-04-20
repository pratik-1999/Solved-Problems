import numpy as np
def food_count(p,m):
    pptn = 1
    food = 0
    for _ in range(39):
        food += p/pptn
        p += m
        pptn *= 2
    print(int(np.ceil(food)))
        

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        p, m = list(map(int, input().split()))
        food_count(p,m)