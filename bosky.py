# Write your code here
def height_calc(n, A):
    for i in range(1, len(A)):
        B = rule_2(A, i)
        # for j in B: 
        #     A[j] += 1
        
        
    print(*A)
    
  
def rule_2(A, i):
    en = list(enumerate(A))
    return [en[req][0] for req in range(len(A[:i])) if A[req]>=A[i] ]
    
    
    
    
if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    height_calc(n, A)