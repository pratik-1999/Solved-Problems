up_pitch = []
low_pitch = []

n = int(input('Enter no. of singers:'))



for i in range(n):
    print(f'Enter the lower limit of singer {i+1}: ')
    l = int(input())
    low_pitch.append(l)
    print(f'Enter the higher limit of singer {i+1}:')
    h = int(input())
    up_pitch.append(h)


pitch_range = [u - l for l, u in zip(low_pitch, up_pitch)]


def win_check(ls,n):
    k = 0
    score = [-1] * n
    for i in ls:
        for j in ls:
            if i > j:
                score[k] += 2
            elif i == j:        
                score[k] += 1
        k += 1
    print('final score:')
    print(score)

win_check(pitch_range,n)
