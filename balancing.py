# import pdb

def gen_balance_check(word):
    top = -1
    open_close = {'(':')', '{':'}', '[':']'}
    if word[0] in open_close.values():
        return 'Unbalanced'
    else:
        top_char_list = []
        for i in range(len(word)):
            # pdb.set_trace()
            
            if word[i] in open_close.keys():
                top_char_list.append(word[i])
                top_char = top_char_list[-1]
                top += 1
                # print(f'{top_char}, {top}')
            elif word[i] in open_close.values():
                if open_close[top_char] == word[i]:
                    top -= 1
                    top_char_list.pop()
                    if i < len(word)-1:
                        top_char = top_char_list[-1]
                else:
                    return 'Unbalanced'

        if top == -1:
            return 'Balanced'
    


def balance_check(word):
    top = -1
    if word[0] == ')':
        print("Unbalanced")
    else:
        for w in word:
            if w == "(":
                top += 1
            elif w == ")":
                top -= 1
        
        if top == -1:
            print("Balanced")
        else:
            print("Unbalanced")

            
     
if __name__ == "__main__":
    word = input()
    print(gen_balance_check(word))




