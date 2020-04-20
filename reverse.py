def reverse_st(string):
    try:
        if type(string) != str or len(string) <= 1:
            raise ValueError
        else: 
            return string[::-1]

    except ValueError:
        print("The array input is either not string or of one character!")




if __name__ == "__main__":
    string = input()
    print(reverse_st(string))