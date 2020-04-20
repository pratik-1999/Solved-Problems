import random
# Write your code here
def p_sort():
    '''
      n : no. of integers
      m : no. of index ranges
      Output: All ok if the list is sorted after sorting the substrings in the same order, else return the list of integers. 
    '''
    n, m = map(int, input().split())
    indexes = []
    perm = list(range(n))
    random.shuffle(perm)
    check = perm
    print(perm)
    for i in range(m):
        a,b = map(int, input().split())
        indexes.append((a,b))
    for i in indexes:
        j, k = i
        perm[j-1:k] = sorted(perm[j-1:k])
    if sorted(check) == perm:
        print('All ok!')
    else:
        print(*perm)

p_sort()
