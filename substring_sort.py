from itertools import permutations
import random

def check():
    nums, subs = map(int, input().split())
    
    perm_list = list(range(1,nums+1))
    random.shuffle(perm_list)
    cases = []
    
    for i in range(subs):
        a, b = map(int, input().split())
        cases.append((a, b))
    p_test = perm_list 
    for case in cases:
        x, y = case
        p_test[x-1:y] = sorted(perm_list[x-1:y])
        
    if p_test == sorted(perm_list):
        print("All ok!")
        
    else:
        print(*perm_list)
    
    
if __name__ == "__main__":
    check()