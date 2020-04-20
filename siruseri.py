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

pitch = list(zip(low_pitch,up_pitch))


def win_check(ls,n):
    k = 0
    score = [0] * n
    for i in ls:
        for j in ls:
            if i[0] < j[0]:           #checking lower limit of pitch
                score[k] += 2
            elif i[0] == j[0]:        #if lower limit same then check higher limit.
                if i[1] > j[1]:       #Assuming draw isn't possible as per the question.
                    score[k] += 2
        k += 1
    print('final score:')
    print(score)

win_check(pitch,n)
