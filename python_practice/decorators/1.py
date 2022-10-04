def dis_marks(dist):
    def distinction(marks):
        for i in marks:
            if i > 75:
                print('distinction')
        dist(marks)        
    return distinction

@dis_marks
def student_marks(marks):
    for i in marks:
        if i >= 33:
            print('Pass')
        else:
            print('Fail')
            break
    else:
        print('pass')

m = [72,33,91,25]

student_marks(m)