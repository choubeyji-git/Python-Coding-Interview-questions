def distinction(dist_marks):
    def distMarks(marks):
        for i in marks:
            if i >= 75:
                print('Distinction')
        dist_marks(marks)        
    return distMarks        


@distinction
def student_marks(marks):
    for i in marks:
        if i >= 33:
            print('pass')
        else:
            print('fail')


marks = [76,34,33,54]
student_marks(marks)