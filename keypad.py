def time_table():
    test_cases = int(input())
    key_strokes = [".,?!1", 
                 "abc2",
                 "def3",
                 "ghi4",
                 "jkl5",
                 "mno6",
                 "pqrs7",
                 "tuv8",
                 "wxyz9",
                 " 0"
                ]
                
    time_taken = []
    
    for i in range(test_cases):
        current = 0
        time = 0
        word = input()
        for symbols in key_strokes:
            for symbol in word:
                if symbol in symbols:
                    idx = key_strokes.index(symbols)
                    sym_idx = symbols.index(symbol) + 1
                    if idx != current:
                        current = idx
                        time += 1 + sym_idx
                    else:
                        time += sym_idx
        time_taken.append(time)
                    
    print(time_taken)

if __name__ == "__main__":
    time_table()