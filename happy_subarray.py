def happiness_check(sub_arr, H):
    counts = dict((x, sub_arr.count(x)) for x in set(sub_arr))
    for key in counts:
        if counts[key] != H[key-1]:
            return 0
    return 1



if __name__ == "__main__":
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    H = list(map(int, input().split()))
    # H_dict = dict((x+1, H[x]) for x in range(m))
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        subarray = A[l-1:r]
        print(happiness_check(subarray, H))
