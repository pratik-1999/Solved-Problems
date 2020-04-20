import timeit

# def find_nemo(array):


def find_nemo(array):
    if "nemo" in list(filter(lambda x: x == "nemo" , array )):
        return "Found"
    return "Not found"


if __name__ == "__main__":
    a = ['rach', 'adfh', 'yter', 'nome', 'prax', 'rach', 'adfh', 'yter', 'nome', 'prax']
    print(find_nemo(a))
