def distinction(dis_marks):
    def dist(marks):
        for i in marks:
            if i >= 75:
                print(f'{i}: distinction')
        dis_marks(marks)        
    return dist


@distinction
def student_marks(marks):
    for i in marks:
        if i > 33:
            print(f'{i}:pass')
        else:
            print('fail')

my_marks = [79,34,35,36,34,75]

student_marks(my_marks)