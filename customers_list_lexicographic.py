# Chotu's father is the owner of a Vada Pav shop. One Sunday, his father takes him to the shop.
# Father tells him that at the end of the day, Chotu has to give him a list consisting of the names 
# of all the customers on that day who bought Vada Pav(s) from the shop. The list should not have
# the names of any of the customers being repeated and it should be such that the lexicographically
# smallest name comes first, ie., the names should be sorted in dictionary order.

def list_lexify(customers_list):
    ''' Generates the lexicographically order list of unique customers by name.

    params: customer_list (list) : list of all customers.

    output: returns the lexicographical list of unique customers. 
    '''
    unique_customers = list(set(customers_list))
    unique_customers.sort()
    return unique_customers



if __name__=="__main__":
    N = int(input())
    customers_list = []
    for _ in range(N):
        cust = input()
        customers_list.append(cust)

    final_list = list_lexify(customers_list)
    print(len(final_list))
    print('\n'.join(final_list))
