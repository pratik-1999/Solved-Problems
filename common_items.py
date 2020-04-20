import time
def common(array1, array2):
    if len(list(filter(lambda a1: a1 in array2, array1))) > 0:
        return True
    return False

def common_n2(array1, array2):
    for a1 in array1:
        for a2 in array2:
            if a1==a2:
                return True
    return False

def common_n3(array1:list, array2:list):
    if len(list(set(array1).intersection(set(array2)))) > 0:
        return True
    return False

if __name__=="__main__":
    a1 = list(range(0,10000000,2))
    a2 = list(range(50000,150000, 100))
    # t1 = time.time()
    # print(common(a1,a2))
    # print("time taken: "+ str(time.time()-t1))
    # t2 = time.time()
    # print(common_n2(a1,a2))
    # print("time taken: "+ str(time.time()-t2))
    t3 = time.time()
    print(common_n3(a1,a2))
    print("time taken: "+ str(time.time()-t3))