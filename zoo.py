def is_zoo():
    word = input()
    if len(word)%3 == 0 and len(word) >= 3:
        z_part = word[:int(len(word)/3)]
        o_part = word[int(len(word)/3):]
        if z_part == int(len(word)/3)*'z' and o_part == int(2*(len(word)/3))*'o':
            print('Yes')
        else:
            print('No')
            
    else:
        print('No')
        
        
        
if __name__ == "__main__":
    is_zoo()