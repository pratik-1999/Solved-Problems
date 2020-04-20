import string

def get_substring(size, string):
    # alph = string.ascii_lowercase
    # idx_list = [alph.index(a)+1 for a in string]
    lex_great = ""
    for i in range(len(string)):
        lex_great = max(lex_great, string[i:])
        
    return lex_great
        


if __name__ == "__main__":
    size = int(input())
    string = input()
    print(get_substring(size, string))