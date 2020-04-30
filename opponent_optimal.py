def main(A1, A2):

    wins = 0
    if max(A1)<min(A2):
        return 0
        
    for a1 in A1:
        
        roi = [a2 for a2 in A2 if a2<a1]

        if roi:
            to_pop = max(roi)
            i = A2.index(to_pop)
            A2.pop(i)
            wins += 1
         
    return wins


if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        N = int(input())
        A1 = list(map(int, input().split()))
        A2 = list(map(int, input().split()))
        print(main(A1, A2))