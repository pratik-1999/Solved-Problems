
scores = 7
def calculate():
        avg = []
        grade = ''
        for i in range(scores):
            try :
                a = int(input())
                avg.append(a)
            except EOFError:
                break

        b = sum(avg)/scores
        if b in range(90,101):
            grade = 'O'
        elif b in range(80,90):
            grade = 'E'
        elif b in range(70,80):
            grade = 'A'
        elif b in range(55,70):
            grade = 'P'
        elif b in range(40,55):
            grade = 'D'
        else:
            grade = 'T'
        print(grade)

calculate()
