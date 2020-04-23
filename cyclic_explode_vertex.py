#
# k = 2
# a=[1,2,3,4]
# cur_index=1
# print((a, a[cur_index], cur_index, k))
# while len(a)>1:
#     if k >0:
#         cur_index = (cur_index+2)%(len(a))
#         k-=1
#         print((a, a[cur_index],cur_index, k))
#
#     else:
#         a.pop(cur_index)
#
#         print(len(a))
#         cur_index = ((cur_index+2)%(len(a)))-1
#         if cur_index < 0:
#             cur_index = len(a)+cur_index
#         print((a, a[cur_index], cur_index, k))


def vertex_exploder(N, K):
    vertices = [i for i in range(1, N+1)]
    cur_index = 1
    while len(vertices)>1:

        if K > 0:
            cur_index = (cur_index+2)%(len(vertices))
            K-=1

        else:
            vertices.pop(cur_index)
            cur_index = ((cur_index+2)%(len(vertices)))-1
            if cur_index < 0:
                cur_index = len(vertices)+cur_index
    return vertices[0]





if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        print(vertex_exploder(N, K))
