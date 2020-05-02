import numpy as np
import time
def main(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    return np.min(arr2//arr1)

 # Write code here 

if __name__=="__main__":
    start = time.time()
    N = int(input())
    req_for_each = list(map(int, input().split()))
    total = list(map(int, input().split()))
    print(main(req_for_each, total))
    print(time.time()-start)