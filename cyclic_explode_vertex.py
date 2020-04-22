
k = 2
a=[1,2,3,4]
prev_index=0
cur_index=1
while len(a)>1:
    if k >0:
        print((a, a[cur_index], cur_index))
        prev_index = cur_index
        cur_index = (cur_index+2)%(len(a))

        k-=1

    else:
        a.pop(cur_index)
        cur_index = ((prev_index+4)%(len(a)))



        print((a, a[cur_index], cur_index))
