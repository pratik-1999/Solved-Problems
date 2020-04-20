def has_pair(array, req_sum):
    array.sort()
    low, high = 0, len(array)-1    
    
    while low<high:
        ar_high = array[high]
        ar_low = array[low]
        cur_sum = ar_high+ar_low 
        if cur_sum == req_sum:
            return (ar_low, ar_high)
        elif cur_sum>req_sum:
            high -= 1
        elif cur_sum<req_sum:
            low += 1
    return False


def has_pair2(array, req_sum):
    comps = {}
    all_pairs = []
    for num in array:
        complement = req_sum-num
        keys = comps.keys()
        values = comps.values()
        if num not in keys:
            if num in values:
                all_pairs.append((num, complement))
            comps[num] = complement

    return all_pairs


    
        

if __name__=="__main__":
    a = [1,5,8,6,3,45,9,7]
    print(has_pair2(a, 9))