pallindromes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202]
    

def get_count(p):
    
    t = int(input())
    for i in range(t):
        
        a, b = map(int, input().split())
        
        count = 0
        
        if b <= pallindromes[-1]:
            count += len(list(filter(lambda x: x>=a and x<=b, list(set(pallindromes)))))
            print(count)
            
        else:
            for n in range(203, b+1):
                if is_pallindrome(n):
                    pallindromes.append(n)
                    
            count += len(list(filter(lambda x: x>=a and x<=b, list(set(pallindromes)))))
            print(count)
            
        
        
        
def is_pallindrome(n):
    return str(n) == str(n)[::-1]
    
    
if __name__ == "__main__":
    get_count(pallindromes)