def cyclic_left(b, m):
    shifted = b[m:] + b[:m]
    return int(shifted, 2)


def cyclic_right(b, m):
    shifted = b[-m:] + b[:-m]
    return int(shifted, 2)

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        N, m, c = input().split()
        N, m = map(int, [N, m])
        binary = '{0:016b}'.format(N)
        m = m%16
        if c == 'L':
            print(cyclic_left(binary, m))
        else:
            print(cyclic_right(binary, m))
