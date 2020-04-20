
def recur_first(arr):
    lookup = {}
    for a in arr:
        if a not in lookup.keys():
            lookup[a] = 1
        else:
            lookup[a] += 1
            if lookup[a] == 2:
                return a

    return None


def recur_first2(arr): #faster as .keys() not used
    lookup = {}
    for a in arr:
        try:
            if lookup[a]:
                return a
            else:
                raise KeyError
        except KeyError:
            lookup[a] = 1
    return None


if __name__ == "__main__":
    arr = map(int, input().split())
    print(recur_first2(arr))