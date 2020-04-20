import numpy as np
import math
# Write your code here
'''
Panda loves solving problems which are deemed impossible by his fellow classmates. The current problem which he is working on is to express a number N as sum of powers of number X (Not necessarily distinct) such that the number of powers of number X used should be minimum.

Note: The powers of a number can be 0, 1, 2, 3, 4, ...

Input Format:
The first line will contain T, the number of test cases. Then, T lines follow, each containing 2 space separated integers N and M.

Output Format:
For each test case, output the minimum number of such numbers (powers of M) which can be summed up to produce N.'''

def expr():
    t = int(input())
    cases = []
    for i in range(t):
        n, m = map(int, input().split())
        cases.append((n, m))
    # res = []
    #
    # for c in cases:
    #     rem = c[0]
    #     count = 0
    #     while rem>0:
    #         high = math.floor(math.log(rem, c[1]))
    #         rem = rem - pow(c[1], high)
    #         count += 1
    #     res.append(count)
    # print(res)
    return cases

expr()
