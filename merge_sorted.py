
def merge_sorted(arrays:list):
    merged = [] 
    
    while len(min(arrays[0], arrays[1])) > 0:
        if arrays[0][0] <= arrays[1][0]:
            merged.append(arrays[0].pop(0))
            
        elif arrays[0][0] > arrays[1][0]:
            merged.append(arrays[1].pop(0))
    else:
        return max(arrays[0], arrays[1])
        
    for i in max(arrays[0], arrays[1]):
        merged.append(i) 

    return merged  






if __name__ == "__main__":
    arrays = [[6,9,13,21], [4,7,10,11]]
    print(merge_sorted(arrays))
    
    